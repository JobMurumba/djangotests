from django.test import TestCase
from django.utils import timezone
from whatever.models import Whatever


class WhateverTest(TestCase):

    def create_whatever(self,title="only a test",body="only a atest"):
        return Whatever.objects.create(name=title,body=body,creatd_at=timezone.now())
    
    def test_whatever_creation(self):
        w=self.create_whatever()
        self.assertTrue(isinstance(w,Whatever))
        self.assertEqual(w.__unicode__(),w.name)