"""Приложение, считающее частоту слов во входном потоке."""
import argparse
import multiprocessing
import sys
from collections import Counter


arg_parser = argparse.ArgumentParser(
    prog='woco', description='Конфигурация запуска счетчика слов')

arg_parser.add_argument(
    '--processes', '-p', type=int, default=1,
    help='Количество процессов (по-умолчанию 1)')
arg_parser.add_argument(
    '--input_file', '-i', type=str, default='test.txt',
    help='Входящий поток (файл) (по-умолчанию test.txt)')


def count_words(string):
    """Возвращает счетчик для строки string.

    :param string: Строка
    :type string: str

    :rtype collections.Counter
    """
    return Counter(string.split())


def file_data(file_name):
    """Генератор данных из файла.

    :param file_name: Путь до файла
    :type file_name: str
    """
    with open(file_name) as f:
        for line in f:
            if not line.isspace():
                yield line


def start():
    """Запускает подсчет слов в файле."""
    args = arg_parser.parse_args()
    processes = args.processes

    pool = multiprocessing.Pool(processes=processes)
    counters = pool.imap(count_words, file_data(args.input_file), 25)

    # Итоговый счетчик
    counter = Counter()

    for c in counters:
        counter += c

    for word, count in counter.most_common():
        sys.stdout.write('{0} {1}\n'.format(word, count))


if __name__ == '__main__':
    multiprocessing.freeze_support()
    start()
