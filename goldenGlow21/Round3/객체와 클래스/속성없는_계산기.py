class SimpleCalculator:
    # 계산기 클래스
    @staticmethod
    def add(first_number, second_number):
        return first_number + second_number
    
    @staticmethod
    def subtract(first_number, second_number):
        return first_number - second_number
    
    @staticmethod
    def multiply(first_number, second_number):
        return first_number * second_number
    
    @staticmethod
    def divide(first_number, second_number):
        return first_number / second_number
    
    
# 계산기 인스턴스 생성
calculator = SimpleCalculator()
    
# 계산기 연산 호출
print(calculator.add(4, 5))
print(calculator.subtract(4, 5))
print(calculator.multiply(4, 5))
print(calculator.divide(4, 5))
