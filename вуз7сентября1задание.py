# Напишите программу, определяющую число десятков и единиц в двузначном числе.
num = int(input())
last_digit = num % 10
first_digit = num // 10
print("Число десятков:", first_digit, "Число единиц:", last_digit)
