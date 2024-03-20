def find_min_coins(sum, coins):
    # Ініціалізуємо масив для зберігання мінімальної кількості монет для кожної суми
    dp = [float('inf')] * (sum + 1)
    dp[0] = 0  # Базовий випадок
    
    # Словник для зберігання кількості кожної монети
    coin_count = {c: 0 for c in coins}
    
    # Попередник для кожної суми
    predecessor = [-1] * (sum + 1)
    
    # Обчислюємо мінімальну кількість монет для кожної суми
    for i in range(1, sum + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                predecessor[i] = coin
    
    # Відновлюємо монети
    current_sum = sum
    while current_sum > 0:
        coin = predecessor[current_sum]
        if coin == -1:  # Якщо монета не була знайдена, решту не можна видати
            return {}
        coin_count[coin] += 1
        current_sum -= coin
    
    # Видаляємо монети з кількістю 0
    return {coin: count for coin, count in coin_count.items() if count > 0}

coins = [1, 2, 10, 50]
sum = 113
print(find_min_coins(sum, coins))
