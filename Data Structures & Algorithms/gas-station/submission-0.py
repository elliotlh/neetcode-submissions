class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        [1,2,3,4]
        [2,2,4,1]
        """
        amount_in_tank = 0
        n = len(gas)
        for i in range(n):
            amount_in_tank = gas[i]
            success = True
            for j in range(n):
                cost_to_leave = cost[(i + j) % n]
                if amount_in_tank < cost_to_leave:
                    success = False
                    break
                else:
                    amount_in_tank -= cost_to_leave
                amount_in_tank += gas[(i + j + 1) % n]
            if success:
                return i
        return -1
                


                

