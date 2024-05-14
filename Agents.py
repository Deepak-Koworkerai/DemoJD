from crewai import Agent
from textwrap import dedent
from logs import store_agent_output
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai


# Load variables from the .env file into the environment
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key)

llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             verbose=True,
                             temperature=0.5,
                             google_api_key= api_key )


class Agents():
    def JD_agent(self):
        return Agent(
            role='HR - Senior Job Description Writer',
            goal="""Generate job description based on requirements provided""",
            backstory=dedent("""\
            You are a HR executive working company, you are master at synthesizing a variety of Job descriptions
            that will address the requirements mentioned."""),
            llm=llm,
            verbose=True,
            allow_delegation=False,
            max_iter=5,
            memory=True,
            step_callback=lambda x: store_agent_output(x,"HR - Senior Job Description Writer"),
        )
    def resume_filter_agent(self):
		    return Agent(
			role='Senior Resume Analyst',
			goal='Filter out non-essential resume looking into the provided job description',
			backstory=dedent("""\
				As a Senior Resume Analyst, You excel in filtering and analyzing resumes to identify top candidates for
        various positions. With extensive experience in screening and shortlisting resumes,
        you possess a keen eye for detail and a knack for discerning key qualifications and attributes from the provided resume
        """),
      llm=llm,
			verbose=True,
			allow_delegation=False,
      max_iter=5,
      memory=True,
      step_callback=lambda x: store_agent_output(x,"Senior Resume Analyst")

		)
