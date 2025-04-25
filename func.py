numbers = [number for number in range(50)]
print(numbers)
yield_numbers = list((number for number in range(50)))
print(yield_numbers)