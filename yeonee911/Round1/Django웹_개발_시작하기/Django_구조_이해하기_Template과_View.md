> Django Framework
프레임워크 : 뼈대, 틀

1. 파이썬 사용
2. vsc
3. 가상환경 : 각각의 개발환경을 독립적으로 만들어서 관리 
	- pyenv : 파이썬 버전 설치, 관리
    - pyenv - virtualenv : 가상 환경을 구성, 파이썬 패키지 관리
4. wsl
	- windows에서 리눅스 터미널을 사용할 수 있게 해주는 확장 프로그램
    - macOS와 비슷한 개발환경을 windows에서 만들 수 있다
5. django 2.2

유닉스 커맨드 라인 -> 공부 필요성


pyenv local {가상 환경 이름} : 특정 디렉토리에 로컬 가상 환경 적용
django-admin --version : 설치된 장고 버전 확인
django-admin startproject {프로젝트 이름} : django 프로젝트 생성하기
ls : 현재 디렉토리에 어느 디렉토리 또는 파일이 있는지 볼 수 있다.
python manage.py runserver : django 개발 서버 실행

### 숨어있는 IP와 Port
```
django-admin runserver {ip:port}
python manage.py runserver {ip:port}
```
사실은 runserver 뒤에 IP와 Port 라는 인자가 숨어 있습니다.
`IP` : Internet Protocol의 약자. 네트워크 상에서 다른 컴퓨터와 내 컴퓨터를 구별하는 주소
`Port` : IP로 찾은 컴퓨터 내부에서 실행되고 있는 프로그램이나 서비스를 구분하는 값
-> 즉, IP로 컴퓨터를 찾고 포트를 통해 프로그램을 찾음

