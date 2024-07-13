class MenuItem:
    # 음식 메뉴를 나타내는 클래스
    def __init__(self, name, price):
        # 여기에 코드를 작성하세요
        self.name = name
        self.price = price

    def __str__(self):
        # 여기에 코드를 작성하세요
        return f"{self.name} 가격: {self.price}"

# 메뉴 인스턴스 생성
burger = MenuItem("햄버거", 4000)
coke = MenuItem("콜라", 1500)
fries = MenuItem("후렌치 후라이", 1500)

# 메뉴 인스턴스 출력
print(burger)
print(coke)
print(fries)