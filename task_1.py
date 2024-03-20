def find_coins_greedy(total_sum, coins):
    coins_count = {}
    remaining_sum = total_sum

    # Сортуємо монети / спочатку найбільші номінали
    for coin in sorted(coins, reverse=True):
        if remaining_sum <= 0:
            break
        count, remaining_sum = divmod(remaining_sum, coin)
        if count > 0:
            coins_count[coin] = count

    return coins_count


if __name__ == '__main__':
    cases = [([50, 25, 10, 5, 2, 1], 133),
             ([10, 6, 1], 12)]
    
    for coins, cash_amount in cases:
        print(f"\nCase for {coins} and sum: {cash_amount}")
        result = find_coins_greedy(cash_amount, coins)
        print(f"Result: {result}")
