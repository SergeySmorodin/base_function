# n!=1⋅2⋅3⋅...⋅n

# форула нахождения факториала
# n! = 1 если n = 0
# n! = n * (n - 1)


# через рекурсию
n = int(input())

def fact_rec(f):
    if f == 0: return 1
    else: return f * fact_rec(f-1)
        
print(fact_rec(n))

# решение 2
def factorial(n):
    p = 1
    for i in range(2, n+1):
        p *= i

    print("my factorial")
    return p
