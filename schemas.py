from typing import Optional

from pydantic import BaseModel, ConfigDict


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class SSubtaskAdd(BaseModel):
    task_id: int
    description: str


class STask(STaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SSubtask(SSubtaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STaskId(BaseModel):
    ok: bool = True
    task_id: int


class SSubtaskId(BaseModel):
    ok: bool = True
    subtask_id: int