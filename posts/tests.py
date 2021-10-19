import json, jwt

from django.test import TestCase, Client

from .models       import Post
from users.models  import User
from my_settings import SECRET_KEY, ALGORITHM


class PostDetailTest(TestCase):
    def setUp(self):
        User.objects.create(
            id=1,
            name="민트",
            email="mint@mint.com",
            password="abcde12345@",
        )
        User.objects.create(
            id=2,
            name="초코",
            email="choco@choco.com",
            password="abcde12345@",
        )
        Post.objects.create(
            id=1,
            author=User.objects.get(id=1),
            subjects="sb1",
            contents="ct1",
        )
        Post.objects.create(
            id=2,
            author=User.objects.get(id=1),
            subjects="sb2",
            contents="ct2",
        )
        Post.objects.create(
            id=3,
            author=User.objects.get(id=2),
            subjects="sb3",
            contents="ct3",
        )
        Post.objects.create(
            id=4,
            author=User.objects.get(id=2),
            subjects="sb4",
            contents="ct4",
        )

    def tearDown(self):
        Post.objects.all().delete()
        User.objects.all().delete()
    
    def test_create_post_success(self):
        access_token = jwt.encode(
            {"id": 1}, SECRET_KEY, ALGORITHM,
        )

        client = Client()
        header = {"HTTP_AUTHORIZATION": access_token}

        posting = {
            "subjects": "제목",
            "contents": "내용",
        }
        response = client.post(
            "/posts/postdetail", json.dumps(posting), **header, content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"MESSAGE": "SUCCESS"})

    def test_subjects_error(self):
        access_token = jwt.encode(
            {"id": 1}, SECRET_KEY, ALGORITHM,
        )

        client = Client()
        header = {"HTTP_AUTHORIZATION": access_token}

        posting = {
            "subjects": "",
            "contents": "내용",
        }
        response = client.post(
            "/posts/postdetail", json.dumps(posting), **header, content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"MESSAGE": "SUBJECTS_ERROR"})

    def test_contents_error(self):
        access_token = jwt.encode(
            {"id": 1}, SECRET_KEY, ALGORITHM,
        )

        client = Client()
        header = {"HTTP_AUTHORIZATION": access_token}

        posting = {
            "subjects": "제목",
            "contents": "",
        }
        response = client.post(
            "/posts/postdetail", json.dumps(posting), **header, content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"MESSAGE": "CONTENTS_ERROR"})

    def test_post_key_error(self):
        access_token = jwt.encode(
            {"id": 1}, SECRET_KEY, ALGORITHM,
        )

        client = Client()
        header = {"HTTP_AUTHORIZATION": access_token}

        posting = {
            "subjects": "제목",
        
        }
        response = client.post(
            "/posts/postdetail", json.dumps(posting), **header, content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"MESSAGE": "KEY_ERROR"})

    def test_get_success(self):
        client = Client()
        response = client.get("/posts/postdetail?post_id=1")

        updated_at = Post.objects.get(id=1).updated_at

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "results": {
                    "time": updated_at.strftime("%Y-%m-%d %H:%M:%S"),
                    "subjects": "sb1",
                    "contents": "ct1",
                    "author": "민트"
                }
            }
        )

    def test_post_error(self):
        client = Client()
        response = client.get("/posts/postdetail?post_id=20")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"MESSAGE": "POST_ERROR"})


class PostListTest(TestCase):
    def setUp(self):
        User.objects.create(
            id=1,
            name="민트",
            email="mint@mint.com",
            password="abcde12345@",
        )
        User.objects.create(
            id=2,
            name="초코",
            email="choco@choco.com",
            password="abcde12345@",
        )
        Post.objects.create(
            id=1,
            author=User.objects.get(id=1),
            subjects="sb1",
            contents="ct1",
        )
        Post.objects.create(
            id=2,
            author=User.objects.get(id=1),
            subjects="sb2",
            contents="ct2",
        )
        Post.objects.create(
            id=3,
            author=User.objects.get(id=2),
            subjects="sb3",
            contents="ct3",
        )
        Post.objects.create(
            id=4,
            author=User.objects.get(id=2),
            subjects="sb4",
            contents="ct4",
        )

    def tearDown(self):
        Post.objects.all().delete()
        User.objects.all().delete()


    def test_postlist_success(self):
        client = Client()
        response = client.get("/posts?limit=2&offset=0")

        updated_at1 = Post.objects.get(id=1).updated_at
        updated_at2 = Post.objects.get(id=2).updated_at

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "results": {
                    "count": 2,
                    "data": [
                        {
                            "time": updated_at1.strftime("%Y-%m-%d %H:%M:%S"),
                            "subjects": "sb1",
                            "author": "민트",
                        },
                        {
                            "time": updated_at2.strftime("%Y-%m-%d %H:%M:%S"),
                            "subjects": "sb2",
                            "author": "민트",
                        },
                    ],
                }
            },
        )


