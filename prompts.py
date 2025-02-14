class Task_Prompt:
    
    Task_Prompt1 = """
    Get detailed information of the real estate agent broker from the state in USA. 
    Make sure to gather information from finding State's real estate agent license search website and get info from State's website only 
    Name of the agent is Curtis Gill from NEw York.
    Prepare the report in the PDF with the information and download it. 
    
    Hint - 1. Ask user for information if you are stuck or enconter failures before giving up. 
           2. You can use Generate a PDF report.
           3. You can use Get sign-in or login credentials for a website with the given name only when needed ex: LinkedIn. 
           4. When you encounter a blue link with agent's name, click on it to get more information.
    """

    Task_Prompt2 = """
    Download the Form for Transit Benefits Plan which is a commuter form by NYC employees. 
    Hint - 1. Ask the user for information if you are stuck. 
           2. You can use Download a PDF file from the provided URL.
    """

    Task_Prompt3 = """
    Verify if licence number and Licence Type Associate Broker is correct for the real estate agent from the state of New York. 
    Make sure to verify from the state website of this info. 
    Hint - 1. Ask user for information if you are stuck. 
           2. Ask user for information abt the Broker name or licence number when you need it. 
    """

class System_Prompt:

    System_Promt1 = """
            MOST IMPORTANT RULE:
                - ALWAYS search Google first if exact url is not provided!!
            """

      
