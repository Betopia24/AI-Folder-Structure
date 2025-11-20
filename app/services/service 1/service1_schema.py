from pydantic import BaseModel
from typing import Optional,List, Any

class service1_request(BaseModel):
    example_field: str
class service1_response(BaseModel):
    example_field: Any