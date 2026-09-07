class Solution:
    def scoreOfString(self, s: str) -> int:
        values = []
        sum = 0
        for char in s:
            values.append(ord(char))
        for value in range(len(values) - 1):
            sum += abs(values[value] - values[value + 1])
        return sum
        