def main():
    n, k, p = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    total_c = sum(c)
    left = 0
    right = total_c
    while left < right:
        m = (left + right) // 2
        if m + m // k >= total_c:
            right = m
        else:
            left = m + 1
    m = left
    free_items = total_c - m
    items_for_free = []
    items_to_pay = []
    for price, quantity in zip(a, c):
        if price <= p:
            items_for_free.append((price, quantity))
        else:
            items_to_pay.append((price, quantity))
    # Сортируем товары для бесплатного получения по убыванию цены
    items_for_free.sort(reverse=True)
    items_to_pay.extend([(price, quantity) for price, quantity in zip(a, c) if price <= p])
    items_to_pay.sort()
    free_items_selected = []
    remaining_free_items = free_items
    for price, quantity in items_for_free:
        take = min(quantity, remaining_free_items)
        free_items_selected.append((price, take))
        remaining_free_items -= take
        if remaining_free_items == 0:
            break
    paid_items = []
    for price, quantity in items_to_pay:
        free_quantity = 0
        for fp, fq in free_items_selected:
            if fp == price:
                free_quantity = fq
                break
        remaining_quantity = quantity - free_quantity
        if remaining_quantity > 0:
            paid_items.append((price, remaining_quantity))
    total_paid_items = 0
    total_cost = 0
    for price, quantity in paid_items:
        if total_paid_items >= m:
            break
        take = min(quantity, m - total_paid_items)
        total_cost += price * take
        total_paid_items += take
    print(total_cost)


if __name__ == "__main__":
    main()
