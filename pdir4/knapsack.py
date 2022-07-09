def knapsack(m, items):
    ratios = []
    tprofit = 0
    tweight = 0
    for i in items:
        ratios.append(i[1] / i[0])
    while tweight <= m and ratios != []:
        indx = ratios.index(max(ratios))
        if m - tweight < items[indx][0]:
            # w = items[indx][1]/items[indx][0]*(m-tweight)
            w = (items[indx][1] * (m - tweight)) / items[indx][0]
            tweight = tweight + m - tweight
            tprofit = tprofit + w
            ratios.remove(max(ratios))
            items.pop(indx)
        else:
            tweight = tweight + items[indx][0]
            tprofit = tprofit + items[indx][1]
            ratios.remove(max(ratios))
            items.pop(indx)
    return [tweight, tprofit]


m = 100
items = [[10, 20], [20, 30], [30, 66], [40, 40], [50, 60]]
print(knapsack(m, items))

m = 50
items = [[20, 60], [50, 100], [30, 120]]
print(knapsack(m, items))

m = 10
items = [[30, 500]]
print(knapsack(m, items))