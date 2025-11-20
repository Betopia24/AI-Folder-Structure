"""Routes for Service 2 - Simple Fitness Helper

This module defines the API endpoints for the fitness service.
"""

from fastapi import APIRouter, HTTPException
from .service2 import Service2
from .service2_schema import service2_request, service2_response
from ...utils.common_utils import setup_logger

# Create router and service instance
router = APIRouter()
service2 = Service2()
logger = setup_logger("Service2Route")

@router.post("/service2", response_model=service2_response)
async def get_fitness_advice(request: service2_request):
    """
    Get fitness advice from the AI coach.
    
    Args:
        request: Contains the user's fitness question
        
    Returns:
        Response with fitness advice
        
    Example:
        POST /service2
        {"question": "I want to exercise but I'm a beginner"}
    """
    try:
        logger.info("Someone asked for fitness advice")
        
        # Process the request
        response = service2.get_service2(request.dict())
        
        logger.info("Successfully provided fitness advice")
        return response
        
    except Exception as e:
        logger.error(f"Failed to provide fitness advice: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
