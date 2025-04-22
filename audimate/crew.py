# src/audimate/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class AudimateCrew():
    """Audimate crew for the Saudi film industry casting assistant"""
    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def script_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['script_analyst'],
            verbose=True,
            tools=[SerperDevTool()]  # Add relevant tools for script analysis
        )

    @agent
    def rubric_editor(self) -> Agent:
        return Agent(
            config=self.agents_config['rubric_editor'],
            verbose=True
        )

    @agent
    def video_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['video_analyzer'],
            verbose=True,
            tools=[SerperDevTool()]  # Add relevant tools for video analysis
        )

    @agent
    def matching_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['matching_agent'],
            verbose=True
        )

    @agent
    def learning_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['learning_agent'],
            verbose=True
        )

    @task
    def script_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['script_analysis_task'],
        )

    @task
    def rubric_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['rubric_creation_task'],
        )

    @task
    def performance_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['performance_analysis_task'],
        )

    @task
    def actor_matching_task(self) -> Task:
        return Task(
            config=self.tasks_config['actor_matching_task'],
        )

    @task
    def feedback_learning_task(self) -> Task:
        return Task(
            config=self.tasks_config['feedback_learning_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Audimate crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,  # Define process for task execution
            verbose=True,
        )
