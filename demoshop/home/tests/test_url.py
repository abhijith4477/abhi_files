from  django.test import SimpleTestCase
from  django.urls import reverse,resolve
from home.views import home,login_user,logout_user

class Testurls(SimpleTestCase):
    def test_home_url(self):
        url=reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func,home)

    def test_login_url(self):
        url=reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func,login_user)

    def test_logout_url(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout_user)


