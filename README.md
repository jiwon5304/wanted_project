# ๐[์์ฝ๋ x ์ํฐ๋] ๋ฐฑ์๋ ํ๋ฆฌ์จ๋ณด๋ฉ ์ ๋ฐ ๊ณผ์  <br>
### ๐ ๊ณผ์ ๊ฐ์
- ๊ธ ์์ฑ, ๊ธ ํ์ธ, ๊ธ ๋ชฉ๋ก ํ์ธ, ๊ธ ์์ , ๊ธ ์ญ์ ๊ฐ ๋๋ API<br>
- Delete๊ณผ Update๋ ํด๋น ์ ์ ์ ๊ธ๋ง ๊ฐ๋ฅ/์ ์  ์์ฑ, ์ธ๊ฐ, ์ธ์ฆ ๊ธฐ๋ฅ<br>
- pagination ๊ตฌํ ํ์<br>
- sqlite3 ์ฌ์ฉ<br>
- Unit Test ๊ตฌํ<br>

### ๐ ์ฌ์ฉ ๊ธฐ์  ์คํ
- Python & Django

##### โ๏ธ Reference
- ๋ณธ ๊ณผ์ ๋ ์ ์๊ถ์ ๋ณดํธ๋ฅผ ๋ฐ์ผ๋ฉฐ, ๋ฌธ์ ์ ๋ํ ์ ๋ณด๋ฅผ ๋ฐฐํฌํ๋ ๋ฑ์ ํ์๋ฅผ ๊ธ์ง ํฉ๋๋ค. 
___
### ๐ ๊ตฌํ ๋ฐฉ๋ฒ ๋ฐ ์ด์ 
#### ์ฌ์ฉ์(user)
- ํ์๊ฐ์ : ์ด๋ฉ์ผ ์ค๋ณตํ์ธ & ์ด๋ฉ์ผ๊ณผ ๋น๋ฐ๋ฒํธ ์ ํจ์ฑ๊ฒ์ฌ  & ๋น๋ฐ๋ฒํธ ์ํธํ
- ๋ก๊ทธ์ธ : jwt ํ ํฐ ์ฌ์ฉํ์ฌ ์ธ์ฆ&์ธ๊ฐ ๊ธฐ๋ฅ๊ตฌํ

#### ๊ฒ์ํ(post)
- ํ์ ์ฌ์ฉ ๊ฐ๋ฅ ๊ธฐ๋ฅ<br> 
-- ๊ฒ์๊ธ ์์ฑ: jwtํ ํฐ๊ณผ ๋ก๊ทธ์ธ ๋ฐ์ฝ๋ ์ดํฐ ํจ์๋ฅผ ์ฌ์ฉํ์ฌ ์ฌ์ฉ์ ํ์ธ ํ ์ฌ์ฉ๊ฐ๋ฅ<br> 
-- ๊ฒ์๊ธ ์์  & ์ญ์  : ํด๋น ์ ์ ์ ๊ฒ์๋ฌผ์๋ง ์ ๊ทผ ๊ถํ์ด ์์<br> 
- ๋นํ์ ์ฌ์ฉ ๊ฐ๋ฅ ๊ธฐ๋ฅ : ๊ฒ์๊ธ ์กฐํ 
___
### ๐ endpoint ํธ์ถ๋ฐฉ๋ฒ
| METHOD | endpoint               | body ์๋ ฅ                     | ๊ธฐ๋ฅ      |
|:------:|:----------------------:|------------------------------|----------|
| POST   | /users/signup          | name, email, password.       | ํ์๊ฐ์    |
| POST   | /users/login           | email, password              | ๋ก๊ทธ์ธ     |
| POST   | /posts/postdetail      | subjects, contents           | ๊ฒ์๊ธ ์์ฑ |
| GET    | /posts/postdetail      |                              | ๊ฒ์๊ธ ์กฐํ |
| GET    | /posts                 |                              | ๊ฒ์๊ธ ๋ฆฌ์คํธ|
| POST   | /posts/postupdate      | post_id, subjects, contents  | ๊ฒ์๊ธ ์์  |
| POST   | /posts/postdelete      |                              | ๊ฒ์๊ธ ์ญ์  |
___
### ๐ API ๋ช์ธ
#### 1.ํ์๊ฐ์
- method  : POST
- endpoint: users/signup
- request

