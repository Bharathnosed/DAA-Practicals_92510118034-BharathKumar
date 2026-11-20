n = int(input("Enter number of items: "))
W = int(input("Enter capacity: "))

wt = []
val = []

for i in range(n):
    wt.append(int(input("Enter weight: ")))
    val.append(int(input("Enter value: ")))

dp = [[0] * (W + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, W + 1):

        if wt[i - 1] <= w:
            take = val[i - 1] + dp[i - 1][w - wt[i - 1]]
            skip = dp[i - 1][w]

            dp[i][w] = max(take, skip)

        else:
            dp[i][w] = dp[i - 1][w]

print("Maximum value:", dp[n][W])