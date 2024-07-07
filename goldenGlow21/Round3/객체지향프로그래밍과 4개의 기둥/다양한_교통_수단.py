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


class Bicycle(Vehicle):
    max_speed = 15 # 자전거의 최대 속도
    
    def __init__(self, speed):
        self._speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= Bicycle.max_speed else 0

    def start(self):
        print("자전거 페달 돌리기 시작합니다.")
        self.speed = Bicycle.max_speed / 3

    def __str__(self):
        return "이 자전거는 현재 {}km/h로 주행 중입니다.".format(self.speed)

class NormalCar(Vehicle):
    def __init__(self, speed, max_speed):
        self._speed = 0
        self.max_speed = max_speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= self.max_speed else 0

    def start(self):
        print("일반 자동차 시동겁니다.")
        self.speed = self.max_speed / 2

    def __str__(self):
        return "이 일반 자동차는 현재 {}km/h로 주행 중입니다.".format(self.speed)

class SportsCar(Vehicle):
    def __init__(self, speed, max_speed):
        self._speed = speed
        self.max_speed = max_speed

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= self.max_speed else 0

    def start(self):
        print("스포츠카 시동겁니다.")
        self.speed = self.max_speed

    def __str__(self):
        return "이 스포츠카는 현재 {}km/h로 주행 중입니다.".format(self.speed)

# 자전거 인스턴스
bicycle = Bicycle(0)        
    
# 일반 자동차 인스턴스
car = NormalCar(0, 100)

# 스포츠카 인스턴스
sports_car = SportsCar(0, 200)

# 정의한 인스턴스들을 모두 주행 시작시킨다
bicycle.start()
car.start()
sports_car.start()

# 자전거의 속도를 출력한다
print(bicycle)

# 자전거만 주행을 멈춰준다
bicycle.stop()

# 결과 값을 출력한다
print(bicycle)
print(car)
print(sports_car)