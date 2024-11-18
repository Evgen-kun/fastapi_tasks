from database import new_session, TasksOrm, SubtasksOrm
from sqlalchemy import select
from schemas import STaskAdd, STask, SSubtaskAdd, SSubtask


class TaskRepository:
    @classmethod
    async def add_task(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TasksOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id


    @classmethod
    async def add_subtask(cls, data: SSubtaskAdd) -> int:
        async with new_session() as session:
            subtask_dict = data.model_dump()

            subtask = SubtasksOrm(**subtask_dict)
            session.add(subtask)
            await session.flush()
            await session.commit()
            return subtask.id


    @classmethod
    async def get_all_tasks(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TasksOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(task_model) for task_model in task_models]
            return task_schemas

    @classmethod
    async def get_all_subtasks_by_task_id(cls, task_id: int) -> list[SSubtask]:
        async with new_session() as session:
            query = select(SubtasksOrm).where(SubtasksOrm.task_id == task_id)
            result = await session.execute(query)
            subtask_models = result.scalars().all()
            subtask_schemas = [SSubtask.model_validate(subtask_model) for subtask_model in subtask_models]
            return subtask_schemas