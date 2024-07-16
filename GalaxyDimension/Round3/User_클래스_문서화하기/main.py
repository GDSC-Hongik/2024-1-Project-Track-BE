class User:
    """SNS의 유저를 나타내는 클래스"""
    count = 0

    def __init__(self, name, email, pw):
        """이름, 이메일, 비밀번호를 인스턴스 변수로 갖고, 인스턴스가 생성될 때마다 클래스 변수 count를 1씩 증가시킨다."""
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

    def say_hello(self):
        """유저의 이름을 포함한 인사 메시지를 출력한다."""
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def __str__(self):
        """유저 정보를 정의된 문자열 형태로 리턴한다."""
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

    @classmethod
    def number_of_users(cls):
        """총 유저 수를 출력하는 클래스 메소드"""
        print("총 유저 수는: {}입니다".format(cls.count))

help(User)
