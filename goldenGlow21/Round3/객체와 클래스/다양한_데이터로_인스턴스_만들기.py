class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_params):
        from_string = string_params.split(",")
        name = from_string[0]
        email = from_string[1]
        password = from_string[2]
        return cls(name, email, password)

    @classmethod
    def from_list(cls, list_params):
        name = list_params[0]
        email = list_params[1]
        password = list_params[2]
        return cls(name, email, password)

# 유저 생성 및 초기값 설정
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)