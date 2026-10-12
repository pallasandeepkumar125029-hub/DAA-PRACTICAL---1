def minimum_coins(coins, amount):
	if amount < 0 or any(coin <= 0 for coin in coins):
		raise ValueError("Coins and amount must be positive, and amount cannot be negative")

	minimum = [amount + 1] * (amount + 1)
	last_coin = [-1] * (amount + 1)
	minimum[0] = 0

	for current_amount in range(1, amount + 1):
		for coin in coins:
			if coin <= current_amount and minimum[current_amount - coin] + 1 < minimum[current_amount]:
				minimum[current_amount] = minimum[current_amount - coin] + 1
				last_coin[current_amount] = coin

	if minimum[amount] == amount + 1:
		return None, []

	combination = []
	current_amount = amount
	while current_amount > 0:
		coin = last_coin[current_amount]
		combination.append(coin)
		current_amount -= coin

	return minimum[amount], combination


coins = [int(value) for value in input("Enter coin denominations separated by spaces: ").split()]
amount = int(input("Enter the amount: "))
coin_count, combination = minimum_coins(coins, amount)

if coin_count is None:
	print("The amount cannot be formed with the given coins.")
else:
	print(f"Minimum number of coins: {coin_count}")
	print(f"Coins used: {combination}")
