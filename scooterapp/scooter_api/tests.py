from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse



'''
Тест на создания профиля, когда пользователь зарегистрировался,
то создается его личный профиль с номер id.
Например: profile/igor/1
'''
class ProfileTestOk(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = get_user_model().objects.create_user(
            first_name="Sarah", last_name='Green', email='sarah12@gmail.com', username="sarah_123", password='Yanifer96', city='Moscow', img='avatar/default.jpeg')

    def test_profile_ok(self):
        response = self.client.get(f"/profile/{self.user.id}")
        self.assertEqual(response.status_code, 200)


#Тест на ошибку 404 (страница не найдена)
class PageNotFoundTest(TestCase):

    def setUp(self):
        self.client = Client()


    def test_page_not_found(self):
        response = self.client.get('/main/')
        self.assertEqual(response.status_code, 404)

'''
Тест на доступ к dashboard. Если пользователь админ, то мы сможем получить доступ к странице,
если же пользователь не является админом, то нас перенаправит на страницу входа
'''
class DashboardTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_dashboard_access(self):
        self.client.post('/login/', {'username': "admin", 'password': 'admin'})
        response = self.client.get("/dashboard/")
        self.assertEqual(response.status_code, 200)
    
    def test_no_dashboard_access(self):
        self.client.post('/login/', {'username': "laba12", 'password': 'Yanifer96'})
        response = self.client.get("/dashboard/")
        self.assertTrue(response, '/login/')