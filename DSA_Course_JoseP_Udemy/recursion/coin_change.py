def coin_change(target, coins, known_results):
    min_coins = target
    if target in coins:
        known_results[target] = 1
        return 1
    elif known_results[target] > 0:
        return known_results[target]
    else:
        for i in [c for c in coins if c <= target]:   
            num_coins = 1 + coin_change(target - i, coins, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[target] = min_coins
    return min_coins


print(coin_change(63, [2, 5, 10, 25], [0]*64))
    
                