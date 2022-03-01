
name = input('Podaj imię: ')
wiek = int(input('ile masz lat? '))

if wiek >= 18:
    print(name + ' jesteś pełnoletni!')
else:
    print(' Jesteś jeszcze za młody')

# for z pominięciem parzystych
lista = [1, 2, 2, 3, 4, 55, 6]
lista2 = []
for x in lista:
    if x % 2 == 0:
        continue
    else:
        print(x)

# While
x = 0
while x <= 5:
    print(x)
    x = x+1

# RANGE
number = 0

for number in range(4):
    if number == 5:
        pass    # pass here

    print('Number is ' + str(number))

print('Out of loop')

# Continue
i = 0
while i<5:
  i += 1
  if i==3:
    print("Skipping 3")
    continue
  print(i)

  # listowanie listy
  words = ["hello", "world", "spam", "eggs"]
  for word in words:
      print(word + "!")