BIN_TO_OCT = {
    "000": "0", "001": "1", "010": "2", "011": "3",
    "100": "4", "101": "5", "110": "6", "111": "7"
}

BIN_TO_HEX = {
    "0000": "0", "0001": "1", "0010": "2", "0011": "3",
    "0100": "4", "0101": "5", "0110": "6", "0111": "7",
    "1000": "8", "1001": "9", "1010": "A", "1011": "B",
    "1100": "C", "1101": "D", "1110": "E", "1111": "F"
}

OCT_TO_BIN = {v: k for k, v in BIN_TO_OCT.items()}
HEX_TO_BIN = {v: k for k, v in BIN_TO_HEX.items()}


def check_binary(binary: str) -> str:
    if not binary:
        raise ValueError("Пустая строка не является двоичным числом")
    if any(ch not in "01" for ch in binary):
        raise ValueError("Строка должна состоять только из 0 и 1")
    return binary


def normalize_binary(binary: str) -> str:
    return binary.lstrip("0") or "0"


def pad_left(binary: str, group_size: int) -> tuple[str, int]:
    pad = (-len(binary)) % group_size
    return "0" * pad + binary, pad


def split_groups(s: str, group_size: int) -> list[str]:
    return [s[i:i + group_size] for i in range(0, len(s), group_size)]


def binary_to_base_2k(binary: str, group_size: int):
    binary = check_binary(binary)

    if group_size == 3:
        table = BIN_TO_OCT
    elif group_size == 4:
        table = BIN_TO_HEX
    else:
        raise ValueError("group_size должен быть 3 или 4")

    padded, added_zeros = pad_left(binary, group_size)
    groups = split_groups(padded, group_size)
    digits_full = "".join(table[g] for g in groups)
    digits_short = digits_full.lstrip("0") or "0"

    return {
        "original_binary": binary,
        "padded_binary": padded,
        "added_zeros": added_zeros,
        "groups": groups,
        "digits_full": digits_full,
        "digits_short": digits_short,
    }


def base_2k_to_binary(digits: str, group_size: int):
    digits = digits.upper().strip()

    if group_size == 3:
        table = OCT_TO_BIN
    elif group_size == 4:
        table = HEX_TO_BIN
    else:
        raise ValueError("group_size должен быть 3 или 4")

    groups = []
    for ch in digits:
        if ch not in table:
            raise ValueError(f"Недопустимый символ для основания 2^{group_size}: {ch}")
        groups.append(table[ch])

    return "".join(groups), groups


def analyze_transition(binary: str):
    binary = check_binary(binary)
    norm = normalize_binary(binary)

    oct_data = binary_to_base_2k(binary, 3)
    hex_data = binary_to_base_2k(binary, 4)

    oct_back_full, oct_groups_back_full = base_2k_to_binary(oct_data["digits_full"], 3)
    hex_back_full, hex_groups_back_full = base_2k_to_binary(hex_data["digits_full"], 4)

    oct_back_short, oct_groups_back_short = base_2k_to_binary(oct_data["digits_short"], 3)
    hex_back_short, hex_groups_back_short = base_2k_to_binary(hex_data["digits_short"], 4)

    print("=" * 72)
    print(f"Исходное двоичное число: {binary}")
    print(f"Нормализованный вид:     {norm}")
    print(f"Длина исходной записи:   {len(binary)} бит")

    print("\n[Переход в восьмеричную]")
    print(f"Дополнено слева нулями:  {oct_data['padded_binary']} (+{oct_data['added_zeros']})")
    print(f"Группы по 3 бита:        {' | '.join(oct_data['groups'])}")
    print(f"Полная запись:           {oct_data['digits_full']}")
    print(f"Обычная запись:          {oct_data['digits_short']}")
    print(f"Цифр в полной записи:    {len(oct_data['digits_full'])}")
    print(f"Цифр в обычной записи:   {len(oct_data['digits_short'])}")
    print(f"Обратный перевод (full): {oct_back_full}   -> группы {' | '.join(oct_groups_back_full)}")
    print(f"Обратный перевод (short):{oct_back_short}   -> группы {' | '.join(oct_groups_back_short)}")

    print("\n[Переход в шестнадцатеричную]")
    print(f"Дополнено слева нулями:  {hex_data['padded_binary']} (+{hex_data['added_zeros']})")
    print(f"Группы по 4 бита:        {' | '.join(hex_data['groups'])}")
    print(f"Полная запись:           {hex_data['digits_full']}")
    print(f"Обычная запись:          {hex_data['digits_short']}")
    print(f"Цифр в полной записи:    {len(hex_data['digits_full'])}")
    print(f"Цифр в обычной записи:   {len(hex_data['digits_short'])}")
    print(f"Обратный перевод (full): {hex_back_full}   -> группы {' | '.join(hex_groups_back_full)}")
    print(f"Обратный перевод (short):{hex_back_short}   -> группы {' | '.join(hex_groups_back_short)}")

    print("\n[Вывод по конкретному числу]")
    print("1) Значение числа сохраняется.")
    print("2) Группы бит восстанавливаются однозначно из каждой цифры:")
    print("   - 1 восьмеричная цифра <-> 3 бита")
    print("   - 1 шестнадцатеричная цифра <-> 4 бита")
    print("3) Но точное количество ведущих нулей в исходной двоичной записи")
    print("   из обычной 8/16-ричной записи восстановить нельзя.")
    print("4) Поэтому числовое значение восстанавливается однозначно,")
    print("   а исходная строка бит — не всегда.")


def demonstrate_ambiguity():
    print("=" * 72)
    print("Демонстрация неоднозначности после отброса ведущих нулей:")
    examples = ["1", "01", "001", "0001", "000001"]

    for b in examples:
        oct_short = binary_to_base_2k(b, 3)["digits_short"]
        hex_short = binary_to_base_2k(b, 4)["digits_short"]
        print(f"{b:>6} -> oct: {oct_short:>2}, hex: {hex_short:>2}")

    print("\nВидно, что разные двоичные записи могут дать одну и ту же")
    print("обычную восьмеричную/шестнадцатеричную запись.")
    print("Например: 1, 01, 001, 0001 -> все дают 1.")
    print("Значит, ведущие нули теряются.")


def final_conclusion():
    print("=" * 72)
    print("ОБЩИЙ ВЫВОД")
    print("1. Представления в системах с основаниями 8 и 16 сохраняют")
    print("   числовое значение двоичного числа без потерь.")
    print("2. Каждая цифра 8-ричной системы однозначно кодирует 3 бита,")
    print("   а каждая цифра 16-ричной системы — 4 бита.")
    print("3. Поэтому обратный переход однозначен для значения числа.")
    print("4. Однако при обычной записи отбрасываются ведущие нули,")
    print("   и точная исходная длина двоичной записи теряется.")
    print("5. Следовательно:")
    print("   - по значению числа представления равносильны;")
    print("   - по длине записи 8 и 16 являются сжимающими относительно двоичной;")
    print("   - для точного восстановления исходной битовой строки")
    print("     нужно дополнительно хранить длину или число ведущих нулей.")


if __name__ == "__main__":
    test_numbers = [
        "0",
        "1",
        "101",
        "00101",
        "110101101",
        "1011110010",
        "0001110001"
    ]

    for number in test_numbers:
        analyze_transition(number)

    demonstrate_ambiguity()
    final_conclusion()