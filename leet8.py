arr = [3579]
def threeConsecutiveOdds(self, arr):
    for i in arr:
        odd = (i % 2 != 0)
        if odd == True:
            return True
        else:
            return False
print(threeConsecutiveOdds(None,arr))