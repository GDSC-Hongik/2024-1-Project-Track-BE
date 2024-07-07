from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class RightTriangle(Shape):
    def __init__(self, side):
        self.side = side

    def draw(self):
        result = ''
        for i in range(1, self.side+1):
            result += '* ' * i + '\n'
        print(result)   

    def __str__(self):
        return f'변이 {self.side}인 직각이등변삼각형'

# 실행 코드
right_triangle = RightTriangle(7)

right_triangle.draw()
print(right_triangle)

