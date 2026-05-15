from dataclasses import dataclass
from typing import Self

@dataclass(order=True)
class Task:
    next_available_use: int
    remaining_frequency: int
    letter: str

    @classmethod
    def next_from_popped_task(cls, popped_task: Self, cooldown: int) -> Self | None:
        if popped_task.remaining_frequency == -1:
            return None
        return cls(
            popped_task.next_available_use + cooldown,
            popped_task.remaining_frequency + 1,
            popped_task.letter,
        )

class TaskScheduler:
    def __init__(self):
        self.min_heap_scheduler: List[Task] = []

    def __len__(self):
        return len(self.min_heap_scheduler)

    def push_task(self, task: Task) -> None:
        heapq.heappush(self.min_heap_scheduler, task)

    def peak(self) -> Task:
        return self.min_heap_scheduler[0]

    def pop_task(self) -> Task:
        return heapq.heappop(self.min_heap_scheduler)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        scheduler = TaskScheduler()
        counts = collections.Counter(tasks)
        for k, v in counts.items():
            scheduler.push_task(Task(
                0,
                -v,
                k
            ))
        cycle = 0
        while len(scheduler) > 0:
            cycle += 1
            if scheduler.peak().next_available_use >= cycle:
                continue
            task = scheduler.pop_task()
            next_task = Task.next_from_popped_task(task, n + 1)
            if next_task is not None:
                scheduler.push_task(next_task)
        return cycle