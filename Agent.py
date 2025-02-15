import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent, Controller, Browser, BrowserConfig, SystemPrompt, ActionResult
from controllers import setup_controllers, agent_store
from config import OPENAI_API_KEY, PLANNER_API_KEY
from prompts import Task_Prompt
from entity import MySystemPrompt

async def main():
    # API Keys
    llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)
    planner_llm = ChatOpenAI(model='gpt-4o', api_key=PLANNER_API_KEY)

    controller = Controller()
    setup_controllers(controller)
    
    browser_config = BrowserConfig(headless=False)
    browser = Browser(config=browser_config)
            
    # Agent
    agent = Agent(
        task=Task_Prompt.Task_Prompt_NY_PDF,
        llm=llm,
        planner_llm=planner_llm,
        controller=controller,
        browser=browser,  
        use_vision=True,
        use_vision_for_planner=True,
        planner_interval=4,
        system_prompt_class=MySystemPrompt,
        save_conversation_path="C:\\temp\\log",
        #generate_gif=True,
        max_failures=10,
        retry_delay=5
    )

    history = await agent.run(max_steps=100)

    stored_agent = agent_store.get_data()
    
    if stored_agent:
        try:
            print('\n--------------------------------')
            for field_name, value in stored_agent.dict().items():
                display_name = field_name.replace('_', ' ').title()
                print(f'{display_name}: {value}')
        except Exception as e:
            print(f'Error processing details: {e}')
    else:
        print('No data found')
    
    await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
