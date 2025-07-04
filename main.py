from dataclasses import dataclass

@dataclass
class Enterprice:
    name: str
    prod: str
    profit: int
    tax: int


class Economy:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.records: list[Enterprice] = []
        self.load_data()

    def load_data(self) -> None:
        with open(self.file_path, 'r', encoding='utf-8') as file:
            next(file)
            for line in file:
                name, prod, profit, tax = line.strip().split("|")
                self.records.append(
                    Enterprice(name, prod, int(profit), int(tax))
                )

    def write_data(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write("Предприятие|Продукция|Прибыль|Налоги\n")
            for r in self.records:
                file.write(f"{r.name}|{r.prod}|{r.profit}|{r.tax}\n")

    def add_enterprice(self, name: str, prod: str, profit: int, tax: int):
        self.records.append(
            Enterprice(name, prod, int(profit), int(tax))
        )
        self.write_data()

    def total_tax(self):
        total = 0
        for r in self.records:
            total += r.tax

        return total

    def clear_profit(self, name: str):
        clr = 0
        for r in self.records:
            if r.name == name:
                clr = r.profit - r.tax

        return clr


class UserInterface:
    @staticmethod
    def menu():
        print("1. Добавить предприятие")
        print("2. Общая сумма налогов")
        print("3. Чистая прибыль предприятия")

    @staticmethod
    def get_choice():
        return int(input())

    @staticmethod
    def add_enerprice():
        print("Введите данные предприятия")
        name = input("Введите имя:")
        prod = input("Введите тип продукции")
        profit = int(input("Введите прибыль"))
        tax = int(input("Введите сумму налога"))

        return name, prod, profit, tax

    @staticmethod
    def get_enterprice_name():
        print("Введите название предприятия")
        name = input()

        return name


def main():
    file_path = "C:/Users/User/PycharmProjects/region_OOP/database.txt"
    economy = Economy(file_path)
    ui = UserInterface()

    ui.menu()
    choice = ui.get_choice()

    if choice == 1:
        data = ui.add_enerprice()
        economy.add_enterprice(*data)
        print("Предприятие добавлено")

    if choice == 2:
        ttl = economy.total_tax()
        print(f"Общая сумма налогов: {ttl}")

    if choice == 3:
        name = ui.get_enterprice_name()
        prft = economy.clear_profit(name)

        print(f"Чистая прибыль {name} = {prft}")


if __name__ == "__main__":
    main()





