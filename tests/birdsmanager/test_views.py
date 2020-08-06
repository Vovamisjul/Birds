import os, sys
from unittest.mock import patch

sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Birds.settings")  # or whatever
import django

django.setup()

from unittest import TestCase
from django.http import HttpRequest
from rest_framework.request import Request
from birdsmanager.models import Bird
from birdsmanager.views import BirdsView
from birdsmanager.serializers import BirdsSerializer


def mock_save():
    pass

class TestBirdsView(TestCase):

    def setUp(self):
        self.all_birds = [{"name": "A", "color": "red", "species": "sparrow", "body_length": 2, "wingspan": 5},
                          {"name": "B", "color": "black", "species": "pigeon", "body_length": 3, "wingspan": 4},
                          {"name": "C", "color": "red", "species": "sparrow", "body_length": 12, "wingspan": 1},
                          {"name": "D", "color": "black", "species": "pigeon", "body_length": 4, "wingspan": 2}]

        def mock_all():
            return self.all_birds

        Bird.objects.all = mock_all
        BirdsSerializer.save = lambda: None

    def test_get_all(self):
        http_request = HttpRequest()
        get_birds = BirdsView().get(Request(http_request))
        self.assertEqual(self.all_birds, get_birds.data)

    def test_get_by_offset(self):
        http_request = HttpRequest()
        http_request.GET['offset'] = '2'
        get_birds = BirdsView().get(Request(http_request))
        self.assertEqual(self.all_birds[2:], get_birds.data)

    def test_get_by_zero_offset(self):
        http_request = HttpRequest()
        http_request.GET['offset'] = '0'
        get_birds = BirdsView().get(Request(http_request))
        self.assertEqual(self.all_birds, get_birds.data)

    def test_get_by_invalid_offset(self):
        http_request = HttpRequest()
        http_request.GET['offset'] = 'as'
        get_birds = BirdsView().get(Request(http_request))
        self.assertEqual(self.all_birds, get_birds.data)

    def test_get_by_negative_offset(self):
        http_request = HttpRequest()
        http_request.GET['offset'] = '-1'
        get_birds = BirdsView().get(Request(http_request))
        self.assertEqual(self.all_birds, get_birds.data)

    def test_get_by_too_much_offset(self):
        http_request = HttpRequest()
        http_request.GET['offset'] = str(len(self.all_birds) + 1)
        get_birds = BirdsView().get(Request(http_request))
        self.assertEqual([], get_birds.data)

    def test_get_by_limit(self):
        http_request = HttpRequest()
        http_request.GET['limit'] = '2'
        get_birds = BirdsView().get(Request(http_request))
        self.assertEqual(self.all_birds[:2], get_birds.data)

    def test_get_by_negative_limit(self):
        http_request = HttpRequest()
        http_request.GET['limit'] = '-2'
        get_birds = BirdsView().get(Request(http_request))
        self.assertEqual(self.all_birds, get_birds.data)

    def test_get_by_invalid_limit(self):
        http_request = HttpRequest()
        http_request.GET['limit'] = 'as'
        get_birds = BirdsView().get(Request(http_request))
        self.assertEqual(self.all_birds, get_birds.data)

    def test_get_by_zero_limit(self):
        http_request = HttpRequest()
        http_request.GET['limit'] = '0'
        get_birds = BirdsView().get(Request(http_request))
        self.assertEqual([], get_birds.data)

    def test_get_by_offset_and_limit(self):
        http_request = HttpRequest()
        http_request.GET['offset'] = '1'
        http_request.GET['limit'] = '2'
        get_birds = BirdsView().get(Request(http_request))
        self.assertEqual(self.all_birds[1:3], get_birds.data)

    @patch('birdsmanager.serializers.BirdsSerializer.save', side_effect = mock_save)
    def test_post(self, MockBirdsSerializer):
        self.fail()