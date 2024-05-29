from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class RequestModel(BaseModel):
    batchid: str = Field(..., alias="batchid")
    payload: List[List[int]] = Field(..., alias="payload")


class ResponseModel(BaseModel):
    batchid: str
    response: List[int]
    status: str
    started_at: datetime
    completed_at: datetime
