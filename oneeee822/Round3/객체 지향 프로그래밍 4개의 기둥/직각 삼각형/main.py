from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class RightTriangle(Shape):
		# 여기 코드를 채워넣어주세요
		def __init__(self, side):
		    self.side = side
		   
		def draw(self):
		    for i in range(1,self.side+1) :
		        print('* '*i)
		   
		def __str__(self):
		    return f"\n변이 {self.side}인 직각이등변삼각형"


# 실행 코드
right_triangle = RightTriangle(7)

right_triangle.draw()
print(right_triangle)

