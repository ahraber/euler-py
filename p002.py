fib_e = []

def fib_calc(): 

    a,b = 0,1

    while ( a < 4000000): 
        a,b = b, a+b 
        if ( a%2 == 0 ):
            fib_e.append(a)

    print(sum(fib_e))

def main():

    fib_calc()

main()
