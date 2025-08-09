from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from crewai import LLM

load_dotenv()

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.1
)

research_agent = Agent(
    role="Research Specialist",
    goal="Research interesting facts about the topic: {topic}",
    backstory="You are an expert at finding relevant and factual data.",
    tools=[SerperDevTool()], # Add tools to the agent
    verbose=True,
    llm=llm
)

writer_agent = Agent(
    role="Creative Writer",
    goal="Write a short blog summary using the research",
    backstory="You are skilled at writing engaging summaries based on provided content.",
    llm=llm,
    verbose=True,
)

task1 = Task(
    description="Find 3-5 interesting and recent facts about {topic} as of year 2025.",
    expected_output="A bullet list of 3-5 facts",
    agent=research_agent,
)

task2 = Task(
    description="Write a 100-word blog post summary about {topic} using the facts from the research.",
    expected_output="A blog post summary",
    agent=writer_agent,
    context=[task1],
)

crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[task1, task2],
    verbose=True,
)

response = crew.kickoff(inputs={"topic": "The future of electrical vehicles"})
print(response)