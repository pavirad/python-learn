def DigitCount(k, n):
    digits = []
    count = 0
    while(count<=k):
        tmp = count
        while( tmp > 0):
            mod_count = tmp%10
            digits.append(mod_count)
            tmp = int(tmp/10)
        count+=1
    if n ==0:
        return(digits.count(n)) + 1
    else:
        return(digits.count(n))

print(DigitCount(19 ,0))
