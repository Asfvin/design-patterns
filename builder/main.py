from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """Specifies methods for creating a product. What are the possible configurations that
    this product can take
    """

    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def product_part_a(self):
        pass

    @abstractmethod
    def product_part_b(self):
        pass

    @abstractmethod
    def product_part_c(self):
        pass


class Product1:
    """The sepecific product used by certain Builder"""
    def __init__(self):
        self.parts = []

    def add(self, part: Any):
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class ConcreteBuilder1(Builder):
    """
    Follows the interface of Builder and provides implementations. Different builder can have
    different implementation"""

    """A blank product instantiation should contain a blank product"""
    def __init__(self):
        self.reset()

    # Creates an instance of Product1 and stores it as _product
    def reset(self):
        self._product = Product1()

    @property
    def product(self):
        # This is a method to retrieve the result. When you are instantiating the builder
        # the self._product will be implemented and you can call the methods without calling this
        # Once this method is called, it will reset the builder
        product = self._product
        self.reset()
        return product

    def product_part_a(self):
        self._product.add('Part A')

    def product_part_b(self):
        self._product.add('Part B')

    def product_part_c(self):
        self._product.add('Part C')


class Director:
    """Only responsible for specifying the exact steps of the builder"""

    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder
    
    def build_minimal_viable_product(self):
        self.builder.product_part_a()

    def build_full_feature_product(self):
        self.builder.product_part_a()
        self.builder.product_part_b()
        self.builder.product_part_c()


if __name__ == "__main__":
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_feature_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.product_part_a()
    builder.product_part_b()
    builder.product.list_parts()
