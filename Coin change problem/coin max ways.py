def coin_change(coins,target):
    dp=[0]*(target+1)
    dp[0]=1
    for coin in coins:
        for current_amount in range(coin , target+1):
            dp[current_amount]=dp[current_amount]+dp[current_amount - coin]
    return dp[target]
#coins=[1,2,5]
#target =5
n= int(input("Enter the number of coins: "))
coins=[]
for i in range(n):
    coin=int(input(f"Enter the coin{i+1}: "))
    coins.append(coin)
target=int(input("Enter the target amount: "))
result=coin_change(coins,target)
print("Maximum ways are: ",result)