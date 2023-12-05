import FoodOrderFSA as fo

def createItemListFSA():
    foodList = []
    numItems = int(input("How many items will you order today? "))
    if numItems < 1:
        print("Number of items must be at least 1.")
        return createItemListFSA()
    for i in range(1, numItems + 1):
        foodName = input(f"Item #{i}-\nEnter food: ")
        amount = float(input(f"Enter amount of pounds: "))
        if amount <= 0:
            print("Amount of pounds must be greater than 0.")
            continue
        FoodOrder = fo.FoodOrder(foodName, amount)
        FoodOrder.priceListFSA()
        FoodOrder.calculateCostFSA()
        foodList.append(FoodOrder)
    return foodList

def displayListFSA(foodList):
    for foodItem in foodList:
        print(foodItem)

def calculateTotalCostFSA(foodList):
    totalCost = 0
    for foodItem in foodList:
        totalCost += foodItem.calculatedPrice
    return totalCost

def main():
    foodList = createItemListFSA()
    displayListFSA(foodList)
    totalCost = calculateTotalCostFSA(foodList)
    print(f"Total cost: ${totalCost:.2f}")

main()