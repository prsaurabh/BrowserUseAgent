from pydantic import BaseModel
from pathlib import Path
import aiohttp
from fpdf import FPDF
from browser_use import ActionResult, Browser, Controller
from credentials import credentials_store
from entity import AgentDetail, ImageRequest, PDFDownloadRequest, AgentDetails
import json

def setup_controllers(controller: Controller):

    @controller.action('Ask user for information')
    def ask_human(question: str) -> str:
        answer = input(f'\n{question}\nInput: ')
        return ActionResult(extracted_content=answer)

    @controller.action("Download a PDF file from the provided URL",
    param_model=PDFDownloadRequest
    )
    async def download_pdf(params: PDFDownloadRequest, browser: Browser):
        pdf_url = params.url
        save_path = Path("C:/temp/downloaded_report.pdf")  # Change the path if needed

        async with aiohttp.ClientSession() as session:
            async with session.get(pdf_url) as response:
                if response.status == 200:
                    save_path.write_bytes(await response.read())
                    return ActionResult(
                        success=True,
                        extracted_content=f"PDF downloaded successfully at {save_path}"
                    )
                else:
                    return ActionResult(
                        success=False,
                        extracted_content="Failed to download the PDF."
                    )
    
    @controller.action("Get the Agents's image only if not found after trying",
    param_model=ImageRequest
    )
    async def get_broker_image(params: ImageRequest) -> ActionResult:
        image_path = Path(params.image_path)

        if not image_path.exists():
            return ActionResult(
                success=False,
                extracted_content="Image file not found."
            )

        # Read the image file and provide it to the agent
        image_data = image_path.read_bytes()  # Read as binary
        
        return ActionResult(
            success=True,
            extracted_content="Broker image provided.",
            image=image_data
        )
    
    @controller.action("Get sign-in or login credentials for a website with the given name ex: LinkedIn")
    def get_login_credentials(website: str) -> ActionResult:
        credentials = credentials_store.get(website.lower(), "")
        return ActionResult(extracted_content=credentials)

    
    @controller.action("Generate a PDF report", param_model=AgentDetail)
    async def generate_pdf_report(params: AgentDetail) -> ActionResult:
        pdf_file_path = "C:/temp/agent_report.pdf"
        
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        
        # Title
        pdf.set_font("Arial", style='B', size=16)
        pdf.cell(200, 10, "Agent Report", ln=True, align='C')
        pdf.ln(10)
    
        pdf.set_font("Arial", size=12)
        
        # Add AgentDetail fields to PDF
        pdf.cell(200, 10, f"Name: {params.Name}", ln=True)
        pdf.cell(200, 10, f"License Type: {params.License_Type}", ln=True)
        pdf.cell(200, 10, f"License Number: {params.licence_Number}", ln=True)
        pdf.cell(200, 10, f"License Status: {params.License_Status}", ln=True)
        pdf.cell(200, 10, f"Expiry Date: {params.Expiry_Date}", ln=True)
        pdf.cell(200, 10, f"Address: {params.Address}", ln=True)
        pdf.cell(200, 10, f"Related Party Name: {params.Related_Party_Name}", ln=True)
        
        pdf.ln(10)
    
        # Save PDF
        pdf.output(pdf_file_path)
    
        # Store agent details in a variable or file
        agent_details = params.dict()
        with open("C:/temp/agent_details.json", "w") as f:
            json.dump(agent_details, f)
    
        return ActionResult(
            success=True,
            extracted_content=f"PDF report created at {pdf_file_path}",
            file_path=pdf_file_path,
            agent_details=agent_details
        )

