# 📒[위코드 x 원티드] 백엔드 프리온보딩 선발 과제 <br>
### 📍 과제개요
- 글 작성, 글 확인, 글 목록 확인, 글 수정, 글 삭제가 되는 API<br>
- Delete과 Update는 해당 유저의 글만 가능/유저 생성, 인가, 인증 기능<br>
- pagination 구현 필수<br>
- sqlite3 사용<br>
- Unit Test 구현<br>

### 📍 사용 기술 스택
- Python & Django

##### ❗️ Reference
- 본 과제는 저작권의 보호를 받으며, 문제에 대한 정보를 배포하는 등의 행위를 금지 합니다. 
___
### 📍 구현 방법 및 이유
#### 사용자(user)
- 회원가입 : 이메일 중복확인 & 이메일과 비밀번호 유효성검사  & 비밀번호 암호화
- 로그인 : jwt 토큰 사용하여 인증&인가 기능구현

#### 게시판(post)
- 회원 사용 가능 기능<br> 
-- 게시글 작성: jwt토큰과 로그인 데코레이터 함수를 사용하여 사용자 확인 후 사용가능<br> 
-- 게시글 수정 & 삭제 : 해당 유저의 게시물에만 접근 권한이 있음<br> 
- 비회원 사용 가능 기능 : 게시글 조회 
___
### 📍 endpoint 호출방법
| METHOD | endpoint               | body 입력                     | 기능      |
|:------:|:----------------------:|------------------------------|----------|
| POST   | /users/signup          | name, email, password.       | 회원가입    |
| POST   | /users/login           | email, password              | 로그인     |
| POST   | /posts/postdetail      | subjects, contents           | 게시글 작성 |
| GET    | /posts/postdetail      |                              | 게시글 조회 |
| GET    | /posts                 |                              | 게시글 리스트|
| POST   | /posts/postupdate      | post_id, subjects, contents  | 게시글 수정 |
| POST   | /posts/postdelete      |                              | 게시글 삭제 |
___
### 📍 API 명세
#### 1.회원가입
- method  : POST
- endpoint: users/signup
- request

| 항목        | 데이터 형      | 예시                             | 비고                                 |
|:----------:|:------------:|:-------------------------------|-------------------------------------|
| name       | string       | "name" : "사용자1"               |                                     |
| email      | string       | "email" : "user1@wanted.com"   |`@`와 `.`이 들어간 이메일 형식.            |
| password   | string       | "password": "abcde12345@"      | 8자리 이상. `특수문자`, `숫자`, `영어` 포함 |

- request example
```bash
request POST 'http://127.0.0.1:8000/users/signup'
{
    "name" : "사용자1", 
    "password": "abcde12345@",
    "email" : "user1@wanted.com"
}
```

- response example
```bash
{
    "MESSAGE": "SUCCESS"
}
```

#### 2.로그인
- method  : POST
- endpoint: users/login
- request

| 항목        | 데이터 형      | 예시                             | 비고  |
|:----------:|:------------:|:-------------------------------|-------|
| email      | string       | "email" : "user1@wanted.com"   |       |
| password   | string       | "password": "abcde12345@"      |       |

- request example
```bash
request POST 'http://127.0.0.1:8000/users/login'
{
    "email": "user1@wanted.com",
    "password": "abcde12345@"
}
```

- response example
```bash
{
    "MESSAGE": "SUCCESS",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NH0.Tg-BvO4H1Gl2kFNDAEgkU5EaitRovdUAXaIoR6KdrQ0"
}
```

#### 3.게시글 작성
- method   : POST 
- endpoint : /posts/postdetail
- request

| 항목      | 데이터 형  | 예시                      | 비고  |
|:--------:|:--------:|:-------------------------|-----|
| subjects | string   |"subjects": "제목1"        |     |
| contents | string   | "contents" : "내용1"      |     |

- request example
```bash
request POST 'http://127.0.0.1:8000/posts/postdetail'
{
    "subjects": "제목1",
    "contents" : "내용1"
}
```
- response example
```
{
  "MESSAGE": "SUCCESS"
}
```

#### 4.게시글 조회

- method  : GET 
- endpoint : /posts/postdetail
- request

| 항목  | 데이터 형 | 예시  | 비고  |
|:-----:|:-------:|:-----|-----|
| id  | int   | post_id=11 |     |

- request example
```bash
request GET 'http://127.0.0.1:8000/posts/postdetail?post_id=11'

```
- response example
```
{
    "results": {
        "time": "2021-10-20 04:05:23",
        "subjects": "제목1",
        "contents": "내용1",
        "author": "사용자1"
    }
}
```

#### 5.게시글 리스트 조회
- method   : GET 
- endpoint : /posts
- request

| 항목      | 데이터 형 | 예시        | 비고  |
|:--------:|:-------:|:-----------|-----|
| offset   | int     | ?offset=4 |     |
| limit    | int     | ?limit=2  |     |

- request example
```bash
request GET 'http://127.0.0.1:8000/posts?limit=2&offset=4'

```
- response example
```
{
    "results": {
        "count": 2,
        "data": [
            {
                "time": "2021-10-20 04:10:52",
                "subjects": "제목2",
                "author": "사용자1"
            },
            {
                "time": "2021-10-20 04:11:03",
                "subjects": "제목3",
                "author": "사용자1"
            }
        ]
    }
}
```

#### 6.게시글 수정
- method  : POST 
- endpoint : /posts/postupdate
- request

| 항목      | 데이터 형 | 예시                   | 비고  |
|:--------:|:-------:|:----------------------|-----|
| post_id  | int     | "post_id": 11         |     |
| subjects | str     | "subjects" : "새로운제목"|     |
| contents | str     |"contents" : "새로운내용" |     |

- request example
```bash
request POST 'http://127.0.0.1:8000/posts/postupdate'
{
    "post_id": 11,
    "subjects" : "새로운제목",
    "contents" : "새로운내용"
}

```
- response example
```
{
    "MESSAGE": "SUCCESS"
}
```

#### 7.게시글 삭제
- mehtod  : POST 
- endpoint : /posts/postdelete
- request

| 항목  | 데이터 형  | 예시  | 비고  |
|:-----:|:-------:|:-----|-----|
| id  | int       |  /11 |     |

- Request example
```bash
request POST 'http://127.0.0.1:8000/posts/postdelete/11'
```
- Response example
```
{
    "MESSAGE": "SUCCESS"
}
```
