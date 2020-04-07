# 템플릿 상속  
>사실 나도 작년에 정말 어렵다고 느꼈고 끝까지 잘 이해하지 못했던 부분이다..  
>아무리 생각해도 올해 멋사 정말 친절 + 디테일한듯 ㅎㅎㅎㅎ   
>좋은 운영진들이 있기 때문이겠죠?ㅎㅎㅎ  

## 첫번째 할 일 
가장 상위의 project 폴더 안에 있는 Project 폴더 안에,
1. templates 폴더 하나를 만들고 
2. `base.html` 파일을 추가한다.   
말 그대로 base가 되는 html 파일을 만드는 개념이다.  

>>그리고 경로는 굉장히 중요하니, 잘 이해하고 만들었으면 한다.  
>>현재 우리는 다른 app 들의 templates 들을 통합하는 `'상위의 프로젝트 templates'폴더`를 만드는 것이기 때문에,  
>>다른 곳이 아닌 Project 폴더 안에 templates 폴더를 생성하는 것이다!  

## 두번째 할 일  
`settings.py`안에 `TEMPLATES` 부분에 아래를 추가한다.  
본래 DIRS 옆에는 공란이다.  

```
        'DIRS': ['myproject/templates'],
```
  
## 세번째 할 일  
겹치는 부분, 즉 ***모든 html 파일에 공통으로 적용할 부분***을 `base.html` 에 넣는다.  
예를 들어 우리는 `<head>` 부분과 `<footer>` 부분을 ***겹치는 부분***으로 두겠다.  

그렇게 되면, 현재 `base.html` 에는  
1. `<head>` 에 해당하는 내용  
2. `<footer>`에 해당하는 내용  
이렇게 두개만 붙여져 있다.  

이것에 추가해야 하는 내용은 ***공통된 부분 외에 추가되는 부분***이다.  
즉, <head> 와 <footer> 사이에 다른 페이지들에서 각각 다르게 보여지게 될 `<body>`부분을 아래와 같이 표시해둔다.  

``` python
#base.html  

<head>
    <title>멋사 8기 두번째 정기세션 HOME</title>
    <h1>멋사 8기 두번째 정기세션 HOME</h1>
</head>

<!-- body는 바뀔거라는 것을 아래 두줄로 알려줘야함 --!> 
<body>
{% block contents %}
{% endblock %}
</body>

    <footer>
        <h4><a href="{% url 'profile' %}">나의 정보 보러가기</a></h4>
        <h4><a href="https://github.com/minseungseon/starting_django">장고 실습 자료 보러가기</a></h4>
        <h4><a href="https://minseungseon.github.io/">선생님 블로그 보러가기</a></h4>
    </footer>
```
위에서 보았듯이, `base.html`에 바뀔 부분에는 
1. `{% block contents %}`   
2. `{% endblock %}`  
를 추가해야한다.  

## 마지막으로 해야할 일  
이제 `base.html`양식을 만들어 놓았으니, 
1. 공통된 부분들을 다른 html 파일에서는 ***지우고***  
2. `base.html`을 가져온다는 표시를 해주고,
2. `base.html`에서 다를거라고 표시했던 부분들을 다시한번 ***영역표시*** 해주어야한다.   
  
다른 html 파일에는 이런식으로 작성하면 된다.  
``` python  
#home.html  

<!-- base.html을 가져오겠다고 말해주기 -->
{% extends 'base.html' %}

<!-- base.html 과 다른 부분에는 앞뒤로 block 표시 해주기 -->
{%block contents%}

<h1>안녕하세요! 저는 선민승입니다.</h1>
<a href="{% url 'home' %}">홈으로 가기</a>
<a href="{% url 'myphoto' %}">내 사진 보기</a>

{% endblock %}
```
