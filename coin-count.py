import sys

def testcases():
    print ("How many test cases?")
    x = int(sys.stdin.readline())
    return x

def getc():
    print ("How much coins in cents?")
    amt = int(sys.stdin.readline())
    return amt

cases = testcases();
amount = getc()
coins = [50, 20, 10, 5, 1]

print ("You entered x amount of cases, x= " + str(cases))
print ("You entered an amount of " + str(amount))
print (coins)
