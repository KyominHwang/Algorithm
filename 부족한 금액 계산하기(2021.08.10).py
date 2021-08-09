def solution(price, money, count):
    sumVal = 0
    for i in range(1, count + 1):
        sumVal += price * i

    return sumVal - money if sumVal - money > 0 else 0