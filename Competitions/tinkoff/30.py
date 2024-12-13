from collections import defaultdict

A, V, T = map(int, input().split())

purchases = defaultdict(list)

for _ in range(T):
    client_id, purchase_amount = map(int, input().split())
    purchases[client_id].append(purchase_amount)
total_spent = sum(sum(purchase) for purchase in purchases.values())

unique_buyers = len(purchases)

buyers_bought_twice_or_more = sum(1 for purchase in purchases.values() if len(purchase) >= 2)

total_purchases = sum(len(purchase) for purchase in purchases.values())

percentage_viewed = round(V / A * 100)
percentage_bought = round(unique_buyers / V * 100) if V else 0

print(f"{A} {V} {unique_buyers} {percentage_viewed}% {percentage_bought}% {total_spent} {buyers_bought_twice_or_more} {total_purchases}")