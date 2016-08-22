Limit = 4000000
PrevNum=1
CurrNum=2
Sum=CurrNum

def NextTerm(PrevNum,CurrNum):
    return CurrNum,PrevNum+CurrNum

def IsEven(Value):
    return False if Value%2 else True

while Sum<=Limit:
    PrevNum,CurrNum = NextTerm(PrevNum,CurrNum)
    Sum += CurrNum if IsEven(CurrNum) else 0

print(Sum)