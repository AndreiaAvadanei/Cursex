#Method that verify if a string is palindrom(se citeste la fel 131 -131)
# aba = True
#abcba = True
#abc = False
#
def is_palindrom(x):
    list_of_chr = []
    invers_list = []
    for chr in x:
        list_of_chr.append(chr)
    #print(len(list_of_chr))

    print("===================")

    for i in range(len(list_of_chr)-1,-1,-1):
       # print(i)
       # print(list_of_chr[1])
        invers_list.append(list_of_chr[i])
    return True if list_of_chr == invers_list else False

print(is_palindrom('abc'))
print(is_palindrom('aba'))
print(is_palindrom('abcba'))

def is_palindrom_short(x):
    return True if x[::-1] else False
print(is_palindrom('abcba'))
print(is_palindrom('aba'))
print(is_palindrom('abc'))