from __future__ import annotations
from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def operation(self):
        pass


class Creator(ABC):

    # The concrete implementation of the Product will be implemented here by the concrete class
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()

        result = f"Creator: the same creator's code has just worked with another {product.operation()}"

        return result


class ConcreteProduct1(Product):
    def operation(self):
        return "Creation of ConcreteProduct1"


class ConcreteProduct2(Product):
    def operation(self):
        return "Creation of ConcreteProduct2"


class ConcreteCreator1(Creator):

    def factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):

    def factory_method(self):
        return ConcreteProduct2()


def client_code(creator: Creator):
    print(
        "This class is not aware of the creator's class but this still works.\n"
        f"{creator.some_operation()}"
        )


if __name__ == "__main__":
    print("App created with Concrete Creator 1")
    client_code(ConcreteCreator1())
    print("\n")

    print("App created with Concrete Creator 2")
    client_code(ConcreteCreator2())
    print("\n")
