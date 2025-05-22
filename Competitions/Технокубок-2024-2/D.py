import sys
sys.setrecursionlimit(10**7)

def solve():
    N = int(input().strip())
    # Если N нечетно, сразу ответ 0, так как невозможно сбалансировать путь
    if N % 2 == 1:
        print(0)
        return

    # Для N=templates1.ipynb сразу известен результат
    if N == 1:
        print(0)
        return
    # Для N=2 результат известен
    if N == 2:
        print(2)
        return

    # Попытка общего решения через бэктрекинг для малых N (например, N<=6)
    # Если N очень большое, перебор будет работать очень долго.
    rows = 3
    cols = N
    total_cells = rows * cols

    grid = [(r, c) for r in range(rows) for c in range(cols)]

    # Вспомогательная структура для быстрого нахождения соседей
    # Соседями считаем клетки слева, справа, сверху, снизу
    moves = [(1,0), (-1,0), (0,1), (0,-1)]

    def neighbors(r, c):
        for dr, dc in moves:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols:
                yield nr, nc

    visited = [[False]*cols for _ in range(rows)]
    visited[0][0] = True

    result = 0

    def backtrack(r, c, count):
        nonlocal result
        # count - количество посещенных клеток (уже включающее стартовую)
        if count == total_cells:
            # Проверяем, можем ли вернуться в старт (0,0) из (r,c)
            for nr, nc in neighbors(r, c):
                if nr == 0 and nc == 0:
                    # Найден цикл
                    result += 1
                    return
            return

        # Пробуем пойти во все возможные соседние не посещенные клетки
        for nr, nc in neighbors(r, c):
            if not visited[nr][nc]:
                visited[nr][nc] = True
                backtrack(nr, nc, count + 1)
                visited[nr][nc] = False

    backtrack(0, 0, 1)
    print(result)

if __name__ == "__main__":
    solve()
