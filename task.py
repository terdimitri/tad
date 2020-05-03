"""a task object"""
import datetime

def bind(val, func):
    """Apply func to val only if val is not None"""
    if val is None:
        return val
    return func(val)


class Task:
    """A node of the hierarchal task structure, representing a task. Contains a
    name, description, time to complete the given task (excluding any subtasks),
    due date of the given task, and any subtasks that must be completed for the
    task itself to be.
    """
    def __init__(self, name, description,
                 completion_time: datetime.timedelta = None,
                 due_date: datetime.datetime = None):
        self.name = name
        self.description = description
        self.completion_time = completion_time
        self.due_date = due_date
        self.complete = False
        self.subtasks = []

    def __repr__(self):
        return f'''Task(
        name={self.name},
        description={self.description},
        completion_time={self.completion_time},
        due_date={self.due_date}
    )'''

    def add_task(self, task: Task):
        self.subtasks.append(task)

    def add_tasks(self, tasks: [Task]):
        self.subtasks.extend(tasks)

    def total_time(self):
        """Accumulate the total completion time of the task with all subtasks"""
        total_time = self.completion_time

        for task in self.subtasks:
            try:
                subtime = task.total_time()
                total_time += subtime
            except TypeError:
                if isinstance(subtime, datetime.timedelta):
                    total_time = subtime

    def simple(self):
        """Return a dictionary representing the same information as the Task
        object, but only containing json compatible objects.
        """
        return {
            'name': self.name,
            'description': self.description,
            'complete': self.complete,
            'completion_time': bind(self.completion_time, datetime.timedelta.total_seconds),
            'due_date': bind(self.due_date, datetime.datetime.isoformat),
            'subtasks': [task.simple() for task in self.subtasks]
            }
