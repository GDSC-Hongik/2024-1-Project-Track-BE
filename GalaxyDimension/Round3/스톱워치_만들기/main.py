class Counter:
    """
    시계 클래스의 시, 분, 초를 각각 나타내는데 사용될 카운터 클래스
    """

    def __init__(self, limit):
        """
        인스턴스 변수 limit(최댓값), value(현재까지 카운트한 값)를 설정한다.
        인스턴스를 생성할 때 인스턴스 변수 limit만 파라미터로 받고, value는 초깃값 0으로 설정한다.
        """
        self.limit = limit
        self.value = 0


    def set(self, new_value):
        """
        파라미터가 0 이상, 최댓값 미만이면 value에 설정한다.
        아닐 경우 value에 0을 설정한다.
        """
        if self.limit > new_value >=0:
            self.value = new_value
        else:
            self.value = 0


    def tick(self):
        """
        value를 1 증가시킨다.
        카운터의 값 value가 limit에 도달하면 value를 0으로 바꾼 뒤 True를 리턴한다.
        value가 limit보다 작은 경우 False를 리턴한다.
        """
        self.value += 1
        if self.value >= self.limit:
            self.value = 0
        else:
            return False


    def __str__(self):
        """
        value를 최소 두 자릿수 이상의 문자열로 리턴한다. 
        일단 str 함수로 숫자형 변수인 value를 문자열로 변환하고 zfill 메소드를 호출한다. 
        """
        return str(self.value).zfill(2)
    
    
# 최대 30까지 셀 수 있는 카운터 인스턴스 생성
counter = Counter(30)

# 0부터 5까지 센다
print("1부터 5까지 카운트하기")
for i in range(5):
    counter.tick()
    print(counter)

# 타이머 값을 0으로 바꾼다
print("카운터 값 0으로 설정하기")
counter.set(0)
print(counter)

# 카운터 값 27로 설정
print("카운터 값 27로 설정하기")
counter.set(27)
print(counter)

# 카운터 값이 30이 되면 0으로 바뀌는지 확인
print("카운터 값이 30이 되면 0으로 바뀝니다")
for i in range(5):
    counter.tick()
    print(counter)       