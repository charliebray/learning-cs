def max_profit(max_weight):
    collect = []
    art_dict = {2: 3, 3: 4, 4: 8, 5: 8, 9: 10}

    for weight in range(0, max_weight + 1):
        profit = 0
        for w in [w for w in art_dict if w <= weight]:
            new_value = collect[weight - w] + art_dict[w]
            if new_value > profit:
                profit = new_value
        collect.append(profit)

    return collect

def main():
    print(max_profit(20))

if __name__ == '__main__':
    main()
