from src.graph.nodes import Nodes
from src.graph.state import EmailsState
from src.crew.crew import EmailFilterCrew
from langgraph.graph import StateGraph
from dotenv import load_dotenv
load_dotenv()


class WorkFlow():

    def __init__(self):
        nodes = Nodes()
        workflow = StateGraph(EmailsState)

        workflow.add_node("check_new_emails", nodes.check_email)
        workflow.add_node("wait_check_email_again", nodes.wait_check_email_again)
        workflow.add_node("draft_responses", EmailFilterCrew().kickoff)

        workflow.set_entry_point("check_new_emails")
        workflow.add_conditional_edges(
            "check_new_emails",
            nodes.new_emails,
            {
                "end": 'wait_check_email_again',
                "continue": 'draft_responses'
            }
                                       )

        workflow.add_edge("draft_responses", "wait_check_email_again")
        workflow.add_edge("wait_check_email_again", "check_new_emails")

        self.app = workflow.compile()


