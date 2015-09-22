import sys

def testcases():
    print ("How many test cases?")
    x = int(sys.stdin.readline())
    return x

def getc(i):
    print ("Amount in cent? Case#: %d" % (i + 1) )
    amt = int(sys.stdin.readline())
    return amt

def getNumOfWays(num, coins):
    coins = sorted(coins, reverse=True)
    ways = [0] * (num + 1)
    ways[0] = 1
    for coin in coins:
        for j in range(coin, num + 1):
            ways[j] += ways[j - coin]

    return ways[num]

def main():
    cases = testcases();
    coins = [50, 20, 10, 5, 1]
    # coins = [3,2,1]
    caseNum = []

    for i in range(0, cases):
        caseNum.append(getc(i))
    for x in range(len(caseNum)):
        num = caseNum[x]
        print ("Case #{}: {}".format( x + 1 , getNumOfWays(num, coins)) )

main()
