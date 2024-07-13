from abc import ABC, abstractmethod

class Vehicle(ABC):
    # 여기에 코드를 작성하세요
    """추상 메소드 start: 교통 수단의 주행을 시작한다"""
    @abstractmethod
    def start(self):
        pass
    
    def stop(self):
        """일반 메소드 stop: 교통 수단의 속도를 0으로 바꾼다"""
        self.speed = 0 #_speed변수에 직접 0을 넣는 것보다 setter함수 speed 실행하는 것이 더 좋음
    
    @property
    @abstractmethod
    def speed(self):
        """변수 _speed(교통 수단의 속도)에 대한 추상 getter 메소드"""
        pass
    


print(Vehicle.mro())        
print(dir(Vehicle))