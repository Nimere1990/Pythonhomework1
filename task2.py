# 2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.
# Нужно написать таблицу истинности.

# x = int(input("Введите x: \n"))
# y = int(input("Введите y: \n"))
# z = int(input("Введите z: \n"))

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or y or z) == (not x and not y and not z):
                print(f'Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно при x = {x}, y={y}, z={z}')