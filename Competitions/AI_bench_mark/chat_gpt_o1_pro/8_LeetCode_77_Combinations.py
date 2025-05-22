class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start, current_combination):
            # If the current combination has k elements, add it to the result
            if len(current_combination) == k:
                result.append(list(current_combination))
                return

            # Try all possible numbers from 'start' to 'n'
            for i in range(start, n + 1):
                current_combination.append(i)  # Include i in the current combination
                backtrack(i + 1, current_combination)  # Recur for the next numbers
                current_combination.pop()  # Backtrack, remove the last added element

        backtrack(1, [])  # Start with number templates1.ipynb and an empty combination
        return result
