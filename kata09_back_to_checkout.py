#Implementation of kata09 http://codekata.com/kata/kata09-back-to-the-checkout/
class Price:
    def __init__(self, itemName, unitPrice, discountFactor, discountPrice):
        self.itemName = itemName
        self.unitPrice = unitPrice
        self.discountFactor = discountFactor
        self.discountPrice = discountPrice

class Checkout:
    global rules
    rules = {}
    rules['A'] = Price('A', 50, 3, 130)
    rules['B'] = Price('B', 30, 2, 45)
    rules['C'] = Price('C', 20, 0, 0)
    rules['D'] = Price('D', 15, 0, 0)

    def calculateTotal(goods):
        total = 0
        def sortGoods(items):
            goods = {}
            for i in range(0, len(items)):
                item = items[i]
                goods[item] = goods.get(item, 0) + 1
            return goods

        goods = sortGoods(goods)

        for k,v in goods.items():
            price = rules[k]
            amount = 0
            if price.discountFactor != 0:
                remainder = v % price.discountFactor
                quotient = v // price.discountFactor
                amount = (quotient * price.discountPrice) + (remainder * price.unitPrice)
            else:
                amount = v * price.unitPrice

            total += amount
        return total
