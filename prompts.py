class Task_Prompt:
    
    Task_Prompt_NY_PDF = """
    Get detailed information of the real estate agent broker from the state in USA. 
    Gather information only from the State's website for real estate agent license search. 
    Name of the agent is Curtis Gill from New York.
    Prepare the report in the PDF with the information and download it. 
    
    Hint - 1. Ask user for information if you are stuck or enconter failures before giving up. 
           2. You should use Get agent details after collecting the information.
           3. You can use Generate a PDF report.
           4. You can use Get sign-in or login credentials for a website with the given name only when needed ex: LinkedIn. 
           5. If you encounter a blue link with agent's name, click on it to get more information.
    """
    Task_Prompt_FL = """
    Get detailed information of the real estate agent broker from the state in USA. 
    First try Gathering information from the State's website for real estate agent license search. Then try other web sites.
    Name of the agent is Jason Crane from Florida.
    
    Hint - 1. Ask user for information if you are stuck.
           2. You should use Get agent details after collecting the information.
           3. If you encounter a blue link with agent's name, click on it to get more information.
    """
    Task_Prompt_Down = """
    Find the Form for Transit Benefits Plan which is a commuter form by NYC employees. 
    Find the editable version of the form.
    Fill the sample data in the form and download the filled form.
    Hint - 1. Ask the user for information if you are stuck. 
           2. You can use Download a PDF file from the provided URL.
    """

    Task_Prompt_Verify = """
    Verify if licence number and Licence Type of the Associate Broker is correct for the real estate agent from the state of New York. 
    Gather information from the State's websites meant for real estate agent license search.  
    Hint - 1. Ask user for information if you are stuck. 
           2. Ask user for information abt the Broker name or licence number when you need it. 
    """

class System_Prompt:

    System_Promt_Main = """
            MOST IMPORTANT RULE:
                - ALWAYS search Google first if exact url is not provided!!
                - If you are stuck, ask user for information.       
                """

