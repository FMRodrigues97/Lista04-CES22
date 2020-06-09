from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass


class Carro(Creator):
    def factory_method(self) -> Carro:
        return Carro()


class Caminhao(Creator):
    def factory_method(self) -> Caminhao:
        return Caminhao()


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class Carro(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class Caminhao(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
