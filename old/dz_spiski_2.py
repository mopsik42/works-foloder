import random

a = [random.randint(1,100) for i in range(0,5)]

min_num = min(a)
max_num = max(a)

print(f"Минимальное число из списка '{a}' - {min_num} ")
print(f"Максимальное число из списка '{a}' - {max_num} ")


