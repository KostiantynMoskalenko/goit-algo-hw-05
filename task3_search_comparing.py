"""
Завдання 3

Порівняти ефективність алгоритмів пошуку підрядка: Боєра-Мура,
Кнута-Морріса-Пратта та Рабіна-Карпа на основі двох текстових файлів
(стаття 1, стаття 2). Використовуючи timeit, треба виміряти час виконання
кожного алгоритму для двох видів підрядків: одного, що дійсно існує в
тексті, та іншого — вигаданого (вибір підрядків за вашим бажанням).
На основі отриманих даних визначити найшвидший алгоритм для кожного тексту
окремо та в цілому.
"""

import timeit
from typing import Callable

from boyer_mur_search import bm_search
from knut_moris_pratt_search import kmp_search
from rabin_karp_search import rk_search


def read_file(filename):
    with open(filename, 'r', encoding='cp1251') as f:
        return f.read()


def benchmark(func: Callable, text_: str, pattern_: str):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}(text, pattern)"
    return timeit.timeit(stmt=stmt, setup=setup_code,
                         globals={'text': text_,
                                  'pattern': pattern_}, number=10)


if __name__ == '__main__':
    text1 = read_file('стаття 1.txt')
    text2 = read_file('стаття 2.txt')
    real_pattern1 = "Експоненціальний пошук використовується для"
    fake_pattern1 = "при використанні мови програмування Python"
    real_pattern2 = "елемент"
    fake_pattern2 = "бармаглот"

    results1 = []
    for pattern in (real_pattern1, fake_pattern1):
        time = benchmark(bm_search, text1, pattern)
        results1.append((bm_search.__name__, pattern, time))
        time = benchmark(kmp_search, text1, pattern)
        results1.append((kmp_search.__name__, pattern, time))
        time = benchmark(rk_search, text1, pattern)
        results1.append((rk_search.__name__, pattern, time))
    results2 = []
    for pattern in (real_pattern2, fake_pattern2):
        time = benchmark(bm_search, text2, pattern)
        results2.append((bm_search.__name__, pattern, time))
        time = benchmark(kmp_search, text2, pattern)
        results2.append((kmp_search.__name__, pattern, time))
        time = benchmark(rk_search, text2, pattern)
        results2.append((rk_search.__name__, pattern, time))
    title = f"{'Алгоритм':<30} | {'Підрядок':<50} | {'Час виконання, сек'}"
    print(title)
    print("=" * len(title))
    for result in results1:
        print(f"{result[0]:<30} | {result[1]:<50} | {result[2]}")
    print("-" * len(title))
    for result in results2:
        print(f"{result[0]:<30} | {result[1]:<50} | {result[2]}")
    print("=" * len(title))
