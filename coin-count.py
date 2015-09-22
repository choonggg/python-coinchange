import sys

def testcases():
    print ("How many test cases?")
    x = int(sys.stdin.readline())
    return x

def getc(i):
    print ("Amount in cent? Case-No#: %d" % (i + 1) )
    amt = int(sys.stdin.readline())
    return amt

def getNumOfWays(num, coins):

    return num

def main():
    cases = testcases();
    # coins = [50, 20, 10, 5, 1]
    coins = [3,2,1]
    caseNum = []

    for i in range(0, cases):
        caseNum.append(getc(i))
    for x in range(len(caseNum)):
        num = caseNum[x]
        print ("Case #%d: %d" % ( x + 1 , getNumOfWays(num, coins)) )

main()
# for case in caseNum :

# print ("You entered x amount of cases, x= " + str(cases))
# print(caseNum)
