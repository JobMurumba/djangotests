from django.test import TestCase
from django.utils import timezone
from whatever.models import Whatever
from django.utils import timezone
from django.urls import reverse
from  whatever import views
import  unittest
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from whatever.forms import WhateverForm
class WhateverTest(TestCase):
    
    def create_whatever(self,title="only a test",body="only a atest"):
        return Whatever.objects.create(name=title,body=body,creatd_at=timezone.now())
    
    def  test_whatever_list_view(self):
        w = self.create_whatever()
        url=reverse("whatever:thelist")
        resp=self.client.get(url)
        self.assertEqual(resp.status_code,200)
        self.assertIn(w.name.encode(),resp.content)

        
    def test_valid_form(self):
        w=Whatever.objects.create(name='foo',body='bar')
        data={'title':w.name,'body':w.body,}
        form=WhateverForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w=Whatever.objects.create(name='foo',body='')
        data={'title':w.name,'body':w.body,}
        form=WhateverForm(data=data)
        self.assertFalse(form.is_valid())

# class TestSignup(unittest.TestCase):
#     def setUp(self):
#         self.driver=webdriver.Firefox(executable_path=r'C:\Users\netflixSterling\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe')

#     def test_signup_fire(self):
#         self.driver.get("http://localhost:8000/tests/add/")
#         self.driver.find_element_by_id('id_name').send_keys("another test")
#         self.driver.find_element_by_id('id_body').send_keys("another test body")
#         self.driver.find_element_by_id('submit').click()
#         self.assertIn("http://localhost:8000",self.driver.current_url)
#     def tearDown(self):
#         self.driver.quit
# if __name__ =='__main__':
#     unittest.main()

class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(MySeleniumTests,cls).setUpClass()
        cls.selenium = WebDriver(executable_path=r'C:\Users\netflixSterling\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests,cls).tearDownClass()

    def test_signup_fire(self):
        self.selenium.get('%s%s' %(self.live_server_url, "/tests/add/"))
        self.selenium.find_element_by_id('id_name').send_keys("another test")
        self.selenium.find_element_by_id('id_body').send_keys("another test body")
        self.selenium.find_element_by_xpath('//input[@value="login"]').click()
        self.assertIn('%s' %(self.live_server_url),self.selenium.current_url)
        

