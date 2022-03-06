#Varianta 1: cu list comprehension
n = 8
l_nou = []
l_nou = [" " * (int(n * 2) - i) + '**' * i for i in range(n)]
for steluta in l_nou:
 print(steluta)

print('\n')



#Varianta 2: cu matrice
rows = 10
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
print('\n')



#Varianta 3
l = [ (" "* (n-i) + "*" * i * 2 + " " * (n-i)) for i in range(n) ]
for i in range(len(l)):
     print(l[i])