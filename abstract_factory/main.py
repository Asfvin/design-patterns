from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    """
    Each product in a Factory should have a base inteface and each variant of this product
    must have this implemented
    """
    def useful_function_a(self) -> None:
        pass


class AbstractProductB(ABC):
    """
    All products can interact with one another but proper interaction can only be done within the 
    product of the same concrete implementation
    """
    def useful_function_b(self) -> None:
        pass

    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        pass


class AbstractFactory(ABC):
    """
    Declares a set of method that provides methods that return separate abstract products
    These collections of products are called families. They share a single theme but the 
    products themselves are incompatible with one another
    """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return 'This is the product of A1'


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return 'This is the product of A2'


class ConcreteProductB1(AbstractProductB):
    """
    Product B1 only works with A1. But it accepts any instance of AbstractProductA
    """
    def useful_function_b(self) -> str:
        return 'This is the product of B1'

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()

        return f'This is the result of product B1 and {result}'


class ConcreteProductB2(AbstractProductB):
    """
    We could say that B2 only works with A2 but it accepts any variant of product A2.
    """
    def useful_function_b(self) -> str:
        return 'This is the product of B2'

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()

        return f'This is the result of product B2 and {result}'


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


def client_code(factory: AbstractFactory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f'{product_a.useful_function_a()}')
    print(f'{product_b.another_useful_function_b(product_a)}')


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())
