num = int(input('Введите номер вашего билета: '))

n1 = num // 100000
n2 = num // 10000 
n2 %= 10
n3 = num // 1000
n3 %= 10
n4 = num // 100
n4 %= 10
n5 = num // 10
n5 %= 10
n6 = num % 10

if n1+n2+n3 == n4+n5+n6:
    print('билет счастливый')
else:
    print('билет не счастливый')

