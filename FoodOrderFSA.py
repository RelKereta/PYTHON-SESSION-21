class FoodOrder:
    def __init__(self, food_name, amount):
        self.food_name = food_name
        self.amount = amount
        self.standardPrice = 0.0
        self.calculatedPrice = 0.0

    def priceListFSA(self):
        foodPrices = {
            "Dry Cured Iberian Ham": 177.80,
            "Wagyu Steaks": 450.00,
            "Matsutake Mushrooms": 272.00,
            "Kopi Luwak Coffee": 306.50,
            "Moose Cheese": 487.20,
            "White Truffles": 3600.00,
            "Blue Fin Tuna": 3603.00,
            "Le Bonnotte Potatoes": 270.81
        }
        self.standardPrice = foodPrices.get(self.food_name, 0.0)

    def calculateCostFSA(self):
        self.calculatedPrice = self.standardPrice * self.amount
        return self.calculatedPrice

    def __str__(self):
        return f"Item: {self.food_name}\nAmount ordered: {self.amount} pounds\nPrice per pound: ${self.standardPrice:.2f}\nPrice of order: ${self.calculatedPrice:.2f}\n"