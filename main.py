
name = input('Podaj imię: ')
wiek = int(input('ile masz lat? '))

if wiek >= 18:
    print(name + ' jesteś pełnoletni!')
else:
    print('Jesteś jeszcze za młody')

# for z pominięciem parzystych
lista = [1,2,2,3,4,55,6,7,8,9]
lista2 = []
for x in lista:
    if x%2 ==0:
        continue
    else:
        print(x)
#Pętla while
x = 1
while x < 10:
    if x%2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")

    x += 1