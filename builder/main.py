from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """Specifies methods for creating a product"""

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
    def __init__(self):
        self.parts = []

    def add(self, parts: Any):
        self.parts.append(parts)

    def list_parts(self):
        print(f"Product parts: {', '.join(self.parts)}", end="")


class ConcreteBuilder1(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product1()

    def product(self):
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
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()
