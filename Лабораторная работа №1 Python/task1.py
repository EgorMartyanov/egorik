numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим


pyst_element = 4
kol = len(numbers)
suma = sum(numbers[:pyst_element]) + sum(numbers[(pyst_element+1):])
sr = suma / kol
numbers[4] = sr
print("Измененный список:", numbers)

