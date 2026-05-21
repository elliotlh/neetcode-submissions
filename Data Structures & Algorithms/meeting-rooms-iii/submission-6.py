class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        """
        General strategy
        1. We will keep a heap of active meetings by their end time
        2. We will keep a heap of available rooms (also min heap)
        3. We will sort the meeting list by their unique start time
                and process each meeting independently
        
        Process Logic
            Clear out available rooms first
            If no available rooms:
                simulate delay
            else:
                assign to earliest available room
        """
        meetings.sort()
        available_rooms = []
        for i in range(n):
            heapq.heappush(available_rooms, i)
        active_meetings = []
        meeting_freq = collections.defaultdict(int)
        for start_time, end_time in meetings:
            # Clear out meetings that ended before this meeting started
            while active_meetings and active_meetings[0][0] < start_time:
                _, room = heapq.heappop(active_meetings)
                heapq.heappush(available_rooms, room)
            # if there is a room available, lets use it
            if available_rooms:
                consumed_room = heapq.heappop(available_rooms)
                meeting_freq[consumed_room] += 1
                # print('assinging', start_time, 'to', consumed_room, 'for end', end_time)
                heapq.heappush(active_meetings, (end_time, consumed_room))
                continue
            # Otherwise we need to process the delay by fast-forwarding to the next available start time
            next_available_start_time, room = heapq.heappop(active_meetings)
            heapq.heappush(available_rooms, room)
            # Now we are guaranteed to be at the correct point in time and have an available room
            consumed_room = heapq.heappop(available_rooms)
            meeting_freq[consumed_room] += 1
            # print('assinging', start_time, 'to', consumed_room, 'for end', next_available_start_time + (end_time - start_time))
            heapq.heappush(active_meetings, (next_available_start_time + (end_time - start_time), consumed_room))
        return max(meeting_freq, key=meeting_freq.get)