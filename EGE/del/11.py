def to_base3(num):
    """Перевод числа в троичную систему счисления (строка)"""
    if num == 0: return '0'
    s = ''
    while num > 0:
        s = str(num % 3) + s
        num //= 3
    return s

def algorithm(n):
    # 1. Строится троичная запись
    s = to_base3(n)
    
    # 2. Обработка по правилам
    if n % 3 == 0:
        # а) дописываются две последние троичные цифры
        s = s + s[-2:]
    else:
        # б) сумма цифр * 3 -> в троичную -> дописать
        digit_sum = sum(int(d) for d in s)
        val = digit_sum * 3
        s_val = to_base3(val)
        s = s + s_val
        
    # 3. Перевод результата в десятичную систему
    return int(s, 3)

# Поиск числа R, ближайшего к 826
target = 826
min_diff = float('inf')
best_r = 0

for n in range(1, 100):
    r = algorithm(n)
    diff = abs(r - target)
    
    # Если нашли разницу меньше текущей минимальной, обновляем ответ
    if diff < min_diff:
        min_diff = diff
        best_r = r

print(f"Лучшее R: {best_r} (получено из N={best_r//9 if best_r%3==0 else '?'})")
print(f"Разница с {target}: {min_diff}")