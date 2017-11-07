class PricingRule:
    def __init__(self,unitprice,itemname):
        self.unitprice = unitprice
        self.itemName  = itemname
    def offer_A(self,no_of_item,price_of_one_item):
        if no_of_item>=3:
            price=1.30
        else:
            price=no_of_item*price_of_one_item
        return price
    def offer_B(self,no_of_item,price_of_one_item):
        if no_of_item>=2:
            price=0.90
        else:
            price=no_of_item*price_of_one_item
        return price
    
