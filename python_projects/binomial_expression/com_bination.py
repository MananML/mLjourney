
def user_input():
    print("ⁿCᵣ")
    while True:
        n = input("Input the value of n: ")
        r = input("input the value of r: ")
        
        if n.isdigit() and r.isdigit():
            return int(n), int(r)
        else:
            print("Please input a digit.") 

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

def main():
    n, r = user_input()
    print(combination(n, r))


main()