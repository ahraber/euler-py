factors = []

def factor_calc(n1, n2, limit): 

    for i in range(n1,limit):
        if (( i%n1 == 0 ) or ( i%n2 == 0 )) and ( i < limit ) and ( i not in factors ): 
            factors.append(i)

    print(sum(factors))

def main():

    n1 = 3
    n2 = 5
    limit = 1000
    factor_calc(n1, n2, limit)

main()
