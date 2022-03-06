"""
Recursivitatea este capacitatea functiilor de a se auto-apela (self-call)

def functie_recursiva(parametru):
    return functie_recursiva(parametru)


5! = 5 * 4 * 3 * 2 * 1

0! = 1
1! = 1
"""

def factorial(number):

    if number < 2:
        return 1
    else:
        return number * factorial(number - 1)

"""

2. 3
return ( 3 * ( 2 * ( 1 )))

return 5 * factorial(4) -> factorial(3) ->
"""

print(factorial(5))