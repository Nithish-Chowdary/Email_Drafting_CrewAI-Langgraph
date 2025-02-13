from crewai import Crew
from src.crew.tasks import EmailFilterTasks
from src.crew.agents import EmailFilterAgents


class EmailFilterCrew():

    def __init__(self):
        agents = EmailFilterAgents()
        self.filter_agent = agents.email_filter_agent()
        self.action_required_agent = agents.email_action_agent()
        self.writer_agent = agents.email_response_agent()

    def kickoff(self, state):
        tasks = EmailFilterTasks()
        crew = Crew(
            agents = [self.filter_agent, self.action_required_agent, self.writer_agent],
            tasks = [tasks.filter_emails_tasks(self.filter_agent, self._format_emails(state["emails"])),
                     tasks.action_required_email_task(self.action_required_agent),
                     tasks.draft_responses_task(self.writer_agent)
                     ],
            verbose= True,
        )

        result = crew.kickoff()
        print(f"updating state of action_required_emails: {result}")
        return {**state, "action_required_emails":result}

    def _format_emails(self, emails):
        emails_string = []

        for email in emails:
            print(email)

            arr = [
                f"ID: {email['id']}",
                f"- Thread ID: {email['threadId']}",
                f"- Snippet: {email['snippet']}",
                f"- From: {email['sender']}"
                f"--------------"
            ]

            emails_string.append("\n".join(arr))
        return "\n".join(emails_string)
