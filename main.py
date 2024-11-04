class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner         # Публічний атрибут
        self.__balance = balance   # Приватний атрибут (прихований)

    # Геттер для доступу до приватного атрибуту
    def get_balance(self):
        return self.__balance

    # Сеттер для встановлення значення приватного атрибуту
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Баланс не може бути негативним")

    # Метод для внесення коштів
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Внесено {amount} на рахунок")
        else:
            print("Сума має бути позитивною")

# Створення об'єкта класу BankAccount
account = BankAccount("Alice", 1000)

# Виклик геттера для перевірки балансу
print(account.get_balance())  # Виведе: 1000

# Внесення коштів
account.deposit(500)  # Виведе: Внесено 500 на рахунок

# Спроба встановити негативний баланс через сеттер
account.set_balance(-500)  # Виведе: Баланс не може бути негативним