fibonacci = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

def fibonacci_grid(price, lines, total_amount=100):
    grid_price = [price]
    total_weight = sum(fibonacci[:lines])
    grid_weight = [fibonacci[i] / total_weight * 100 for i in range(lines)]
    grid_amount = [total_amount * grid_weight[i] / 100 for i in range(lines)]
    for i in range(1, lines):
        index = i - 1
        grid_price.append(grid_price[index] * (1 + fibonacci[index] * 0.01))

    grid_dict = dict(zip(grid_price, grid_amount))


    # return a dict of grid itself and the avg value of the grid
    return {
        'price_by_amount': grid_dict,
        'average_price': sum([grid_amount[i] * grid_price[i] for i in range(lines)])/total_amount,
        'percentage_change': round((grid_price[-1] - grid_price[0]) / grid_price[0] * 100, 2),
    }