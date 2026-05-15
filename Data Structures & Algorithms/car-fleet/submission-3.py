class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        -------------------------------------------------------------------|---------
        C   C             C                C               C  C            |target
        -------------------------------------------------------------------|---------


        1. Sort the position such that we can process the list by closest car to target.
                We need this so we can keep track of bottlenecks
        2. While processing:
                take our current bottleneck candidate and compute time it takes for them to reach target
                for cars immediately behind bottleneck, see if they will run into bottleneck
                    if yes:
                        add them to the fleet
                    if no:
                        this car / bottleneck is the head of a new fleet of 1+ cars. Repeat processing loop
        """
        positions_and_speeds = [(position, speed) for position, speed in zip(position, speed)]
        positions_and_speeds.sort(key=lambda x: x[0], reverse=True)
        # The front of the line is the current bottleneck
        current_bottleneck = 0
        total_fleets = 1
        bottlenecked_time_to_arrival = (target - positions_and_speeds[0][0]) / positions_and_speeds[0][1]
        for car_position, car_speed in positions_and_speeds[1:]:
            time_to_arrival = (target - car_position) / car_speed
            # If our time to arrival is shorter than our bottleneck, then we will join the fleet
            if time_to_arrival <= bottlenecked_time_to_arrival:
                continue
            else:
                bottlenecked_time_to_arrival = time_to_arrival
                total_fleets += 1
        return total_fleets
        