# From the scratch!  
>사실 첫번째 파일을 날려먹어서 다시 하는 중입니다..  
>이 파일은 정말 처음으로 장고 프로젝트를 시작하려는 시점 부터 참고하시면 됩니다!  
  
## 가상환경 만들고 활성화하기  
``` python 
$python3 -m venv myvenv  
  
  
#맥기준 
$source myvenv/bin/activate  
  
  
#윈도우는 아마 myvenv/Scripts/activate 일거에요!  
```  
이렇게 하시면, myvenv 라는 가상환경 폴더가 생기게 됩니다!  
`ls`와 같은 명령어로 자신의 폴더 상황을 점검하는 것도 추천드립니다!  

## 장고 설치  
```python  
$pip install django  
````
  
## 새로운 프로젝트 시작하기  
```python  
$django-admin startproject 프로젝트이름  
````  
이렇게 하면 프로젝트 폴더 하나가 생성됩니다!  
myvenv 파일과 같은 파일에 설치되어야합니다!!!  
myvenv 파일 '안에' 설치가 되어서는 **안됩니다**  

  
## 경로이동의 중요성  
잠시 **경로이동** 에 대한 잔소리를 하고 넘어가겠습니다.  
계속해서 `ls` 혹은 `pwd` 를 통해서 자신의 현재 위치를 확인해야하는 이유는,  
**폴더의 경로가 섞이지 않게 하기 위해서** 그리고 **필요한 파일을 동작시키기 위해서**입니다.  
  
예를 들어 지금부터는 새로 생성된 플젝 파일 안에 있는 `manage.py` 파일을 이용하여 app 을 만들고, 서버를 키는 등의 동작을 할 것입니다.  
이렇게 `manage.py` 파일을 작동시키기 위해서는 **자기 자신이 `manage.py` 파일이 있는 폴더 안**에 있어야 하는게 중요하겠죠!  
  
그러니 바깥에서 새로운 프로젝트 파일을 만들었으니,  
이제 `manage.py` 를 이용해 **새로운 앱**을 만들어야합니다.  
그리고 새로운 앱을 만들게 해주는 `manage.py` 가 들어있는 프로젝트 파일 **안**으로 들어가야합니다!  
  
이 부분을 많은 분들이 헷갈려하셔서 작성합니다 :D  
폴더 안으로 들어가는 방법:  
```python  
$cd 폴더이름  
```  
  
## 새로운 앱 만들기  
새로운 앱은 **프로젝트파일 안**에서 생성됩니다.  
앱은 프로젝트에서의 다양한 기능들을 대표해줍니다. 예를 들어 블로그 프로젝트에는 '나의 소개'앱, '포트폴리오'앱, 등이 있을 수 있겠죠!  
  
```python  
$python3 manage.py startapp 앱이름  
``` 
  
## 새로운 앱 등록하기  
**절대 잊어버려서는 안되는 단계**입니다!  
새로운 앱을 만들었다면 **무조건** 프로젝트에게 '새로운 앱을 만들었다' 라는 것을 알려야합니다.  
따라서 프로젝트의 `settings.py` 에서 app을 추가해주는 코드를 작성합니다.  
  
```python  
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'start_django.apps.StartDjangoConfig', ##추가한 코드
]  
``` 
저는 start_django 라는 새로운 앱을 만들어서 위와 같이 써주었습니다.  
이름을 어떤곳에서 대문자로 쓰고, 소문자로 써야하는지는 터미널 창에서 에러가 나면 자세히 알려주기 때문에 잘 읽어보면서 에러를 해결해나가길 바랍니다.  
이렇게 하면 새로운 프로젝트와 앱까지 구현이 됩니다! 
  
## MTV 간단하게 구현해보기  
Model-Templates-View 개념은 잘 이해하셨겠죠? 잘 이해가 안되셨다면 구글링 고고!  
저는 보통 아래와 같이 작업을 합니다.  
1. 앱에 `templates 폴더` 만들어주기  
2. 그 안에 화면에 띄울 `.html파일` 만들어주기  
3. `views.py`에 새로 만든 템플릿들 띄우는 함수 작성하기  
4. `urls.py`에 경로 추가해주기  
5. `$python3 manage.py runserver`  

**3번**에 해당하는 함수는 다음과 같습니다.  
```python  
#프로젝트.앱.views.py
def home(request):
    return render(request, 'home.html')  
  
#새로운 html 파일을 추가한다면 그 아래에 하나 더 추가해주면 됩니다!  
def profile(request):
    return render(request, 'profile.html')  
```  
**4번**에 대항하는 코드는 다음과 같습니다.  
```python  
#프로젝트.프로젝트폴더.urls.py  
from django.contrib import admin
from django.urls import path
import start_django.views  ##추가된 코드

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start_django.views.home, name="home"), ##추가된 코드 
    path('profile/', start_django.views.profile, name="profile"), ##추가된 코드 
```  
