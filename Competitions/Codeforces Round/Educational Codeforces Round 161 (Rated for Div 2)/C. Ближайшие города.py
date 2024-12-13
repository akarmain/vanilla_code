def main():
    results = []
    for x, y in queries:
        x -= 1
        y -= 1
        direct_cost = abs(cities[x] - cities[y])

        # Стоимость перемещения через ближайшие города
        via_nearest_cost = min_distances[x][y]

        # Выбираем минимальную стоимость
        results.append(min(direct_cost, via_nearest_cost))

    return results

    # Тестовые запросы


queries = [(1, 4), (1, 5), (3, 4), (3, 2), (5, 1)]
results = min_coins_for_travel(min_distances, queries, cities)
results
