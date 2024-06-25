django - TIME_ZONE

error that port is already in use. django
[에러 해결](https://velog.io/@bky373/%EC%97%90%EB%9F%AC-%EC%9E%A5%EA%B3%A0-Error-That-port-is-already-in-use-%ED%95%B4%EA%B2%B0)
원인분석 : 같은 디렉토리 안에 프로젝트를 두 개 만들었는데, 한 프로젝트의 서버를 실행하고 ctrl+c를 실행하지 않고 꺼서 문제가 됐는듯!

url 구조 만들기
![](https://velog.velcdn.com/images/yeonee911/post/a2af799c-5bff-4c6a-ab22-e4f81000e9db/image.png)

![](https://velog.velcdn.com/images/yeonee911/post/38438951-49f9-4c88-8660-15ce51037870/image.png)

## 모델 필드(Model Field)

### 필드 유형(Field Types)

| 필드명        | 설명                                                                            | 개별속성                                                                                                     |
| ------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| CharField     | 최대 길이가 정해진 문자열 필드                                                  | max_length (최대 글자수)                                                                                     |
| TextField     | 최대 길이가 정해지지 않은 문자열 필드                                           |
| EmailField    | CharField와 같은 문자열 필드지만 입력된 형식이 이메일 형식 인지를 체크하는 필드 | max_length=254 (기본값)                                                                                      |
| URLField      | CharField과 같은 문자열 필드지만 입력된 형식이 URL 형식 인지를 체크하는 필드    | max_length=200 (기본값)                                                                                      |
| BooleanField  | True, False 값을 갖는 필드                                                      |
| IntegerField  | 정수 형식의 필드                                                                |
| FloatField    | 부동 소수점 형식의 필드                                                         |
| DateField     | 날짜 형식의 필드                                                                | auto_now (수정 될 때 마다 새로운 값으로 갱신)<br>auto_now_add (생성 될 때 값이 입력 되고 추후 변경하지 않음) |
| TimeField     | 시간 형식의 필드                                                                | auto_now, auto_now_add                                                                                       |
| DateTimeField | 날짜 시간 형식의 필드                                                           | auto_now, auto_now_add                                                                                       |

### 필드 옵션(Field options)

| 필드 옵션    | 설명                                                                  | 기본값 |
| ------------ | --------------------------------------------------------------------- | ------ |
| null         | True 일 경우 데이터베이스에 빈 값을 저장할 때 NULL을 사용하게 됩니다. | False  |
| blank        | True 일 경우 해당 필드를 비워 둘 수 있게 합니다.                      | False  |
| default      | 필드에 기본값을 지정할 때 사용합니다.                                 |
| editable     | 필드의 수정 가능 여부를 설정합니다.                                   | True   |
| help_text    | 해당 필드를 입력할 때 보여줄 도움말을 설정합니다.                     |
| unique       | True 일 경우 중복된 값을 입력할 수 없게 합니다.                       | False  |
| verbose_name | 사람이 인식하기 좋은 별명을 필드에 설정합니다.                        |
| validators   | 필드의 유효성 검증에 사용할 검증 목록 입니다.                         |

## Django Model API

### API란?

- Application Programming Interface의 약자
- 어플리케이션에서 시스템의 기능을 제어할 수 있도록 만든 인터페이스

### Queryset

- Django Model의 데이터가 담겨있는 목록
  ![](https://velog.velcdn.com/images/yeonee911/post/0d74da0a-fcca-45d8-8692-ed47fa921a26/image.png)
  ![](https://velog.velcdn.com/images/yeonee911/post/27931c89-74f3-4ccc-9a9d-2d7d7bc0bde0/image.png)
  ![](https://velog.velcdn.com/images/yeonee911/post/84c373e6-a3fd-4b32-91c6-dcc17b930ac1/image.png)

### 필드 조건 옵션 (Field Lookups)

Queryset 연산을 할 때 사용할 수 있는 여러 필드 조건 옵션입니다. 필드명 뒤에 \_\_ 를 쓰고 사용할 옵션 인자를 적어 주면 됩니다.
