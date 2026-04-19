
from com_bination import combination
def user_input():
    while True:
        power = input("Input the power of the binomial expression: ")
        if power.isdigit:
            int(power)
        else:
            print("Please enter a digit.")
        
        return power


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

if __name__ == main():
    main()