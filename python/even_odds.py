# see: https://codeforces.com/problemset/problem/318/A

def even_odds(number, k):
    odds = []
    evens = []

    for value in range(1, number + 1):
        odds.append(value) if value % 2 == 0 else evens.append(value)

    result = evens + odds
    
    return result[ k - 1 ]
