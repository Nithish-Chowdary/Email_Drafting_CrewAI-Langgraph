# EMAIL DRAFTING ASSISTANT | CrewAI + LangGraph

## Introduction
This project demonstrates the integration of CrewAI with LangChain and LangGraph to automate email checking and drafting. CrewAI orchestrates autonomous AI agents that collaborate and perform tasks efficiently, allowing you to automatically draft emails based on incoming messages.


## CrewAI Framework
CrewAI enables AI agents to work together in a collaborative and efficient manner. In this project, CrewAI agents are orchestrated to automate email checking and drafting, making communication management easier and faster.


## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:Nithish-Chowdary/Email_Drafting_CrewAI-Langgraph.git
   cd Email_Drafting_CrewAI-LangGraph
   ```
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
## Environment Variables
Create a `.env` file with the following variables:

```env
MY_EMAIL=
TAVILY_API_KEY=
```

## Running the Code
This example uses DEEPSEEK R1-1.5b parameter model

 - Configure Environment: create a .env and set up the environment variable
 - Setup a credentials.json: Follow the [google instructions](https://developers.google.com/gmail/api/quickstart/python#authorize_credentials_for_a_desktop_application), once you’ve downloaded the file, name it credentials.json and add to the root of the project,
 - Execute the Script: Run python main.py

## Details & Explanation
 - Running the Script: Execute python main.py
 - Key Components:
   - ./src/graph/graph.py: Class defining the nodes and edges.
   - ./src/graph/nodes.py: Class with the function for each node.
   - ./src/graph/state.py: State declaration.
   - ./src/crew/agents.py: Class defining the CrewAI Agents.
   - ./src/crew/tasks.py: Class definig the CrewAI Tasks.
   - ./src/crew/crew.py: Class defining the CrewAI Crew.
   - ./src/crew/tools.py: Class implementing the GmailDraft Tool.
