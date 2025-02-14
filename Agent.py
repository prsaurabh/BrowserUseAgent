import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent, Controller, Browser, BrowserConfig, SystemPrompt, ActionResult
from controllers import setup_controllers
from credentials import credentials_store
from config import OPENAI_API_KEY, PLANNER_API_KEY
from prompts import Task_Prompt
from entity import AgentDetail, MySystemPrompt
from pydantic import ValidationError
import json

async def main():
    # API Key initialization
    llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)
    planner_llm = ChatOpenAI(model='o1-mini', api_key=PLANNER_API_KEY)

    controller = Controller()
    setup_controllers(controller)
    
    browser_config = BrowserConfig(headless=False)
    browser = Browser(config=browser_config)
            
    # Create Agent
    agent = Agent(
        task=Task_Prompt.Task_Prompt1,
        llm=llm,
        #planner_llm=planner_llm,
        controller=controller,
        browser=browser,  
        use_vision=True,
        use_vision_for_planner=False,
        planner_interval=4,
        system_prompt_class=MySystemPrompt,
        save_conversation_path="C:\\temp\\log",
        #generate_gif=True,
        max_failures=10,
        retry_delay=5
    )

    # Run Agent
    history = await agent.run(max_steps=100)

    # Retrieve and process the final result
    result = history.final_result()
    if result:
        try:
            # Load agent details from the stored file
            with open("C:/temp/agent_details.json", "r") as f:
                agent_details = json.load(f)
            
            # Parse the result using the defined Pydantic model
            parsed: AgentDetail = AgentDetail(**agent_details)
            print('\n--------------------------------')
            print(f'Name: {parsed.Name}')
            print(f'License Type: {parsed.License_Type}')
            print(f'License Number: {parsed.licence_Number}')
            print(f'License Status: {parsed.License_Status}')
            print(f'Expiry Date: {parsed.Expiry_Date}')
            print(f'Address: {parsed.Address}')
            print(f'Company: {parsed.Related_Party_Name}')
            print(result)
        except ValidationError as e:
            print(f'Error parsing result: {e}')
    else:
        print('No result')
    await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
