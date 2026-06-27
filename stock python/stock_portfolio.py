# Stock Portfolio Tracker

# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330
}

total = 0

print("===== Stock Portfolio Tracker =====")
print("Available Stocks:")

for stock in stock_prices:
    print(stock, "-", "$", stock_prices[stock])

num = int(input("\nHow many different stocks do you own? "))

for i in range(num):
    stock = input("Enter Stock Name: ").upper()
    quantity = int(input("Enter Quantity: "))

    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        total += investment
        print("Investment in", stock, "=", investment)
    else:
        print("Stock not available!")

print("\nTotal Investment = $", total)

# Save result in a text file
file = open("portfolio.txt", "w")
file.write("Total Investment = $" + str(total))
file.close()

print("Result saved successfully in portfolio.txt")