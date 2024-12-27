from agentsai import Agent, Task, Crew
from agentsai_tools import SerperDevTool

# Create a research agent
researcher = Agent(
    role="Researcher",
    goal="Find latest AI news",
    backstory="You're an AI research analyst",
    tools=[SerperDevTool()]
)

# Create a research task
task = Task(
    description="Find and summarize latest AI news",
    expected_output="Bullet list of top 5 AI news",
    agent=researcher
)

# Create and run the crew
crew = Crew(
    agents=[researcher],
    tasks=[task],
    verbose=True
)

result = crew.start()
