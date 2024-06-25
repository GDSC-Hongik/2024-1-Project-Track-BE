데이터 베이스 : 실제로 데이터를 저장하는 곳
- SQL
추가 `Create`
조회 `Read`
수정 `Update`
삭제 `Delete`

- ORM(Object-Relational Mapper)

1. 사용할 데이터 확인 
2. 데이터 모델링 
3. 데이터에 맞는 field작성
4. 모델 생성 or 변경
5. 장고에 반영 -> 
```
python manage.py makemigrations
python manage.py migrate
```

```
# models.py

from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=50)	# 문자열 최대 길이를 필수 인자로 넘겨야 함
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    img_path = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
```

## Django의 Model Field
### 필드(Field)
필드(Field)는 데이터 테이블에서의 열(column), 즉 데이터의 속성을 의미합니다.
#### CharField
class CharField(max_length=None)
제한된 길이의 문자열을 위한 필드입니다.
- max_length 필수 인수이며 입력할 최대 길이를 설정합니다.

#### IntegerField
class IntegerField()
정수 값을 위한 필드이며 -2147483648 부터 2147483647 범위를 지원합니다.

#### BooleanField
class BooleanField()
Boolean 값을 위한 필드 입니다.

#### DateField
class DateField(auto_now=False, auto_now_add=False)
DateField는 파이썬의 datetime.date 객체 형태로 표시되는 날짜 필드입니다.
- auto_now
	true로 설정되면 해당 객체가 변경(save) 될 때마다 자동으로 필드 값을 지금으로 수정합니다. '마지막 수정 시간' 같은 항목으로 사용하면 좋겠죠?
- auto_now_add
	모델이 처음 생성될 때 한 번, 자동으로 필드 값을 지금으로 설정합니다. '생성된 시간'을 저장하기 위해 많이 사용합니다.

#### DateTimeField
class DateTimeField(auto_now=False, auto_now_add=False)
파이썬의 datetime.datetime 객체 형태로 표시되는 날짜 필드 입니다. DateField와 인수 옵션은 같습니다.

#### EmailField
class EmailField(max_length=254)
CharField의 하위 클래스로 문자열이 이용 가능한 이메일 주소인지 EmailValidator를 통해 확인합니다. 

#### FileField
class FileField(upload_to=None, max_length=100)
파일 업로드를 위한 필드 입니다.
- upload_to 업로드될 경로를 지정하는 필드로 Storage.save() 함수로 값이 전달되어 저장됩니다. 

#### ImageField
class ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
FileField를 상속하여 구현되는 파일 업로드를 위한 필드이며 기본적으로 최대 길이가 100인 문자열 형식으로 생성됩니다. 위에서 나왔던 FileField에서 업로드된 파일이 정상적인 이미지 파일인지 확인하는 과정이 추가된 필드로 이미지 처리를 위한 Pillow 라이브러리가 필수적으로 필요합니다. 
- height_field & width_field 객체가 저장 될 때 이미지의 높이와 너비값이 자동으로 채워 집니다.


### 옵션(Option)
아래 옵션은 모든 필드 타입에 사용할 수 있으며 선택적으로 적용할 수 있습니다.

**null**
Field.null

기본 값은 False이며 Null 값 허용 여부를 선택 합니다.
만약 이 null 옵션을 적용할 필드가 문자열 기반 필드 (Char, Text)일 경우에는 주의해서 사용해야 하는데 ' ' (빈 문자열)과 Null 모두 해당 필드의 데이터가 없다는 것을 의미하기 때문입니다. 일반적으로 데이터가 없다는 것을 의미하는 값은 하나여야 하므로 Django는 문자열 기반 필드가 데이터가 없음을 표시할 때는 ' '(빈 문자열)을 사용하도록 권장하고 있습니다.

**blank**
Field.blank

기본 값은 False이며 True로 설정한 경우 필드 값을 빈 값으로 설정할 수 있습니다.
그렇다면 null과 blank의 차이는 무엇 일까요?
null은 온전히 데이터베이스와 관련된 사항이고 blank는 데이터의 유효성 검사와 관련된 옵션입니다. 예를들어 blank가 True라면 해당 필드에 데이터를 입력하지 않아도 유효성 검사를 통과하게 됩니다.

**default**
Field.default

필드의 기본값을 설정하는 옵션으로 값 또는 함수가 들어갈 수 있습니다.

**db_column**
Field.db_column

해당 필드에 사용할 데이터베이스 속성 명을 지정합니다. 따로 지정하지 않을 경우 일반적으로 필드의 이름을 사용합니다.

[Field와 Option에 관한 공식 문서]( https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.Field.default)

![](https://velog.velcdn.com/images/yeonee911/post/8c47fdb8-a982-48ac-a3c6-bc69fcbda217/image.png)


## Django의 Migration
마이그레이션(Migration)은 모델(Model)의 변경 사항 즉 Django 프로젝트의 데이터 구조 변경 사항을 관리하기 위한 Django만의 관리 방법입니다. 변경될 때마다 히스토리를 하나씩 만들어 두고 마치 블럭을 갈아 끼우듯 생성한 히스토리를 실제 데이터베이스에 반영하는 거죠. 그리고 이 모든 과정은 Django의 ORM(Object-Relational Mapping)을 통해 진행됩니다.

### makemigrations
```
python manage.py makemigrations
```
모델의 변경 사항을 인식해서 새로운 마이그레이션을 만듭니다. 이때 마이그레이션은 각 앱 디렉토리 내 migrations 디렉토리 안쪽에 생성됩니다.

### migrate
```
python manage.py migrate
```
생성된 최신 버전의 마이그레이션을 데이터베이스에 반영합니다. 만약 이전 마이그레이션으로 되돌리고 싶다면 python manage.py migrate {앱 이름} {되돌릴 마이그레이션 번호}를 사용할 수 있습니다

### showmigrations
```
python manage.py showmigrations
```
현재 django 프로젝트의 모든 마이그레이션과 반영 상태를 나타냅니다. 만약 특정 앱에 대한 것만 보고 싶다면 python manage.py showmigrations {앱 이름}을 사용할 수 있습니다.
 
### sqlmigrate
```
python manage.py sqlmigrate {앱 이름} {마이그레이션}
```
인수로 넘겨준 마이그레이션이 ORM을 통해 변경된 SQL문을 출력합니다. sqlmigrate를 통해 모델이 의도한 대로 SQL문으로 변경되어 데이터베이스에 반영되었는지 확인할 수 있습니다.

[migration 공식 문서](https://docs.djangoproject.com/en/2.2/topics/migrations/)

## shell
: 사용자의 명령어를 받아서 해석한 다음, 프로그램을 실행
from foods.models import Menu	# 모델 불러오기 (foods앱 안에 Menu 모델)

{model}.objects.create({필드명}={값})
: 데이터베이스에 데이터 저장하기

{model}.objects.all()
: 모든 데이터 조회하기

{model}.objects.all().values()
: 세부 데이터 조회하기


[Error] Django django.db.utils.OperationalError: no such table:
->> makemigrations
- >> migrate
: model을 만들면 장고에 알려줘야함!!