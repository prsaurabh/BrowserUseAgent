import asyncio, json, os
from langchain_openai import ChatOpenAI
from browser_use import Agent, Controller, Browser, BrowserConfig, SystemPrompt, ActionResult
from controllers import setup_controllers
from config import OPENAI_API_KEY, PLANNER_API_KEY, File_Generated
from prompts import Task_Prompt
from entity import AgentDetail, MySystemPrompt
from pydantic import ValidationError

async def main():
    # API Keys
    llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)
    planner_llm = ChatOpenAI(model='03-mini', api_key=PLANNER_API_KEY)

    controller = Controller()
    setup_controllers(controller)
    
    browser_config = BrowserConfig(headless=False)
    browser = Browser(config=browser_config)
    
    prompt = Task_Prompt.Task_Prompt_FL_PDF
            
    # Agent
    agent = Agent(
        task=prompt,
        llm=llm,
        planner_llm=planner_llm,
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

    history = await agent.run(max_steps=100)

    result = history.final_result()
    
    if result and os.path.exists(File_Generated):
        try:
            # Load agent details generated while building PDF
            with open(File_Generated, "r") as f:
                agent_details = json.load(f)
            
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
        print(result)
    await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
