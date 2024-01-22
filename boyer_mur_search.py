# алгоритм пошуку підрядка Боєра-Мура
def build_shift_table(pattern):
    # створюємо таблицю зсувів для алгоритму Боєра-Мура.
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table


def bm_search(text, pattern):
    # створюємо таблицю зсувів для патерну (підрядка)
    shift_table = build_shift_table(pattern)
    i = 0

    # проходимо по основному тексту, порівнюючи з підрядком
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i  # підрядок знайдено
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    # якщо підрядок не знайдено, повертаємо -1
    return -1


if __name__ == '__main__':
    text = "Being a developer is not easy"
    pattern = "developer"
    shift_table = build_shift_table(pattern)
    print(shift_table)

    position = bm_search(text, pattern)
    if position != -1:
        print(f"Підрядок знайдено починаючи з індекса {position}")
    else:
        print("Підрядок не знайдено")
