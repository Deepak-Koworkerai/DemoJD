import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Crew, Process
from Agents import Agents
from Tasks import Tasks
from logs import store_agent_output
import google.generativeai as genai


# Load variables from the .env file into the environment
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key)


llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             verbose=True,
                             temperature=0.5,
                             google_api_key= api_key
)


#   STATIC VARIABLE DECLARATION:
company_details = '''
                  Name : KoworkerAI,
                  Location : Dubai,AE,
                  website : www.kowrokerai.com,
                  contact mail : desmondmarshall@gmail.com
                  '''

# object creation
agents = Agents()
tasks = Tasks()

JDAgent = agents.JD_agent()

# get the requirements from the user for candidate
requirements = input("What are the requirements for the role? :")
Jd_task = tasks.draft_JD_task(JDAgent,requirements,company_details)


# create a Job object
crew = Crew(
    agents=[JDAgent],
    tasks=[Jd_task],
    verbose=True,
    process=Process.sequential,
    full_output=True,
    share_crew=False,
    step_callback=lambda x: store_agent_output(x,"MasterCrew Agent")
)

# Kick off the crew's work
results = crew.kickoff()
