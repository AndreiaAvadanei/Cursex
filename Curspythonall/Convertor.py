'''
121 / 2 = 60 rest 0.5 ----> 1
60 / 2 = 30 rest ---------> 0
30 / 2 = 15 rest ---------> 0
15 / 2 = 7 rest 0.5 ------> 1
7 / 2 = 3 rest 0.5 -------> 1
3 / 2 = 1 rest 0.5 -------> 1
1 / 2 = 0 rest 0.5 -------> 1
'''

def dec2bin(num):
    # facem o lsita goala in care bagam rand pe rand resturile impartitilor la 2
    lista = []
    while num > 0:
        # cat timp numarul este mai mare sau egal cu 1, il prelucram

        # bagam aici in lsita restul impartirii numarului initial la 2
        rest = num % 2
        print(f"Restul impartirii lui: {num} % 2 este: -------> {rest}")
        lista.append(rest)
        # apoi aici impartim numarul la 2, pt ca atunci cand convertim in baza 2, trebuie sa tot impartim la 2
        num = num // 2
        print(f"Rezultatul impartirii: {num}")

        # apoi afisam lista invers
    print(lista[::-1])


print(dec2bin(121))


'''Exercitiul 2'''
'''
Binary to Decimal:
Numar: 01001011

[6][5][4][3][2][1][0]
 1  0  0  1  0  1  1

(2 ** 7) * 0 +
(2 ** 6) * 1 +
(2 ** 5) * 0 +
(2 ** 4) * 0 +
(2 ** 3) * 1 +
(2 ** 2) * 0 +
(2 ** 1) * 1 +
(2 ** 0) * 1 +
dec

(base ** power) * bit

Selectam doar valaorile cu "1"
(2 ** 6) * 1 + (2 ** 3) * 1 + (2 ** 1) * 1 + (2 ** 0) * 1

64 + 8 + 2 + 1 = 75

'''
def bin2dec(bin):
    dec = 0
    power = 0
    while bin > 0:
        #selectam ultimul element
        bit = bin % 10
        print("Ultimul element este:", bit)
        '''
        folosit pentru selectarea ultimului element:
        123 % 10 = 3
        187 % 10 = 7
        '''
        result = 2 ** power * bit
        print(f"(2 ** {power}) * {bit}")
        dec += result

        # aruncam ultimul element
        new_bin = bin // 10
        print("Noul numar dupa eliminarea ultimului element", new_bin)
        bin = new_bin

        power = power + 1
        print("Marim puterea cu fecare iteratie:", power)

    return dec

print(bin2dec(1001011))