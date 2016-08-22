def IsMultiple(dividend, divisor):
    return False if(dividend%divisor) else True

NoOfIterations = 1000
sum=0

for num in range(0,NoOfIterations):
    if(IsMultiple(num,3) | IsMultiple(num,5)):
        sum+=num

print(sum)