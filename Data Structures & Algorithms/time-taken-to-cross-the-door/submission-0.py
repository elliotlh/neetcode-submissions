class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        """
        0,0,0,1,1,1,2,15 | 0,1,0,1,0,1...
        PrevSecondResult = 0, 1, None

        global timer starting at arrival[0]
        iterate over arrival and place everyone with time <= global t in their respective queue
        process both queues according to rule engine and update global timer
        each time i increment the global timer, add all people with that arrival time into the queue
        if pointer < len(arrival) and queues are empty, update global time and pointer to next in line
        --->.     <--
        2,1,1,0| |0,1,15
        """
        if not arrival:
            return []
        arrival_idx = 0
        global_time = arrival[arrival_idx]
        entering_queue = collections.deque()
        exiting_queue = collections.deque()
        prev_result = None
        processed = 0
        ans = [0] * len(arrival)
        while processed < len(arrival):
            # Add all elements that are <= global time to their queues
            # print('initial arrival idx', arrival_idx)
            while arrival_idx < len(arrival) and arrival[arrival_idx] <= global_time:
                if state[arrival_idx] == 0:
                    entering_queue.append(arrival_idx)
                else:
                    exiting_queue.append(arrival_idx)
                arrival_idx += 1
            # print('final arrival idx', arrival_idx)
            # print(entering_queue, exiting_queue, global_time, prev_result)
            # easy cases, there is no conflict
            if entering_queue and not exiting_queue:
                ans[entering_queue.popleft()] = global_time
                prev_result = 0
            elif exiting_queue and not entering_queue:
                ans[exiting_queue.popleft()] = global_time
                prev_result = 1
            # if there is conflict, lets apply the rules
            elif prev_result is None:
                prev_result = 1
                ans[exiting_queue.popleft()] = global_time
            elif prev_result == 0:
                ans[entering_queue.popleft()] = global_time
            elif prev_result == 1:
                ans[exiting_queue.popleft()] = global_time
            processed += 1
            # increment the global time
            global_time += 1
            # if our queues are empty, we need to fast forward
            if not entering_queue and not exiting_queue and arrival_idx < len(arrival):
                # if global time is still smaller than next arrival, we ignore our previous result
                if global_time < arrival[arrival_idx]:
                    prev_result = None
                global_time = max(global_time, arrival[arrival_idx])
        return ans

            
            
            
        
        