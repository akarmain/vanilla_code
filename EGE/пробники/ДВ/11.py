import math

memory_limit_mb = 23  # условие
iterations = 125_300  # условие
memory_limit_bytes = memory_limit_mb * 1024 * 1024

for kod in range(1, 5000):
    bits_per_value = math.ceil(math.log2(kod))

    # Сколько байт займёт одна запись из 119 полей по bits_per_value бит каждому
    bytes_per_record = math.ceil((119 * bits_per_value) / 8)
    # Общий объём памяти для всех записей
    total_bytes = iterations * bytes_per_record

    # Проверяем, превысили ли мы лимит
    if total_bytes > memory_limit_bytes:
        print(kod)
