import os
from smolagents import GoogleSearchTool, LiteLLMModel, CodeAgent, DuckDuckGoSearchTool,ToolCallingAgent, WebSearchTool

model = LiteLLMModel(
    model_id="groq/qwen/qwen3-32b", # Or "groq/llama-3.3-70b-versatile"
    api_key=os.environ.get("GROQ_API_KEY")
)

agent = CodeAgent(tools=[WebSearchTool()], model=model)
agent.run("Search for the best music recommendations for a party at the Wayne's mansion.")
