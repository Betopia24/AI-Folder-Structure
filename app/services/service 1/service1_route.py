"""Routes for Service 1 - General AI Assistant

This module defines the API endpoints for the general AI assistant service.
"""

from fastapi import APIRouter, HTTPException
from .service1 import Service1
from .service1_schema import service1_request, service1_response
from ...utils.common_utils import setup_logger

# Create router and service instance
router = APIRouter()
service1 = Service1()
logger = setup_logger("Service1Route")

@router.post("/service1", response_model=service1_response)
async def get_ai_assistance(request: service1_request):
    """
    Get general AI assistance.
    
    Args:
        request: Contains the user's question or request
        
    Returns:
        Response with AI assistance
        
    Example:
        POST /service1
        {"example_field": "What is the capital of France?"}
    """
    try:
        logger.info("Someone asked for AI assistance")
        
        # Process the request
        response = service1.get_service1(request.dict())
        
        logger.info("Successfully provided AI assistance")
        return response
        
    except Exception as e:
        logger.error(f"Failed to provide AI assistance: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
