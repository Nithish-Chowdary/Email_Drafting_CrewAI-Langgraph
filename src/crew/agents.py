from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.get_thread import GmailGetThread
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.llms import Ollama


from textwrap import dedent
from crewai import Agent
from src.crew.tools import CreateDraftTool



class EmailFilterAgents():

    def __init__(self):
        self.gmail = GmailToolkit()
        #self.llm = ChatOpenAI(model_name="gpt-3.5-turbo")
        self.llm = Ollama(model="llama3.1")


    def email_filter_agent(self):
        return Agent(
            role='Senior Email Analyst',
            goal='Filter out non-essential emails like newsletters and promotional content',
            backstory=dedent("""\
            				As a Senior Email Analyst, you have extensive experience in email content analysis.
            				You are adept at distinguishing important emails from spam, newsletters, and other
            				irrelevant content. Your expertise lies in identifying key patterns and markers that
            				signify the importance of an email."""),
            llm = self.llm,
            verbose=True,
            allow_delegation=False
        )


    def email_action_agent(self):
        return Agent(
            role="Email Action Specialist",
            goal="Identify action required emails and compile list of their ID's",
            backstory=dedent("""\ 
                    As an AI agent specializing in email analysis. Your core skill is understanding context to identify
                      emails requiring action. You assess urgency, importance, and intent based on content, tone,
                      and sender. Your goal is to ensure no critical email is overlooked, prioritizing effectively and 
                      summarizing key points for quick decision-making."""),
            tools = [
                GmailGetThread(api_resource=self.gmail.api_resource),
                TavilySearchResults()
            ],
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )

    def email_response_agent(self):
        return Agent(
            role="Email Response Writer",
            goal="Draft Responses to action-required Emails",
            backstory=dedent("""\ 
            you are specialist writer, crafting responses to action-required emails. Your expertise lies in
             clear, concise, and effective communication. You tailor responses based on context, ensuring they are 
             professional yet friendly. Your goal is to provide well-structured replies that address key points, 
             maintain a positive tone, and drive action efficiently."""),
            tools=[
                TavilySearchResults(),
                GmailGetThread(api_resource=self.gmail.api_resource),
                CreateDraftTool.create_draft
            ],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
        )
