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

## 서버의 이해

### IP와 도메인은 무엇일까 ?

- IP
  - 인터넷 프로토콜의 약자로, 네트워크에서 정보통신에 대한 규약을 의미
  - IP address는 통신에 필요한 고유 주소
  - IP address는 숫자로 이루어져 있다. (ex. 192.168.0.1, 127.0.0.1 등)
- domain
  - IP address는 숫자로 이루어져 있기 때문에 사람이 읽기 힘든 단점이 있다.
  - domain은 IP address를 사람이 읽기 쉽도록 이름을 부여한 것이다.
  - 예를 들면 www.google.com 과 같이 언어로 작성된 주소 들이 도메인이라고 볼 수 있다.

### 클라이언트와 서버는 무엇일까요 ?

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

### 정적 웹 사이트와 동적 웹 사이트의 차이점은 무엇일까요 ? Django 는 무엇을 위한 도구인가요 ?

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

### HTTP는 무엇이고 요청과 응답 메시지 구성은 어떻게 되나요 ?

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

### 프레임워크는 무엇일까요 ?

- 간단하게 번역하면 뼈대, 골조 로 번역 가능
- 특정 목적을 달성하기 위해 복잡하게 얽힌 문제를 해결하기 위한 구조
- 프레임워크는 여러 기능을 가진 클래스와 라이브러리가 특정 결과물을 구현하고자 합쳐진 형태라고 볼 수 있음
- 각 기능을 보유한 라이브러리들을 한 데 묶어 담은 것이라고 볼 수 있음
- 예를 들면 웹 프레임워크는 웹 서버를 구현하기 위한 목적으로 만들어진 프레임워크