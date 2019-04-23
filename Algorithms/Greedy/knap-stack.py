def knap_stack(weights, prices, capacity):

    ratio = [price/weight for price/weight in zip(prices, weights)]
    
    max_weight = prices[0]/weights[0]
    registered_index = 0
    bag = 0
    total_price = 0
    while bag < capacity:
        for index, (weight, price) in enumerate(zip(weights,prices)):
            if price/weight > max_weight:
                max_weight = price/weight
                registered_index = index
        if 
        bag += weight[registered_index]
        total_price += prices[registered_index]
        weight.pop(registered_index)
        prices.pop(registered_index)


def main():
    x = [1,2,3]
    y=[10,12,23]
    capacity = 90

    knap_stack(x,y,capacity)

main()