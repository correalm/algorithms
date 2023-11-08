# see: https://codeforces.com/problemset/problem/479/A

def expression(*argv):
    def maxProductOfSum(*argv):
        values = argv[ 0 ]

        firstValue, secondValue, thirdValue = values

        firstResult = (firstValue + secondValue) * thirdValue
        secondResult = (secondValue + thirdValue) * firstValue

        return max(firstResult, secondResult)

    product = 1
    sum = 0
    productOfSum = maxProductOfSum(argv)

    for value in argv:
        product = value * product
        sum = value + sum

    return max(product, sum, productOfSum)

        