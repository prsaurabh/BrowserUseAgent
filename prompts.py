class Task_Prompt:
    
    sensitive_data_ny = {'x_firstname': 'Curtis', 'x_lastname': 'Gill', 'x_state': 'New York'}
    
    Task_Prompt_NY_PDF = """
    Get detailed information of the real estate agent broker from the state in USA. 
    Gather information only from the State's website for real estate agent license search. 
    Name of the agent is x_firstname x_lastname from x_state.
    Prepare the report in the PDF with the information and download it. 
    
    Hint - 1. Ask user for information if you are stuck or enconter failures before giving up. 
           2. You can use Generate a PDF report.
           3. You can use Get sign-in or login credentials for a website with the given name only when needed ex: LinkedIn. 
           4. If you encounter a blue link with agent's name, click on it to get more information.
    """
    sensitive_data_fl = {'x_firstname': 'Jason', 'x_lastname': 'Crane', 'x_state': 'Florida'}
    
    Task_Prompt_FL_PDF = """
    Get detailed information of the real estate agent broker from the state in USA. 
    First try Gathering information from the State's website for real estate agent license search. Then try other web sites.
    Name of the agent is x_firstname x_lastname from florida.
    
    Hint - 1. Ask user for information if you are stuck or enconter failures before giving up. 
           2. You can use Generate a PDF re port.
           3. You can use Get sign-in or login credentials for a website with the given name only when needed ex: LinkedIn. 
           4. If you encounter a blue link with agent's name, click on it to get more information.
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

