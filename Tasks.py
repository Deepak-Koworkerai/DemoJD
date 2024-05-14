from crewai import Task

class Tasks():

    def draft_JD_task(self, agent,requirements,company_details):
        return Task(
        description=f"""Draft a comprehensive job description based on the gathered requirements. \
            Use the provided requirements to outline the responsibilities, qualifications, and \
            any other relevant details for the position. \

            REQUIREMENTS:\n\n {requirements} \n\n
            Company details ; \n\n {company_details} \n\n


            """,


        expected_output="""A well-crafted job description that accurately represents the position \
            and its requirements""",
        context=[],
        agent=agent,
        output_file="draft_job_description.txt",
    )

    def filter_resumes_task(self, agent, requirements, resume, short_listed):
        return Task(
            description=f"""\
                Analyze a batch of resumes and filter out non-essential ones.

                Utilize your expertise in resume screening to identify top candidates
                for the next round of evaluation. Pay attention to key qualifications,
                experience, and skills.

                Make sure to filter out resumes that do not meet the minimum criteria
                for the position and focus on selecting those that align closely with
                the job requirements

                requirements : {requirements}

                RESUMES
                -----------------
                      {resume}
                If the resume is eligible then append the resume candidate name, email, phone, LinkedIn
                into the short_listed list {short_listed} as a dictionary
            """,
            expected_output="""List of shortlisted candidates""",
            context=[],
            input_data=(requirements, resume, short_listed),
            agent=agent,
            output_file='shortListedCandidates.txt'
        )
