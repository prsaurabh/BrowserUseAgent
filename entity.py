from pydantic import BaseModel
from prompts import System_Prompt
from browser_use import SystemPrompt
from typing import Optional

class AgentDetail(BaseModel):
    Name: str
    License_Type: str
    licence_Number: str
    License_Status: str
    Expiry_Date: str
    Address: str
    Related_Party_Name: str
    image_path: Optional[str] = "C:/temp/Agent.jpg"

class ImageRequest(BaseModel):
    image_path: str = "C:/temp/Agent.jpg"

class PDFDownloadRequest(BaseModel):
    url: str
    
class MySystemPrompt(SystemPrompt):
    def important_rules(self) -> str:
        rules = System_Prompt.System_Promt_Main
        return f'{rules}'