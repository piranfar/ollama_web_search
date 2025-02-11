# -*- coding: utf-8 -*-
import os
from langchain_ollama.llms import OllamaLLM  # ✅ Correct Import
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from colorama import Fore, Style
from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()

@app.get("/realtime-search")
def realtime_search(query: str = Query(..., description="Your search query")):
    """API endpoint for real-time search in Open WebUI."""
    return {"response": query_with_web_search(query)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


    
# Load SerpAPI Key securely from environment variables
SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")
if not SERPAPI_KEY:
    raise ValueError("ERROR: SerpAPI Key is missing! Set SERPAPI_API_KEY in your environment.")

# Load Dolphin-Mistral model from Ollama
llm = OllamaLLM(model="dolphin-mistral")  # ✅ Replace "mistral" with the chosen model

# Configure Web Search
search = SerpAPIWrapper()

# Create an agent that integrates Ollama with Web Search
agent = initialize_agent(
    tools=[Tool(name="Search", func=search.run, description="Use this tool to fetch live information from the internet.")],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,  
    verbose=False,
    return_intermediate_steps=True  # ✅ Forces AI to use the Search tool
)
# Function to query the AI with web search
def query_with_web_search(prompt):
    """Runs a query through the AI agent with live web search capability."""
    try:
        # ✅ If the question is about time or date, force a web search
        if "time" in prompt.lower() or "date" in prompt.lower():
            return search.run(prompt)  # Directly query SerpAPI for real-time info

        response = agent.run(prompt.strip())
        return response
    except Exception as e:
        return "Error occurred: {}".format(e)


# Interactive Mode for Continuous Queries
if __name__ == "__main__":
    print("\n" + Fore.CYAN + "Ollama AI with Live Web Search (Type 'exit' to quit)" + Style.RESET_ALL)
    
    while True:
        user_input = input("\n" + Fore.YELLOW + "Ask me anything: " + Style.RESET_ALL).strip()
        
        if user_input.lower() == "exit":
            print(Fore.GREEN + "Exiting... Have a great day!" + Style.RESET_ALL)
            break
        
        response = query_with_web_search(user_input)
        print("\n" + Fore.BLUE + "AI Response:" + Style.RESET_ALL + "\n")
        print(response)
