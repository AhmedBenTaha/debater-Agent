from typing import List

from crewai import Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class Debater:
    """Debater crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            verbose=True,
        )

    @agent
    def debater_for(self) -> Agent:
        return Agent(
            config=self.agents_config["debater_for"],
            verbose=True,
        )

    @agent
    def debater_against(self) -> Agent:
        return Agent(
            config=self.agents_config["debater_against"],
            verbose=True,
        )

    @agent
    def debate_judge(self) -> Agent:
        return Agent(
            config=self.agents_config["debate_judge"],
            verbose=True,
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
        )

    @task
    def debate_for_task(self) -> Task:
        return Task(
            config=self.tasks_config["debate_for_task"],
            context=[self.research_task()],
        )

    @task
    def debate_against_task(self) -> Task:
        return Task(
            config=self.tasks_config["debate_against_task"],
            context=[self.research_task()],
        )

    @task
    def debate_judge_task(self) -> Task:
        return Task(
            config=self.tasks_config["debate_judge_task"],
            context=[
                self.debate_for_task(),
                self.debate_against_task(),
            ],
            output_file="debate_report.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Debater crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )