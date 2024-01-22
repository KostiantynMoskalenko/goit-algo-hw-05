def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rk_search(main_string, substring):
    # довжини основного рядка та підрядка пошуку
    substring_length = len(substring)
    main_string_length = len(main_string)

    # базове число для хешування та модуль
    base = 256
    modulus = 101  # [0, 100]

    # хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base,
                                         modulus)

    # попереднє значення для перерахунку хешу
    h_multiplier = base ** (substring_length - 1) % modulus

    # проходимо крізь основний рядок
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i + substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) *
                                  h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base +
                                  ord(main_string[i +
                                                  substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1


if __name__ == '__main__':

    main_string = "Being a developer is not easy"
    substring = "developer is not easy"

    position = rk_search(main_string, substring)
    if position != -1:
        print(f"Підрядок знайдено, починаючи з індекса {position}")
    else:
        print("Підрядок не знайдено")
