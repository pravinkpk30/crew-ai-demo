"""
CrewAI Blog Writing Crew Configuration
-------------------------------------
This module defines a CrewAI crew for automated blog post generation using a multi-agent system.
The crew consists of specialized agents working together to research and write blog content.

Key Components:
- Researcher Agent: Gathers information using SerperDev for web search
- Writer Agent: Creates well-structured blog posts from research
- Tasks: Research and blog writing tasks with configurations in YAML files

Configuration Files:
- config/agents.yaml: Defines agent roles, goals, and backstories
- config/tasks.yaml: Contains task descriptions and expected outputs

Environment Variables Required:
- SERPER_API_KEY: API key for Serper.dev search functionality
- GOOGLE_API_KEY: API key for Google's Gemini model

Usage:
    python 5_crew_config_sample.py
"""

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, DirectoryReadTool, FileWriterTool, FileReadTool
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

@CrewBase
class BlogCrew():
    """
    Blog Writing Crew
    
    A specialized crew that automates the process of researching and writing blog posts.
    The crew consists of multiple agents working together to produce high-quality content.
    
    Attributes:
        agents_config (str): Path to the YAML file containing agent configurations
        tasks_config (str): Path to the YAML file containing task configurations
    """
    
    # Paths to configuration files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        """
        Creates and configures the Researcher agent.
        
        The researcher is responsible for gathering information using web search tools.
        
        Returns:
            Agent: Configured Researcher agent instance
        """
        return Agent(
            config=self.agents_config['research_agent'],  # Load from YAML config
            tools=[
                SerperDevTool(),
                # Additional tools can be added here
            ],
            verbose=True  # Enable verbose output for debugging
        )

    @agent
    def writer(self) -> Agent:
        """
        Creates and configures the Writer agent.
        
        The writer takes research data and transforms it into well-structured blog content.
        
        Returns:
            Agent: Configured Writer agent instance
        """
        return Agent(
            config=self.agents_config['writer_agent'],  # Load from YAML config
            verbose=True  # Enable verbose output for debugging
        )

    @task
    def research_task(self) -> Task:
        """
        Defines the research task for the Researcher agent.
        
        Returns:
            Task: Configured research task instance
        """
        return Task(
            config=self.tasks_config['research_task'],  # Load from YAML config
            agent=self.researcher()
        )

    @task
    def blog_task(self) -> Task:
        """
        Defines the blog writing task for the Writer agent.
        
        Returns:
            Task: Configured blog writing task instance
        """
        return Task(
            config=self.tasks_config['blog_task'],  # Load from YAML config
            agent=self.writer(),
            context=[self.research_task()]  # Make research task output available
        )

    @crew
    def crew(self) -> Crew:
        """
        Assembles and configures the complete crew.
        
        Returns:
            Crew: Configured crew instance with agents and tasks
        """
        return Crew(
            agents=[self.researcher(), self.writer()],
            tasks=[self.research_task(), self.blog_task()],
            process=Process.sequential,  # Run tasks in sequence
            verbose=True  # Detailed logging
        )


if __name__ == "__main__":
    # Create and run the blog writing crew
    blog_crew = BlogCrew()
    result = blog_crew.crew().kickoff(
        inputs={
            "topic": "The future of electrical vehicles"  # Default topic, can be overridden
        }
    )
    print(result)