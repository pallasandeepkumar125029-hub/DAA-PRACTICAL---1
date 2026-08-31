def factorial(number):
	if number < 0:
		raise ValueError("Factorial is not defined for negative numbers")
	if number == 0 or number == 1:
		return 1
	return number * factorial(number - 1)


number = int(input("Enter a non-negative integer: "))
print(f"Factorial of {number} is {factorial(number)}")
