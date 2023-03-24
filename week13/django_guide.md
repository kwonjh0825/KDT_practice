# 내가 작성해보는 Django 가이드

## Django 1일차 - 개발 환경설정 가이드 작성, 서버의 이해

### Django 개발 환경 설정 가이드

1. 가상 환경 생성
   - `python -m venv venv`를 통해 현재 경로에 venv라는 이름으로 가상환경 생성
2. 가상 환경 활성화
   - 터미널: 가상 환경(venv)가 있는 경로에서 `source venv/bin/activate` 명령 실행
   - vscode: select interpreter에서 가상 환경 경로의 python 선택
3. 가상환경에 Django 설치
   - `pip install django==3.2.18` 명령을 통해 설치
   - 특정 버전을 지정하여 설치할 수 있음
   - LTS 버전 설치 권장
4. (git을 활용할 경우) .gitignore 파일 작성
   - [gitignore.io](https://gitignore.io) 사이트 활용
5. (git을 활용할 경우) git 저장소 생성
   - `git init` 명령을 통해 저장소 생성
6. django 프로젝트 생성
   - `django-admin startproject project_name .` 를 통해 현재 경로에 django 프로젝트를 생성
7. django 서버 실행 
   - `python manage.py runserver` 를 통해 서버 실행
   - 브라우저에 해당 주소 입력 후 잘 실행되었는지 확인

### 서버의 이해

#### IP와 도메인은 무엇일까 ?

- IP
  - 인터넷 프로토콜의 약자로, 네트워크에서 정보통신에 대한 규약을 의미
  - IP address는 통신에 필요한 고유 주소
  - IP address는 숫자로 이루어져 있다. (ex. 192.168.0.1, 127.0.0.1 등)
- domain
  - IP address는 숫자로 이루어져 있기 때문에 사람이 읽기 힘든 단점이 있다.
  - domain은 IP address를 사람이 읽기 쉽도록 이름을 부여한 것이다.
  - 예를 들면 www.google.com 과 같이 언어로 작성된 주소 들이 도메인이라고 볼 수 있다.

#### 클라이언트와 서버는 무엇일까요 ?

- 클라이언트
  - 클라이언트는 인터넷을 사용하려는 사용자의 인터넷이 연결된 장치라고 할 수 있다.
  - 예를 들어, 인터넷이 연결된 PC, 무선 인터넷이 연결된 스마트폰과 같은 장치들이 클라이언트라고 할 수 있다.
  - 클라이언트의 특징
    - 클라이언트는 간혈적으로 연결된다.
    - 동적 ip 주소를 가질 수 있다.
- 서버
  - 서버는 웹 페이지, 사이트, 앱 등을 저장하고 있는 컴퓨터다.
  - 클라이언트가 웹 페이지에 접근하려고 하면, 서버는 클라이언트가 웹 페이지를 볼 수 있도록 웹 페이지를 불러와 클라이언트에게 제공한다.
  - 서버의 특징
    - always-on host(항상 켜져 있다)
    - 고정적인 ip 주소를 갖는다.

#### 정적 웹 사이트와 동적 웹 사이트의 차이점은 무엇일까요 ? Django 는 무엇을 위한 도구인가요 ?

- 정적 웹 사이트
  - 특별한 리소스 요청이 들어오면 서버에서 하드 코딩된 동일한 컨텐츠 반환
  - 사용자가 페이지를 탐색하거나 브라우저가 지정된 URL에 HTTP GET 요청을 보낼 때 서버는 요청한 문서를 검색하고 문제가 발생하지 않으면 success status를 포함한 HTTP 응답을 반환
- 동적 웹 사이트
  - 필요할 때에 동적으로 응답 컨텐츠가 생성됨
  - 사용자 또는 저장된 환경을 기반으로 URL에 대해 다른 데이터를 반환할 수 있으며, 응답을 반환하는 과정에서 다른 작업을 수행할 수 있음
  - 동적 웹사이트를 지원하는 코드는 서버에서 실행되어야 함. 이러한 코드를 작성하는 것은 server-side programming (backend scripting)이라 불림
- Django
  - django는 파이썬으로 작성된 오픈 소스 웹 프레임워크
  - 주된 목표는 고도의 데이터베이스 기반 웹 사이트를 작성할 때 수고를 더는 것
  - MVC 패턴(Model-View-Controller)를 따름
  - 풀 스택 프레임워크로 내장된 기능만을 통해 빠른 개발을 할 수 있도록 도와준다

#### HTTP는 무엇이고 요청과 응답 메시지 구성은 어떻게 되나요 ?

- HyperText Transfer Protocol의 약자로, 웹 상에서 정보를 주고 받을 수 있는 프로토콜
- 클라이언트와 서버 간 이루어지는 요청과 응답 프로토콜
- 요청의 구조
  - Method
    - 클라이언트가 수행하고자 하는 동작을 정의
    - GET, POST, HEAD 등
  - Path
    - 요청할 리소스의 경로
  - Version of protocol
    - HTTP 버전 작성
    - ex. HTTP/1.1
  - Headers
    - 서버에 대한 추가 정보
  - Body
    - POST 와 같은 특정 메서드에 존재
    - 데이터가 담겨 있는 부분
- 응답의 구조
  - Version of protocol
    - 요청에서의 Version of protocol과 동일
  - Stauts Code
    - 요청의 성공 여부와 이유를 나타 냄
  - Status Message
    - Status code를 설명해 주는 메시지
  - Headers
    - 요청과 비슷한 구조

#### 프레임워크는 무엇일까요 ?

- 간단하게 번역하면 뼈대, 골조 로 번역 가능
- 특정 목적을 달성하기 위해 복잡하게 얽힌 문제를 해결하기 위한 구조
- 프레임워크는 여러 기능을 가진 클래스와 라이브러리가 특정 결과물을 구현하고자 합쳐진 형태라고 볼 수 있음
- 각 기능을 보유한 라이브러리들을 한 데 묶어 담은 것이라고 볼 수 있음
- 예를 들면 웹 프레임워크는 웹 서버를 구현하기 위한 목적으로 만들어진 프레임워크

## Django 2일차 - 디자인 패턴, django project, app

### MVC 패턴

- Model(데이터베이스) - View(사용자 인터페이스) - Controller(비즈니스 로직)
- 애플리케이션을 구조화하는 대표적인 패턴
- 시각적 요소와 뒤에서 실행되는 로직을 서로 영향 없이 독립적이고 쉽게 유지보수 할 수 있는 애플리케이션을 만들기 위해 도입

### MTV 패턴

- Model - Template - View
- django에서 애플리케이션을 구조화하는 패턴
- 기존 MVC 패턴과 동일하지만 명칭을 다르게 정의

### Django project

- 애플리케이션의 집합
- DB 설정, URL 연결, 전체 앱 설정 등을 처리

### Django application

- 독립적으로 작동하는 기능 단위 모듈
- 각자 특정 기능을 담당하며 다른 앱들과 함께 하나의 프로젝트 구성
- `python manage.py startapp appname`을 통해 앱 생성 가능
- 앱 추가는 프로젝트 디렉터리 안 settings.py 파일 내에 INSTALLED_APPS 에 앱 이름을 작성

### URLs

- path 를 활용하여 url과 이에 해당하는 적절한 view를 연결
- 해당 app을 import 후 작성해야 함
- ex) `path('articles/', views.index)

### View

- View 파일에는 render 함수를 활용하여 HTTP request에 대한 respond 작성
- ex) 
  ```python
  def index(request):
    return render(request, 'index.html')
  ```

### Template

- 앱 디렉터리 안에 templates 폴더 생성
- templates 폴더 내에 템플릿 페이지 작성
- django 에서는 app/templates 이 기본 경로로 설정되어 있음

### 데이터 흐름에 따른 코드 작성

- URLs -> View -> Templates 순으로 작성하는 것을 권장

## Django 3일차 - Django Template System

### Django Template Language

- Template에서 조건, 반복, 변수, 필터 등의 프로그래밍적 기능을 제공하는 시스템

#### Sytnax

- Variable
  - view 함수에서 render의 세 번째 인자로 dictionary 타입으로 넘겨받을 수 있음
  - dictionary key 에 해당하는 문자열이 template 에서 사용 가능한 변수명이 됨
  - . 를 사용하여 변수 속성에 접근할 수 있음
  - `{{ varibale }}` 와 같이 사용 가능
- Filters
  - 표시할 변수를 수정할 때 사용
  - chained 가능
  - 일부 필터는 인자를 받기도 함
  - 약 60개의 built-in template filter
  - `{{ variable|filter }}` 와 같이 사용 가능
- Tags
  - 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 작업 수행
  - 일부 태그는 시작, 종료 태그 필요
  - 약 24개의 built-in template tag
  - `{% tag %}` 와 같이 사용 가능

### Template 상속

#### extends

- 자식(하위) 템플릿이 부모 템플릿을 확장하는 것을 알림
- 반드시 템플릿 최상단에 작성
- 2개 이상 사용 불가(2개 이상 상속 불가)
- `{% extends 'path' %}` 와 같이 사용

#### block

- 하위 템플릿에서 재정의(overridden)할 수 있는 블록 정의
- 하위 템플릿이 작성할 수 잇는 공간 제공
- `{% block name %} {% endblock name %}` 와 같이 사용

### 요청과 응답

#### form 

- 사용자로부터 할당된 데이터를 서버로 전송
- 웹에서 사용자 정보를 입력하는 여러 방식 제공

#### action, method

- form 의 핵심 속성 2가지
- 데이터를 어디(action)로 어떤 방식(method)으로 보낼지 결정
- action
  - 입력 데이터가 전송될 URL(목적지) 지정
  - 지정하지 않으면 데이터는 현재 form 이 있는 페이지의 URL로 전송됨
- method
  - 어떤 방식으로 보낼 지 결정
  - HTTP request method 지정(GET, POST)

#### input 

- 사용자의 입력을 받을 수 있는 요소
- type 속성값에 따라 다양한 유형의 입력 데이터를 ㅂ다음

#### name

- input 의 핵심 요소
- 데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터에 접근 가능

#### Query String Parameters

- 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 넘기는 방법
- 문자열은 `&` 로 연결된 `key=value` 쌍으로 구성되며, 기본 URL과 `&` 로 구분됨

#### request 객체

- form 을 통해 제출된 데이터는 HTTP request 객체에 들어 있음
- `request.GET`을 통해 dictionary 타입으로 받을 수 있음

## Django 4일차 - URL dispatcher

### 변수와 URL 

#### Variable Routing

- URL 일부에 변수를 포함시키는 것
- 변수는 view 함수의 인자로 전달할 수 있음
- `<path_converter:variable_name>`와 같이 작성
  - `path_converter`: type 지정(int, str 등)
  - `str` 타입 생략 가능, 하지만 명시적으로 작성 권장

### App과 URL

#### APP URL mapping

- 각 앱에 URL을 정의하는 것
- 프로젝트와 각각의 앱이 URL 을 나누어 관리하여 주소 관리를 편하게 하기 위함

#### inculde

- 다른 URL들을 참조할 수 있도록 돕는 함수
- URL의 그 시첨까지 일치하는 부분을 잘라내고 남은 문자열 부분을 후속 처리를 위해 include된 URL로 전달

### URL 이름 지정

#### Naming URL Patterns

- URL에 이름을 지정하는 것
- path 함수의 name  dlswkfmf wjddmlgotj tkdyd

#### `url` tag

- 주어진 URL 패턴의 일므과 일치하는 절대 경로 주소 반환
- `{% url 'url-name' arg1 arg2 ... %}` 와 같이 사용

## Django 5일차 - Django Model

### Django Model

- DB의 데이터를 정의하고 데이터를 조작할 수 있는 기능들 제공
- 테이블 구조를 설계하는 청사진(설계 도면)
- django.db.models 모듈의 Model 이라는 부모 클래스를 상속받아 작성
  - model 기능에 관련된 모든 설정이 담긴 클래스
  - 개발자가 테이블 구조 설계에만 집중할 수 있도록 하기 위함
  - 클래스 변수 명
    - 테이블 각 필드 이름 역할
  - model Field 메서드
    - 테이블 필드의 데이터 타입 역할
    - 키워드 인자: 제약 조건 관련 설정

### Migration

- model 클래스의 변경 사항을 DB에 최종 반영하는 방법

#### makemigrations

- model 클래스를 기반으로 설계도 작성

#### migrate

- 만들어진 설계도를 DB에 전달하여 반영

#### 추가 필드 작성

- 기존 테이블이 존재하기 때문에 필드를 추가할 때 필드의 기본 값 설정 필요
  - 1번 옵션은 직접 기본 값을 입력
  - 2번 옵션은 현재 대화 종료 후 models.py 에서 기본값 관련 설정
- 추가하는 필드의 기본 값 입력
  - django 가 제안하는 기본 값이 있다면 아무 것도 입력하지 않고 enter를 입력하면 제안된 기본값으로 설정됨
- model 클래스에 변경사항이 생겼다면 makemigrations, migrate를 통해 DB에 반영

### Field

#### CharField()

- 길이의 제한이 있는 문자열을 넣을 때 사용
- `max_length`: 필드의 최대 길이를 결정하는 필수 인자

#### TextField()

- 글자의 수가 많을 때 사용

#### DatetimeField()

- 날짜와 시간을 넣을 때 사용
- 선택 인자
  - `auto_now`
    - 데이터가 저장될 때마다 자동으로 현재 날짜, 시간 저장
    - update 에 적합
  - `auto_now_add`
    - 데이터가 처음 생성될 때만 자동으로 현재 날짜, 시간 저장
    - create 에 적합

### Admin site

#### Automatic admin interface

- django 는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스를 제공

#### admin 계정 생성 명령어

- `python manage.py createsuperuser`
- 유저 이름, 이메일, 비밀 번호 설정 가능
