accounts = [[2,8,7],[7,1,3],[1,9,5]]
def maximumWealth(self, accounts):
        max_wealth = 0
        for customer_wealth in accounts:
                j = sum(customer_wealth)
                if j > max_wealth:
                        max_wealth = j
        return max_wealth
        
print(maximumWealth(None,accounts))
