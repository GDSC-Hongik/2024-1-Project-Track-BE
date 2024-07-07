class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_params):
        # 여기에 코드를 작성하세요
        a = string_params.split(',')
        return User(a[0],a[1],a[2])

    @classmethod
    def from_list(cls, list_params):
        # 여기에 코드를 작성하세요
        return User(list_params[0],list_params[1],list_params[2])

# 유저 생성 및 초기값 설정
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)