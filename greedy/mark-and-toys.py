# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_toys(prices, rupees):
    #Compute and return final answer over here
    prices.sort()
    answer = 0
    sum_ = 0
    for price in prices:
        if price + sum_ < rupees:
            sum_ = price + sum_
            answer += 1
        else:
            break
            
    return answer

if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    prices = map(int, raw_input().split())
    print max_toys(prices, k)

