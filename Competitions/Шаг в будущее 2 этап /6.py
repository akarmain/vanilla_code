def read_block():
    return [list(map(int, input().split())) for _ in range(3)]

def is_solid(row):
    return all(cell == 1 for cell in row)

def can_place_above(lower, upper):
    # Проверяем совместимость: верхняя грань lower и нижняя грань upper должны дополнять друг друга
    for j in range(3):
        if upper[2][j] == 0 and lower[0][j] != 1:
            return False
        if upper[2][j] == 1 and lower[0][j] != 0:
            return False
    return True

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end and len(path) == N:  # Проверяем, что путь включает все блоки
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path:
                return new_path
    return None

# Считываем входные данные
N = int(input())
blocks = [read_block() for _ in range(N)]

# Находим основание и вершину
base = None
top = None
for idx, block in enumerate(blocks):
    if is_solid(block[2]):  # Нижняя грань сплошная
        base = idx
    if is_solid(block[0]):  # Верхняя грань сплошная
        top = idx

# Строим граф совместимости
graph = {i: [] for i in range(N)}
for i in range(N):
    for j in range(N):
        if i != j and can_place_above(blocks[i], blocks[j]):
            graph[i].append(j)

# Находим путь от основания до вершины
path = find_path(graph, base, top)
if path:
    # Преобразуем индексы (0-based) в номера блоков (templates1.ipynb-based)
    print(' '.join(str(idx + 1) for idx in path))
else:
    print("No solution found")