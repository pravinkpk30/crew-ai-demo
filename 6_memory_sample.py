"""
Memory-Enabled CrewAI Example
----------------------------
This script demonstrates how to use CrewAI with memory capabilities to maintain context
between multiple agent interactions. It creates a research and writing crew that can
remember previous conversations and build upon them.

Key Features:
- Uses Gemini 2.0 Flash model for LLM
- Implements memory persistence between crew executions
- Configures Google's text embedding for memory retrieval
- Shows how to chain multiple agent tasks with context

Environment Variables Required:
- GEMINI_API_KEY: API key for Google's Gemini model
- SERPER_API_KEY: API key for Serper.dev search functionality
"""

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Import required libraries
import os
from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool

# Initialize the LLM with Gemini 2.0 Flash
# Temperature is set low (0.1) for more focused and deterministic outputs
llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.1,
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Create a Research Specialist agent
# This agent is responsible for finding factual information online
research_agent = Agent(
    role="Research Specialist",
    goal="Research interesting facts about the topic: {topic}",
    backstory="You are an expert at finding relevant and factual data.",
    tools=[SerperDevTool()],  # Enable web search capability
    verbose=True,  # Show detailed execution logs
    llm=llm  # Use the configured LLM
)

# Create a Creative Writer agent
# This agent transforms research into engaging content
writer_agent = Agent(
    role="Creative Writer",
    goal="Write a short blog summary using the research",
    backstory="You are skilled at writing engaging summaries based on provided content.",
    llm=llm,  # Use the same LLM instance
    verbose=True,
)

# Define the research task
# This task will be executed by the research_agent
task1 = Task(
    description="Find 3-5 interesting and recent facts about {topic} as of year 2025.",
    expected_output="A bullet list of 3-5 facts",
    agent=research_agent,
)

# Define the writing task
# This task depends on the output of task1
task2 = Task(
    description="Write a 100-word blog post summary about {topic} using the facts from the research.",
    expected_output="A blog post summary",
    agent=writer_agent,
    context=[task1],  # Pass the research task as context
)

# Create and configure the crew
# The crew coordinates the agents and manages task execution
crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[task1, task2],
    verbose=True,  # Enable detailed logging
    memory=True,  # Enable memory for the crew
    # Configure the embedding model for memory
    embedder={
        "provider": "google",
        "config": {
            "api_key": os.getenv("GOOGLE_API_KEY"),  # Use the API key from environment
            "model": "text-embedding-004"  # Google's text embedding model
        }
    }
)

# Execute the crew with the first topic
print("\n" + "="*80)
print("RESEARCHING: The future of electrical vehicles".center(80))
print("="*80)
crew.kickoff(inputs={"topic": "The future of electrical vehicles"})

# Execute the crew with a follow-up topic
# The memory system will maintain context between these executions
print("\n" + "="*80)
print("FOLLOW-UP: Revenue outlook in the EV sector".center(80))
print("="*80)
crew.kickoff(inputs={"topic": "What is the revenue outlook in this sector?"})