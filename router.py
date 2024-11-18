from fastapi import APIRouter, Depends
from typing import Annotated

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId, SSubtask, SSubtaskAdd, SSubtaskId

router = APIRouter()

@router.post(path='/tasks', tags=['Tasks'])
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepository.add_task(task)
    return {'ok': True, 'task_id': task_id}


@router.post(path='/subtasks', tags=['Subtasks'])
async def add_subtask(
        subtask: Annotated[SSubtaskAdd, Depends()],
) -> SSubtaskId:
    subtask_id = await TaskRepository.add_subtask(subtask)
    return {'ok': True, 'subtask_id': subtask_id}


@router.get(path='/tasks', tags=['Tasks'])
async def get_all_tasks() -> list[STask]:
    tasks = await TaskRepository.get_all_tasks()
    return tasks


@router.get(path='/subtasks', tags=['Subtasks'])
async def get_all_subtasks_by_task_id(
        task_id: int
) -> list[SSubtask]:
    subtasks = await TaskRepository.get_all_subtasks_by_task_id(task_id)
    return subtasks
