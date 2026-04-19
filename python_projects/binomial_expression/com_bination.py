
from perm_utation import permutation, factorial
def user_input():
    print("ⁿCᵣ")
    while True:
        n = input("Input the value of n: ")
        r = input("input the value of r: ")
        
        if n.isdigit() and r.isdigit():
            return int(n), int(r)
        else:
            print("Please input a digit.") 

def combination(n, r):
    r_fact = factorial(r)
    
    return int(permutation(n, r)/r_fact)

def main():
    n, r = user_input()
    print(combination(n, r))

if __name__ == "__main__":
    main()