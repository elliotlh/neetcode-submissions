class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        We need a few things:
        1. We need the ability to instantly pick the smallest processing time and smallest index of "available" events
        2. We need a way to keep track of relative time
        3. We need to make sure that our step 1 only contains events that are available for enqueue


        Approach 1:
        -----------
        We could sort all of the tasks by their enqueue time, secondary sorrt by processing time and index
        We take the first task and use that to baseline our time
        After we process the task, we
        """
        # 1. Get our sorted tasks
        wrapped = []
        for i, task in enumerate(tasks):
            wrapped.append((task[0], task[1], i))
        wrapped.sort(key=lambda x: (x[0], x[1], x[2]))
        # 2. Simulate task processing
        task_list = [wrapped[0][1:]]
        task_idx = 1
        t = wrapped[0][0]
        result = []
        # Run the simulation until time is handled
        while task_list:
            task = heapq.heappop(task_list)
            result.append(task[1])
            available_enqueue_time = t + task[0]
            # CPU will be idle, we need to fast forward to our next unprocessed task
            if task_idx < len(wrapped) and wrapped[task_idx][0] > available_enqueue_time:
                t = wrapped[task_idx][0]
                available_enqueue_time = t
            else:
                # Otherwise we can keep t as the available enqueue time
                t = available_enqueue_time
            # Now we can add all items to the heap and process them
            while task_idx < len(wrapped) and wrapped[task_idx][0] <= available_enqueue_time:
                heapq.heappush(task_list, wrapped[task_idx][1:])
                task_idx += 1

        return result