class PostUpdateTest(TestCase):
    def setUp(self):
        User.objects.create(
            id=1,
            name="민트",
            email="mint@mint.com",
            password="abcde12345@",
        )
        User.objects.create(
            id=2,
            name="초코",
            email="choco@choco.com",
            password="abcde12345@",
        )
        Post.objects.create(
            id=1,
            author=User.objects.get(id=1),
            subjects="sb1",
            contents="ct1",
        )
        Post.objects.create(
            id=2,
            author=User.objects.get(id=1),
            subjects="sb2",
            contents="ct2",
        )
        Post.objects.create(
            id=3,
            author=User.objects.get(id=2),
            subjects="sb3",
            contents="ct3",
        )
        Post.objects.create(
            id=4,
            author=User.objects.get(id=2),
            subjects="sb4",
            contents="ct4",
        )

    def tearDown(self):
        Post.objects.all().delete()
        User.objects.all().delete()


    def test_update_success(self):
        access_token = jwt.encode(
            {"id": 1}, SECRET_KEY, ALGORITHM,
        )

        client = Client()
        header = {"HTTP_AUTHORIZATION": access_token}

        posting = {
            "post_id" : 1,
            "subjects": "제목",
            "contents": "내용",
        }
        response = client.post(
            "/posts/postupdate", json.dumps(posting), **header, content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"MESSAGE": "SUCCESS"})
    
    def test_user_error(self):
        access_token = jwt.encode(
            {"id": 2}, SECRET_KEY, ALGORITHM,
        )

        client = Client()
        header = {"HTTP_AUTHORIZATION": access_token}

        posting = {
            "post_id" : 1,
            "subjects": "제목",
            "contents": "내용",
        }
        response = client.post(
            "/posts/postupdate", json.dumps(posting), **header, content_type="application/json"
        )

        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json(), {"MESSAGE": "INVALID_USER"})

    def test_subjects_error(self):
        access_token = jwt.encode(
            {"id": 1}, SECRET_KEY, ALGORITHM,
        )

        client = Client()
        header = {"HTTP_AUTHORIZATION": access_token}

        posting = {
            "post_id" : 1,
            "subjects": "",
            "contents": "내용",
        }
        response = client.post(
            "/posts/postupdate", json.dumps(posting), **header, content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"MESSAGE": "SUBJECTS_ERROR"})
    
    def test_contents_error(self):
        access_token = jwt.encode(
            {"id": 1}, SECRET_KEY, ALGORITHM,
        )

        client = Client()
        header = {"HTTP_AUTHORIZATION": access_token}

        posting = {
            "post_id" : 1,
            "subjects": "제목",
            "contents": "",
        }
        response = client.post(
            "/posts/postupdate", json.dumps(posting), **header, content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"MESSAGE": "CONTENTS_ERROR"})
    
    def test_post_error(self):
        access_token = jwt.encode(
            {"id": 1}, SECRET_KEY, ALGORITHM,
        )

        client = Client()
        header = {"HTTP_AUTHORIZATION": access_token}

        posting = {
            "post_id" : 100,
            "subjects": "제목",
            "contents": "내용",
        }
        response = client.post(
            "/posts/postupdate", json.dumps(posting), **header, content_type="application/json"
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"MESSAGE": "POST_ERROR"})

    def test_key_error(self):
        access_token = jwt.encode(
            {"id": 1}, SECRET_KEY, ALGORITHM,
        )

        client = Client()
        header = {"HTTP_AUTHORIZATION": access_token}
        posting = {
            "postid" : 1,
            "subject": "제목",
            "content": "내용",
        }
        response = client.post(
            "/posts/postupdate", json.dumps(posting), **header, content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"MESSAGE": "KEY_ERROR"})


class PostDeleteTest(TestCase):
    def setUp(self):
        User.objects.create(
            id=1,
            name="민트",
            email="mint@mint.com",
            password="abcde12345@",
        )
        User.objects.create(
            id=2,
            name="초코",
            email="choco@choco.com",
            password="abcde12345@",
        )
        Post.objects.create(
            id=1,
            author=User.objects.get(id=1),
            subjects="sb1",
            contents="ct1",
        )
        Post.objects.create(
            id=2,
            author=User.objects.get(id=1),
            subjects="sb2",
            contents="ct2",
        )
        Post.objects.create(
            id=3,
            author=User.objects.get(id=2),
            subjects="sb3",
            contents="ct3",
        )
        Post.objects.create(
            id=4,
            author=User.objects.get(id=2),
            subjects="sb4",
            contents="ct4",
        )

    def tearDown(self):
        Post.objects.all().delete()
        User.objects.all().delete()

    def test_delete_success(self):
        access_token = jwt.encode(
            {"id": 1}, SECRET_KEY, ALGORITHM,
        )

        client = Client()
        header = {"HTTP_AUTHORIZATION": access_token}
        response = client.post("/posts/postdelete/1", **header)

        self.assertEqual(response.status_code, 201)

    def test_user_error(self):
        access_token = jwt.encode(
            {"id": 2}, SECRET_KEY, ALGORITHM,
        )

        client = Client()
        header = {"HTTP_AUTHORIZATION": access_token}
        response = client.post("/posts/postdelete/1", **header)

        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json(), {"MESSAGE": "INVALID_USER"})

    def test_post_error(self):
        access_token = jwt.encode(
            {"id": 1}, SECRET_KEY, ALGORITHM,
        )

        client = Client()
        header = {"HTTP_AUTHORIZATION": access_token}
        response = client.post("/posts/postdelete/100", **header)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"MESSAGE": "POST_ERROR"})
