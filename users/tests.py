import json

from django.test import TestCase, Client

from .models import User

class SignUpTest(TestCase):
    def setUp(self):
        User.objects.create(
            email="bbb@wecode.com",
            name="파이썬",
            password="abcde12345@",
        )

    def tearDown(self):
        User.objects.all().delete()
        
    def test_signup_success(self):
        client = Client()
        user = {
            "email": "aaa@wecode.com",
            "name": "깔끔한",
            "password": "abcde12345@",
        }
        response = client.post(
            "/users/signup", json.dumps(user), content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"MESSAGE": "SUCCESS"})

    def test_duplication_user(self):
        client = Client()
        user = {
            "email": "bbb@wecode.com",
            "name": "탄탄한",
            "password": "abcde12345@@",
        }
        response = client.post(
            "/users/signup", json.dumps(user), content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"MESSAGE": "ALREADY_EXISTED_EMAIL"})

    def test_email_format_error(self):
        client = Client()
        user = {
            "email": "cccwecode.com",
            "name": "파이썬",
            "password": "abcde12345@",
        }
        response = client.post(
            "/users/signup", json.dumps(user), content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"MESSAGE": "EMAIL_ERROR"})
    
    def test_password_format_error(self):
        client = Client()
        user = {
            "email": "ddd@wecode.com",
            "name": "파이썬",
            "password": "abcde12345",
        }
        response = client.post(
            "/users/signup", json.dumps(user), content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"MESSAGE": "PASSWORD_ERROR"})
    
    def test_key_error(self):
        client = Client()
        user = {
            "email": "eee@wecode.com",
            "name": "파이썬",
        }
        response = client.post(
            "/users/signup", json.dumps(user), content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"MESSAGE": "KEY_ERROR"})


class LoginTest(TestCase):
    def setUp(self):
        User.objects.create(
            id=3,
            email="fff@wecode.com",
            name="파이썬",
            password="$2b$12$GknwVYGZxyYbVnbUty4g/.rxFbpSgqwg4fEjPEmh3yCzEj8oxq4pW",
        )

    def tearDown(self):
        User.objects.all().delete()

    def test_email_error(self):
        client = Client()
        user = {
            "email": "abcde@wecode.com",
            "password": "abcde12345@",
        }
        response = client.post(
            "/users/login", json.dumps(user), content_type="application/json"
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"MESSAGE": "INVALID_USER"})

    def test_password_error(self):
        client = Client()
        user = {
            "email": "fff@wecode.com",
            "password": "aaaaaaaaa",
        }
        response = client.post(
            "/users/login", json.dumps(user), content_type="application/json"
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"MESSAGE": "INVALID_USER"})

    def test_login_success(self):
        client = Client()
        user = {
            "email": "fff@wecode.com",
            "password": "abcde12345@",
        }
        response = client.post(
            "/users/login", json.dumps(user), content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "MESSAGE": "SUCCESS",
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6M30.tpEToen_MCZcP_uTPBmouoh5YinCVOyg4bHgLnnOc2I",
            })
    
    def test_key_error(self):
        client = Client()
        user = {
            "email": "fff@wecode.com",
            
        }
        response = client.post(
            "/users/login", json.dumps(user), content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"MESSAGE": "KEY_ERROR"})






