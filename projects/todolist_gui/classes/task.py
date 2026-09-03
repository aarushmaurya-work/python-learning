from pydantic import BaseModel, Field, field_serializer
from datetime import datetime
from typing import Literal


class Task(BaseModel):
    id: int = Field(...)
    title: str = Field(...)
    desc: str | None = None
    priority: Literal["low", "medium", "high"] = "medium"
    status : Literal["pending", "completed"] = "pending"
    time: datetime = Field(
        default_factory=datetime.now
    )  # default_factory is like you execute this function at the time of instance creation and get whatever the value is returned

    @field_serializer("time")
    def serialize_time(self, time : datetime) -> str:
        return time.isoformat()
        
