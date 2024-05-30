from fastapi import APIRouter, HTTPException
from app.models.add_models import RequestModel, ResponseModel
from app.services.add_service import process_addition
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/process", response_model=ResponseModel)
async def process_request(request: RequestModel):
    started_at = datetime.now()
    logger.info(f"Processing request with batchid: {request.batchid} started at {started_at.isoformat()}")

    try:
        # Attempt to process the addition
        result = process_addition(request.payload)
    except Exception as e:
        # Log the exception with a stack trace
        logger.exception(f"An error occurred while processing the request with batchid: {request.batchid}")
        # Respond with an HTTP error
        raise HTTPException(status_code=500, detail=str(e))

    completed_at = datetime.now()
    logger.info(f"Processing request with batchid: {request.batchid} completed at {completed_at.isoformat()}")

    # Create the response model
    response = ResponseModel(
        batchid=request.batchid,
        response=result,
        status="complete",
        started_at=started_at.isoformat(),
        completed_at=completed_at.isoformat()
    )

    # Log the successful processing of the request
    logger.info(f"Request with batchid: {request.batchid} processed successfully")

    return response
