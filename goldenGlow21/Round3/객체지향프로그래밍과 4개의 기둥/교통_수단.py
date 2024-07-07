from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        """추상 메소드 start: 교통 수단의 주행을 시작한다"""
        pass

    @property
    @abstractmethod
    def speed(self):
        """변수 _speed(교통 수단의 속도)에 대한 추상 getter 메소드"""
        pass

    def stop(self):
        """일반 메소드 stop: 교통 수단의 속도를 0으로 바꾼다"""
        self.speed = 0

print(Vehicle.mro())        
print(dir(Vehicle))
