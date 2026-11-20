def coin_change(coins,amount):
    dp=[float('inf')]*(amount+1)
    dp[0]=0

    for current_amount in range(1,amount+1):
        for coin in coins:
            if coin <= current_amount:
                dp[current_amount]=min(dp[current_amount],dp[current_amount - coin] + 1)
    if dp[amount] == float('inf'):
        return -1
    return dp[amount]
#coins=[1,2,5]
#amount = 11
n=int(input("Enter the number of coins: "))
coins=[]
for i in range(n):
    coin=int(input(f"enter coin{i+1}: "))
    coins.append(coin)
target=int(input("Enter the target amount: "))

result=coin_change(coins,target)
if result == -1:
    print("Amount cannot be formed")
else:
    print("Minimim coins are: ",result)
