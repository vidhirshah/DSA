mod = int(1e9 + 7)

def findWays(num, tar):
    n = len(num)
    dp = [[0 for i in range(tar + 1)] for j in range(n)]

    if num[0] == 0:
        dp[0][0] = 2  # 2 cases - pick and not pick
    else:
        dp[0][0] = 1  # 1 case - not pick

    if num[0] != 0 and num[0] <= tar:
        dp[0][num[0]] = 1  # 1 case - pick
    for i in dp:
        print((i))
    for ind in range(1, n):
        for target in range(tar + 1):
            notTaken = dp[ind - 1][target]

            taken = 0
            if num[ind] <= target:
                taken = dp[ind - 1][target - num[ind]]

            dp[ind][target] = (notTaken + taken) % mod

    return dp[n - 1][tar]

def targetSum(n, target, arr):
    totSum = 0
    for i in range(n):
        totSum += arr[i]
    # Checking for edge cases
    if (totSum - target) < 0 or ((totSum - target) % 2):
        return 0
    print((totSum - target) // 2)

    return findWays(arr, (totSum - target) // 2)

def main():
    arr =  [0,0,0,0,0,0,0,0,1]
    target = 1
    n = len(arr)

    print("The number of ways found is", targetSum(n, target, arr))

if __name__ == "__main__":
    main()
