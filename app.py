def calculate_total(prices, tax_rate):
    total = sum(prices)
    return total + (total * tax_rate)


if __name__ == "__main__":
    items = [10, 25, 50]
    tax = 0.08

    result = calculate_total(items, tax)

    print("Total price:", result)
