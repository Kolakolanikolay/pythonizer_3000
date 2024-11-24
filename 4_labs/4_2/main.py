import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as file:
        reader = csv.DictReader(file)
        list_for_dump = [row for row in reader]
        with open(OUTPUT_FILENAME, 'w') as f: #Не пойму, нужна тут табуляция или нет? как будто бы нужна, а то list_for_dump станет локальным списком. Вообщем сильно не ругайте, (если это ошибка) я и с табуляцией и без нее пробовал, оно работает и так и так
            json.dump(list_for_dump, f, indent= 4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
