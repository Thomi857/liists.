n = 10
m = 3
class Solution:
    def differenceOfSums(self, n: int, m: int):
        num_1 = sum(i for i in range(1, n + 1) if i % m != 0)
        num_2 = sum(i for i in range(1, n + 1) if i % m == 0)
        return num_1 - num_2