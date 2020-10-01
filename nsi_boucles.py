#1 bonjour 5 fois

for bonjour in range(5):
    print('bonjour')

for bonjour in range(5):
    print('bonjour', end=" ")


print("\n")


#2 nombre pairs

for nombres in range(10, 21, 2):
    print(nombres)

print("\n")


#3 multiplication de deux entiers sans *

c=0
a = int(input('Entrez un nombre :'))
b = int(input('Entrez un nombre :'))


for a in range(a):
    c += b

print(c)

#4 factorielle de n

n = int(input("Entrez la variable n"))