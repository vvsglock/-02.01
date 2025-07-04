from dataclasses import dataclass


@dataclass
class Enterprises:
    name: str
    prod: str
    profit: int
    tax: int


def load_data(file_path: str):
    records = []
    with open(file_path, 'r', encoding='utf-8') as file:
        next(file)
        for line in file:
            name, prod, profit, tax = line.strip().split("|")
            records.append(
                Enterprises(name, prod, int(profit), int(tax))
            )

    return records


def write_data(file_path: str, records: list[Enterprises]):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("Предприятие|Продукция|Прибыль|Налоги\n")
        for r in records:
            file.write(f"{r.name}|{r.prod}|{r.profit}|{r.tax}\n")


def add_enterprise(records: list[Enterprises], name: str, prod: str, profit: int, tax: int):
    records.append(
        Enterprises(name, prod, int(profit), int(tax))
    )


def total_sum_tax(records: list[Enterprises]):
    total = 0
    for r in records:
        total += r.tax

    return total


def clear_profit(records: list[Enterprises], name: str):
    profit = 0
    for r in records:
        if r.name == name:
            profit = r.profit - r.tax

    return profit


def main():
    path = "C:/Users/User/PycharmProjects/region/.venv/database.txt"

    records = load_data(path)

    print("1. Добавить предприятие")
    print("2. Узнать общую сумму налогов")
    print("3. Узнать чистую прибыль предприятия")

    point = int(input())

    if point == 1:
        print("Введите название предприятия")
        name = input()

        print("Введите продукцию предприятия")
        prod = input()

        print("Введите прибыль предприятия")
        profit = int(input())

        print("Введите налог предприятия")
        tax = int(input())

        add_enterprise(records, name, prod, profit, tax)
        write_data(path, records)

    if point == 2:
        ttl = total_sum_tax(records)
        print(f"В казну пришло: {ttl}")

    if point == 3:
        print("Введите предприятие")
        name = input()

        clr = clear_profit(records, name)

        print(f"Чистая прибыль {name} = {clr}")


if __name__ == "__main__":
    main()