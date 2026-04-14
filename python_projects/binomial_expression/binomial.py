

def user_input():
    while True:
        power = input("Input the power of the binomial expression: ")
        if power.isdigit:
            int(power)
        else:
            print("Please enter a digit.")
        
        return power

def factorial(num):
    i = 1
    lst_num = [num]

    while i != num:
        lst_num.append(num - i)
        i += 1
    result = 1
    for _ in lst_num:
        result *= _
    
    return result

def combination(n, r):
    n_fact = factorial(n)
    r_fact = factorial(r)
    nr_fact = factorial(n-r)
    
    return int((n_fact)/(nr_fact * r_fact))


def calculate(n):
    i = 1
    coefficients = [1]

    while i != n:
        coefficients.append(combination(n, i))
        i += 1
    
    coefficients.append(1)
    return coefficients


def equation(ⁿ): #stil working on print the equation to the screen
    ...

def pascal(): # still working on printing pascal traingle of the binomial expression 
    ...

def main():
    power = user_input()  
    power = int(power)

    print(*calculate(power)) 

main()