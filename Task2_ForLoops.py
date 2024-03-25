"""
cars=['Audi', 'VW', 'Jaguar', 'Mini']
for x in cars:
    print(x)

print("For loop complete")
"""

"""
list = [1, 2, 3, 4, 5, 6]
for x in list:
    print(x * 2)

print("For loop complete")
"""

numbers = [1, 2, 3, 4, 5, 6]
for x in numbers:
    print(x)
    if x == 5:
        print("Breaking condition met, existing loop")
        break

else:
    print("Number was not found")