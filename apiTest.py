import unittest
import requests

class TestYourAPI(unittest.TestCase):
    def testRegisterUser(self):
        #註冊成功
        api_endpoint = "http://127.0.0.1:5000/register"
        json_data = {
            "password": "passwd",
            "username": "alan",
            "email": "123@gmail.com"
        }
        response = requests.post(api_endpoint, json=json_data)
        data = response.json()
        self.assertEqual(data, "register success")

        #註冊失敗
        api_endpoint = "http://127.0.0.1:5000/register"
        json_data = {
            "password": "wrongpasswd",
            "username": "alan",
            "email": "user1@example.com"
        }
        response = requests.post(api_endpoint, json=json_data)
        data = response.json()
        self.assertEqual(data, "User already exist")
    # 測試登入
    def testLoginUser(self):
        # 登入失敗1
        api_endpoint = "http://127.0.0.1:5000/login"
        json_data = {
            "email": "wrong@gmail.com",
            "password": "passwd"
        }
        response = requests.get(api_endpoint, json=json_data)
        data = response.json()
        self.assertEqual(data, "this email isn't register yet")
        #登入失敗2
        json_data = {
            "email": "user1@example.com",
            "password": "wrongpasswd"
        }
        response = requests.get(api_endpoint, json=json_data)
        data = response.json()
        self.assertEqual(data, "login failed")
        
        #登入成功
        json_data = {
            "email": "user1@example.com",
            "password": "password1"
        }
        response = requests.get(api_endpoint, json=json_data)
        data = response.json()
        self.assertEqual(data, "login success")
if __name__ == "__main__":
    unittest.main()
