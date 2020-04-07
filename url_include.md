
# URL 관리  
>너무 졸리지만 아기사자들을 생각하며 버틴다..  
>다들 잘 따라오고 있죠?!  
>복습을 위해 쓰기도 하지만 제가 강의하면서 혹시나 잊어버릴까봐 써놓기도 하는거랍니다..  

## 왜 URL 관리를 하는가?  
지금은 app이 한두개이지만, 더 많아진다면 url 들을 관리하기란 정말 힘든 일이다..  
지금의 `urls.py` 는 `프로젝트 파일` 안에 하나 밖에 없기 때문에, 많은 앱들의 템플릿들이 모두 섞여서 리스트로 적히게 된다.  
~~나중에 가면 정말 헷갈리게 될것이다...~~  

**따라서!!**  
1. APP 별로 `urls.py` 를 만들고 
2. `부모 urls.py` 에는 기존의 url 들을 지우고  
3. `부모 urls.py` 에 몇가지 코드만 추가해준다면  

우리는 **APP 별로 url 들을 추가** 해줄 수 있게 된다!  

## Stage1  
실습을 하던 `myapp` (또는 아무거나 자신의 APP) 에 `urls.py` 를 만들어준다.  
그리고 그 안에는 해당 app 에 관련된 url 들만 복사해서 넣어준다.  

예를 들어,  
``` python  

#myapp.urls.py  

from django.contrib import admin
from django.urls import path
import myapp.views
#or from .import views
#. 은 현재 폴더를 의미함 

urlpatterns = [
    path('',myapp.views.home, name="home"),
    path('profile/',myapp.views.profile, name="profile"),
]  
```
이렇게 추가를 한다.  

## Stage 2  
그러면 기존 `urls.py` 에 가서 필요 없는 것들은 지워준다.  
  
위의 예시로 치면,  
``` python  

path('',myapp.views.home, name="home"),
path('profile/',myapp.views.profile, name="profile"),
```
이 두줄을 `myproject.urls.py` 에서 지워주었다. 

## Stage 3  
이렇게만 두면 **절대 안된다**!!  
1. 기존 `urls.py` 에서 윗부분에 있는 줄에 `,include` 추가를 해야한다. 
``` python  
from django.urls import path, include
```  
2. 그리고 원래 path 가 있던 곳에 이것을 추가해준다.  
``` python  
path('', include('myapp.urls')),
```  
그러면 대충 이런식으로 `myproject.urls.py` 가 생겨먹게된다.  
  
  ``` python  
  #myproject.urls.py  
  
  from django.contrib import admin
from django.urls import path, include
import myapp.views
import portfolio.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('myphoto/',portfolio.views.myphoto, name="myphoto"),
]
```  

그러면! 모두 다 잘 될것이다!  