| ํญ๋ชฉ        | ๋ฐ์ดํฐ ํ      | ์์                             | ๋น๊ณ                                  |
|:----------:|:------------:|:-------------------------------|-------------------------------------|
| name       | string       | "name" : "์ฌ์ฉ์1"               |                                     |
| email      | string       | "email" : "user1@wanted.com"   |`@`์ `.`์ด ๋ค์ด๊ฐ ์ด๋ฉ์ผ ํ์.            |
| password   | string       | "password": "abcde12345@"      | 8์๋ฆฌ ์ด์. `ํน์๋ฌธ์`, `์ซ์`, `์์ด` ํฌํจ |

- request example
```bash
request POST 'http://127.0.0.1:8000/users/signup'
{
    "name" : "์ฌ์ฉ์1", 
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

#### 2.๋ก๊ทธ์ธ
- method  : POST
- endpoint: users/login
- request

| ํญ๋ชฉ        | ๋ฐ์ดํฐ ํ      | ์์                             | ๋น๊ณ   |
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

#### 3.๊ฒ์๊ธ ์์ฑ
- method   : POST 
- endpoint : /posts/postdetail
- request

| ํญ๋ชฉ      | ๋ฐ์ดํฐ ํ  | ์์                      | ๋น๊ณ   |
|:--------:|:--------:|:-------------------------|-----|
| subjects | string   |"subjects": "์ ๋ชฉ1"        |     |
| contents | string   | "contents" : "๋ด์ฉ1"      |     |

- request example
```bash
request POST 'http://127.0.0.1:8000/posts/postdetail'
{
    "subjects": "์ ๋ชฉ1",
    "contents" : "๋ด์ฉ1"
}
```
- response example
```
{
  "MESSAGE": "SUCCESS"
}
```

#### 4.๊ฒ์๊ธ ์กฐํ

- method  : GET 
- endpoint : /posts/postdetail
- request

| ํญ๋ชฉ  | ๋ฐ์ดํฐ ํ | ์์  | ๋น๊ณ   |
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
        "subjects": "์ ๋ชฉ1",
        "contents": "๋ด์ฉ1",
        "author": "์ฌ์ฉ์1"
    }
}
```

#### 5.๊ฒ์๊ธ ๋ฆฌ์คํธ ์กฐํ
- method   : GET 
- endpoint : /posts
- request

| ํญ๋ชฉ      | ๋ฐ์ดํฐ ํ | ์์        | ๋น๊ณ   |
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
                "subjects": "์ ๋ชฉ2",
                "author": "์ฌ์ฉ์1"
            },
            {
                "time": "2021-10-20 04:11:03",
                "subjects": "์ ๋ชฉ3",
                "author": "์ฌ์ฉ์1"
            }
        ]
    }
}
```

#### 6.๊ฒ์๊ธ ์์ 
- method  : POST 
- endpoint : /posts/postupdate
- request

| ํญ๋ชฉ      | ๋ฐ์ดํฐ ํ | ์์                   | ๋น๊ณ   |
|:--------:|:-------:|:----------------------|-----|
| post_id  | int     | "post_id": 11         |     |
| subjects | str     | "subjects" : "์๋ก์ด์ ๋ชฉ"|     |
| contents | str     |"contents" : "์๋ก์ด๋ด์ฉ" |     |

- request example
```bash
request POST 'http://127.0.0.1:8000/posts/postupdate'
{
    "post_id": 11,
    "subjects" : "์๋ก์ด์ ๋ชฉ",
    "contents" : "์๋ก์ด๋ด์ฉ"
}

```
- response example
```
{
    "MESSAGE": "SUCCESS"
}
```

#### 7.๊ฒ์๊ธ ์ญ์ 
- mehtod  : POST 
- endpoint : /posts/postdelete
- request

| ํญ๋ชฉ  | ๋ฐ์ดํฐ ํ  | ์์  | ๋น๊ณ   |
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