### 프로젝트 구조
![](https://velog.velcdn.com/images/yeonee911/post/81cb07fa-0356-4dab-84ad-582cb8568472/image.png)


1. Project Root : django 프로젝트의 모든 파일이 담겨있는 최상위 디렉토리 : 이름을 마음대로 바꿀 수 있음
	2. Project App : 우리 Project의 가장 중심이 되는 App : 이름을 바꾸면 많은 수정 / Django 프로젝트를 위한 여러 파일이 담겨 있는 디렉토리 입니다. 
    	2-1. `__init__.py` : 내가 있는 디렉토리가 Python 패키지로 인식되게 한다 / Python 3.3 버전 이상부터는 없어도 python패키지로 인식, but 하위 버전 호환을 위해 작성하는 것이 좋다
        2-2. settings.py : 시간대 설정, 데이터베이스 설정, 여러 경로 설정 등 / Django 프로젝트의 전반적인 설정을 담당
        2-3. urls.py : URL을 보고 알맞은 페이지로 연결해주는 역할
        2-4. wsgl.py : 웹 서버와 Python 어플리케이션인 Django가 소통하는데 필요한 일종의 프로토콜
    3. manage.py : Django 프로젝트 관리를 위한 명령어를 지원/앱 생성, 데이터베이스 관련 명령, 개발 서버 실행 등
    4. de.sqlite3 : 우리 프로젝트에서 사용하는 데이터베이스 파일

프로젝트 vs 앱
프로젝트 : 웹 서비스 전체
앱 : 기능을 나타내는 단위

python manage.py startapp {앱 이름} : django 앱 생성하기

![](https://velog.velcdn.com/images/yeonee911/post/8b69dbcf-4cf5-43ee-97ca-9f1d6eee959a/image.png)
admin.py : 앱을 django관리자와 연동하기 위해 필요한 설정 파일
apps.py : 앱에 대한 설정을 넣어두는 파일
__django의 핵심__
models.py : django app에서 사용할 데이터 모델 정의, 데이터베이스 연동과 관련된 파일
views.py : django app 의 메인 로직 처리와 관련된 파일
__
test.py : 프로젝트의 테스트 코드를 작성하는 곳
migrations : 데이터베이스의 변경 사항 히스토리 누적


필수!! 새로운 앱을 만들면 장고에게 알려줘야 함
![](https://velog.velcdn.com/images/yeonee911/post/6e429ecf-e130-4c19-a3d1-5603481c9d36/image.png)


### url 라우팅
```
settings.py

ROOT_URLCONF = 'costuarant.urls'
# 장고가 URL을 보고 가장 먼저 어떤 파일을 봐야 할지 설정하는 부분
```

```
costuarnat : urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foods/', include('foods.urls'))  
    #'foods/' 있으면 그 다음에 foods파일의 urls.py를 봐라
]
```

```
foods : urls.py

urlpatterns = [
    path('index/', views.index)
    # 'index/'매칭 -> views.py의 함수 index를 봐라
]
```

```
view.py

def index(request):
    return HttpResponse("<h2>Hello, Django !</h2>")
    # 파라미터로 request를 받고 응답(<h2>Hello, Django !</h2>)을 리턴
```

Django는 클라이언트-서버 구조에서 서버에 속합니다.
서버는 웹 페이지 뿐만 아니라 이미지나 동영상등 여러가지 형태의 자원(Resource)를 클라이언트에게 제공할 수 있습니다.

URL(Uniform Resource Locator)는 네트워크 상의 자원(Resource)의 위치를 나타내는 문자열 입니다.
그 중에서 Domain은 서버를 의미합니다.


템플릿 : 화면 구성을 담당하는 부분

## render() 함수에 대해 알아보자
### render()
**render( request, template_name, context=None, content_type=None, status=None, using=None )**
인자로 넘겨주는 템플릿과 context 데이터를 합쳐서 HttpResponse 객체로 돌려주는 함수인 거죠.

### 필수 인자
: `request` `template_name`
- `request`에는 데이터를 요청한 요청 객체를 넘겨줍니다. 
- `template_name`은 렌더링에 사용할 대상 템플릿을 명시합니다.

### 선택 인자
- `context` 는 템플릿에 추가할 값들이 들어 있는 사전형 인자로 기본값은 아무것도 없는 None입니다.
- `content_type` 은 결과로 만들어 내는 문서의 유형을 말하며 기본값은 'text/html' 즉 HTML 웹 페이지입니다.
- `status` 는 상태 코드(Status Code) 값이며 기본값은 200(성공)입니다. 상태 코드는 클라이언트의 요청이 성공적으로 처리되었는지에 대한 정보를 주는 코드인데 뒤에서 자세하게 다루도록 하겠습니다.
- `using` 은 템플릿을 렌더하는 템플릿 엔진을 지정할 수 있는 인자입니다. 원하는 경우 다른 템플릿 엔진을 사용하여 템플릿을 렌더링할 수 있습니다.

### 두 개의 render
1. 서버에서 Django 코드를 render 해서 HTML 파일로 만든다
2. 웹 브라우저에서 HTML 파일을 render 해서 우리가 보는 웹페이지로 바꿔준다


## MVT
Django는 맨 처음 url을 보고 알맞은 메인 로직을 처리하는 view를 호출합니다.
view에서는 필요하다면 model을 통해 데이터베이스와 소통하고
처리한 데이터를 화면을 담당하는 template과 함께 렌더해서 최종 화면을 만든 후  
view를 통해 클라이언트 에게 응답으로 돌려줍니다. 
이러한 Django의 구조를 mvt아키텍처 라고 합니다.

### Model
- 데이터 구조 생성
- 데이터베이스와 소통
### Template
- 웹 사이트의 화면 구성 담당
- 매번 바뀌는 동적인 화면을 구성
### View
- 웹 사이트의 로직을 담당
- Model과 Template 사이를 연결
-> 요청을 처리해서 응답
![](https://velog.velcdn.com/images/yeonee911/post/e744da7b-525b-4d8a-93d5-86fcbfcc4692/image.png)

## 아키텍처 패턴(Architecture Pattern)
: 소프트웨어 내부에 존재하는 구조적인 패턴
1. 계층화 패턴(Layered pattern)
2. 클라이언트-서버 패턴 (Client-server pattern)
3. 마스터-슬레이브 패턴 (Master-slave pattern)
4. 파이프-필터 패턴 (Pipe-filter pattern)
5. 브로커 패턴 (Broker pattern)
6. 피어 투 피어 패턴 (Peer-to-peer pattern)
7. 이벤트-버스 패턴 (Event-bus pattern)
8. MVC 패턴 (Model-view-controller pattern)
9. 블랙보드 패턴 (Blackboard pattern)
10. 인터프리터 패턴 (Interpreter pattern)

### 클라이언트-서버 패턴
클라이언트로부터 요청이 들어오면 서버는 요청에 맞는 서비스를 제공

### MVC 패턴
MVC 패턴은 하나의 소프트웨어를 역할에 따라 Model, View, Controller 세 가지의 파트로 나눠서 개발하는 패턴입니다.
Model : 데이터를 저장, 보관
View : 사용자에게 보여지는 부분을 담당
Controller : 사용자의 입력을 받아서 내부 로직을 처리

MVT VS MVC?

#### 정적파일(static files)
웹 페이지를 렌더링하는 과정에서 필요한 추가적인 파일

```
{% load staic %}
```
탬플릿 태그 : static에 있는 정적 파일을 현재 이 템플릿 파일에서 사용한다고 알려주는 것

### 템플릿 언어
#### 템플릿 변수
우리가 지정한 데이터로 변환
view에서 넘겨 받은 값으로 변환
`{{변수명}}`
`{{템플릿.속성}}` : 템플릿 변수는 점(.)을 사용해서 변수 안쪽 속성에 접근할 수 있습니다.

#### 템플릿 필터 
템플릿 변수를 특정 형식으로 변환
`{{변수명|필터}}`
예시) default, capfirst, random, upper&lower, ljust&rjust

#### 템플릿 태그
템플릿 작성에 로직을 사용
`{% 태그 %}` `{% end태그 %}`
예시) for, if, with

#### 템플릿 주석
템플릿 언어의 주석 처리를 담당
`{# 주석 #}`

### 템플릿 상속
`{% block %}`
`{% extends %}`

## Django의 URL 처리
### URLconf (urls.py)
Django에서 URL을 처리하기 위해서는 URLconf 모듈 즉 urls.py를 작성해야 합니다. 아래는 URLconf의 예시입니다.
```
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('URL', views.view)
]
```
### URL 처리 순서
1. 처음 요청이 들어오면 Django는 맨 처음 사용할 URLConf 모듈을 찾습니다. 따로 변경하지 않았다면 프로젝트 앱 내 settings.py의 ROOT_URLCONF 설정을 사용합니다.
2. ROOT_URLconf로 정의된 URLConf 모듈을 보고 urlpatterns 리스트 안쪽의 django.urls.path() 함수를 순서대로 실행합니다.
3. 요청과 일치하는 URL 패턴이 있다면 django.urls.path() 함수에 따라 view를 호출하거나, 일치하는 URL 패턴 다음의 URL을 하위 URLconf 모듈로 넘깁니다.

### Path 함수 알아보기
```
django.urls.path

path(route, view, kwargs=None, name=None)
```
#### route
: URL 문자열을 인수로 받으며 경로 변수(Path Converter)를 사용하여 URL의 일부를 view의 인수로 보낼 수 있습니다.

**Path converters**
- str : 경로 구분 기호(/)를 제외한 모든 문자열과 매칭됩니다.
- int : 0 또는 양의 정수와 매칭됩니다.
- slug : 문자, 숫자, 하이픈(-), 밑줄(_)로 구성된 문자열과 매칭됩니다.
- uuid : 범용 고유 식별자(UUID)와 매칭 됩니다. 
- path : 경로 구분 기호(/)를 포함한 모든 문자열과 매칭 됩니다.


#### view
: 함수형 view 또는 클래스 기반 view가 들어갈 수 있고 우리가 위에서 적어준 것처럼 include를 사용해서 다른 URLconf 모듈로 연결할 수도 있습니다.

#### kwargs
: view에 추가 인자를 전달 할 때 사용 합니다.

#### name
: path 함수가 가지는 URL 패턴에 이름을 붙여 주기 위해 사용하는데 URL을 직접 템플릿에 적지 않게 해주고 URL을 직관적으로 참조할 수 있게 해줍니다.

## 상태코드(Status Code)
- 요청에 대한 처리 결과가 어떻게 되었는지 알려주는 코드
- 크게 5가지로 구성
### 1xx `informational` 
: 요청을 받아서 작업 중
- 100 (진행, Continue)
요청의 첫 부분을 받아서 다음 요청을 기다리고 있다는 것을 알려 줍니다. 이미 요청을 완료했다면 해당 응답을 무시할 수 있습니다.
- 101 (프로토콜 전환, Switching Protocol)
클라이언트가 서버에게 프로토콜 전환을 요청했고 서버에서 프로토콜을 변경한다는 것을 나타냅니다.

### 2xx `success` 
: 요청에 대한 처리 결과가 정상
- 200 (성공, OK)
클라이언트의 요청이 성공적으로 처리되었다는 것을 의미하며 주로 요청한 페이지를 서버가 제공했다는 것을 알려줍니다.
- 201 (작성됨, Created)
요청이 성공적으로 처리되어 새로운 리소스를 생성했다는 것을 의미합니다
- 202 (허용됨, Accepted)
서버가 성공적으로 요청을 받았지만 아직 처리 전인 상태를 나타냅니다.
- 203 (신뢰할 수 없는 정보, Non-Authoritative Information)
서버가 성공적으로 요청을 처리했지만 요청에 포함된 정보가 다른 곳에서 수정된 정보라는 것을 나타냅니다.
- 204 (콘텐츠 없음, No Content)
요청을 성공적으로 처리했지만 콘텐츠를 제공하지 않는다는 것을 의미합니다.
- 205 (콘텐츠 재설정, Reset Content)
요청을 성공적으로 처리했고 콘텐츠를 제공하지 않으며 클라이언트가 문서 보기를 재설정할 것을 요구합니다.

### 3xx `redirection` 
: 요청을 완료하기 위해 추가적인 동작 필요
- 300 (여러 개의 선택 항목, Multiple Choice)
요청에 대해 서버가 여러 응답이 가능하며 하나를 선택해야 함을 나타냅니다.
- 301 (영구 이동, Moved Permanently)
요청한 리소스가 새로운 위치로 영구 이동했음을 나타냅니다. 클라이언트는 자동적으로 새로운 위치로 전달됩니다.
- 302 (임시 이동, Found)
요청한 리소스가 일시적으로 이동했음을 나타내며 향후 다시 해당 리소스를 요청할 때도 동일한 주소로 해야 한다는 것을 알려줍니다.
- 304 (수정되지 않음, Not Modified)
마지막 요청 이후 요청한 리소스는 수정되지 않았다는 것을 알려주며 서버가 콘텐츠를 전달하지 않습니다. 클라이언트는 이전에 전달받은 결과를 계속해서 사용할 수 있습니다.

### 4xx `client error` 
: 클라이언트의 요청에 문제가 있음
- 400 (잘못된 요청, Bad Request)
클라이언트의 요청을 서버가 이해할 수 없다는 것을 의미합니다.
- 401 (권한 없음, Unauthorized)
클라이언트가 해당 요청에 대한 응답을 받기 위해서는 추가적인 인증이 필요하다는 것을 나타냅니다.
- 402 (결제 필요, Payment Required)
이 요청을 결제가 필요하다는 것을 의미하며 처음 이 응답 코드가 만들어질 당시에는 결제 시스템에 사용할 목적이었으나 현재는 사용되고 있지 않습니다.
- 403 (금지됨, Forbidden)
클라이언트가 요청한 리소스에 접근할 권한이 없음을 의미합니다. 401과 다른 점은 서버는 해당 클라이언트에 대한 정보를 가지고 있다는 점입니다.
- 404 (찾을 수 없음, Not Found)
클라이언트가 요청한 리소스를 서버가 찾을 수 없다는 것을 의미합니다.

### 5xx `server error` 
: 서버가 요청을 처리하는 과정에서 문제 발생
- 500 (내부 서버 오류, Internal Server Error)
서버에서 오류가 발생하여 요청한 작업을 수행할 수 없다는 것을 의미합니다.
- 501 (구현되지 않음, Not Implemented)
클라이언트가 요청한 방법을 서버에서 수행할 수 있는 기능이 없다는 것을 의미합니다.
- 502 (잘못된 게이트웨이, Bad Gateway)
서버가 요청을 처리하는데 필요한 작업 중 게이트웨이로부터 잘못된 응답을 받았다는 것을 의미합니다.
- 503 (서비스를 사용할 수 없음, Service Unavailable)
서버가 해당 요청을 처리할 준비가 되지 않았으며 일반적으로는 유지관리를 위해 작동이 중단되거나 과부하가 걸렸을 때를 나타내며 대개 일시적입니다.