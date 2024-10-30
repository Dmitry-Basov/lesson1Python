# найдите сумму чисел трехзначного числа
# 123 => 6(1+2+3)

number = int(input(' Введите число: '))
sum = 0

while number != 0:
    sum += number % 10
    number //= 10

print(sum)
    
