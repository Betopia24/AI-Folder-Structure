from pydantic import BaseModel
from typing import Optional

class service2_request(BaseModel):
    """Simple request model for service2 - just ask for what you want!"""
    question: str = "Give me a simple workout"
    
class service2_response(BaseModel):
    """Simple response model for service2"""
    answer: str