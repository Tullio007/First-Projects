import math as m
num = int(input('Write your respective number to see his binare: '))
numint = m.floor(num)
bina = ''
while num > 0:
    resto = num % 2
    bina += str(resto)
    num //= 2
print(f'The binarie of the number {numint} is...{bina[::-1]}')
