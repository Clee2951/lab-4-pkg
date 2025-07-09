from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, base : float, height : float):
        self.base = base
        self.height = height 
        pass

    def area(self):
        return self.base * self.height

class Triangle(Shape):
    def __init__(self, base : float, height : float):
        self.base = base
        self.height = height
        pass

    def area(self):
        return self.base * self.height / 2