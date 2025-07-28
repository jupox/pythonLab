from pydantic import BaseModel
from datetime import datetime

class TaskItem(BaseModel):
    id: str
    message: str
    type_task: str = "simple"
    status: str = "pending"
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()