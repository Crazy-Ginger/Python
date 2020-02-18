def basket_price(basket, stock, prices):
    total = 0
    for key, val in basket.items():
        if key not in stock or val > stock[key]:
            print ("Not enough", key, "in stock")
            return None
        total += val * prices[key]
    return total


def checkout(basket, stock, prices):
    total = 0
    tmp_stock = stock
    for key, val in basket.items():
        if key not in stock or val > stock[key]:
            print ("Not enough", key, "in stock")
            return -1
        tmp_stock[key] -= val
        total += val * prices[key]
    stock = tmp_stock
    return total


def add_stock(items, stock):
    for key, val in items.items():
        if key in stock:
            stock[key] += val
        else:
            stock[key] = val
    stock = stock

    
####Main code block####
stock = {
 "banana": 6,
 "apple": 0,
 "orange": 32,
 "pear": 15
}
prices = {
 "banana": 40,
 "apple": 20,
 "orange": 15,
 "pear": 30
}
basket_1 = {
 "banana": 4,
 "pear": 3
}
basket_2 = {
 "apple": 1,
 "pear": 3
 }
