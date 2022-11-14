from django.test import TestCase
import inspect

from myapp.models import TODOList
from myapp.utils import send_test_csv_report

from django.contrib.auth.models import User
from rest_framework.test import APIClient,APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
# Create your tests here.

TEST_RESULTS = []

class TODOListTestCase(APITestCase):
    def setup(self)->None:
        self.user = User.objects.create_user(username='test_user',password='adminpass')
        self.other_user = User.objects.create_superuser(username='other_user',password='adminpass')
        self.task = TODOList.objects.create(user = self.user,title = 'MY Initial Task')
        self.client = APIClient()

    @classmethod
    def tearDownClass(cls):
        User.objects.filter(username__in = ['test_user','other_user']).delete()

    def tes_create_task_with_un_authenticate_user(self):

        response = self.client.post(reverse('todo'),{'title':'My Task 1'},format = 'json')
        is_passed = response.status_code == status.HTTP_403_FORBIDDEN
        TEST_RESULTS.append({
            'result':"Passed" if is_passed else "Failed",
            "test_name":inspect.currentframe().f_code.co_name,
            "test_description": "Un_authenticated user cannot add a task into the TODO List"
        })

    def test_get_other_user_detail(self):

        self.client.login(username = 'other_user',password = 'adminpass')
        response = self.client.get(reverse('todo-detail',args=[str(self.task.id)]))
        is_passed = response.status_code == status.HTTP_403_FORBIDDEN

        TEST_RESULTS.append({
            'result':"Passed" if is_passed else "Failed",
            "test_name":inspect.currentframe().f_code.co_name,
            "test_description": "Only the Owner can view the Task Detail"
        })

    def test_create_task_with_authenticated_user(self):
        self.client.login(username = 'test_user',password = 'adminpass')
        response = self.client.post(reverse('todo'),{'title':'My Task'},format = 'json')
        is_passed = response.status_code == status.HTTP_201_CREATED

        TEST_RESULTS.append({
            'result':"Passed" if is_passed else "Failed",
            "test_name":inspect.currentframe().f_code.co_name,
            "test_description": "Task added into the TODO List Successfully"
        })

    def test_get_task_detail(self):
        self.client.login(username = 'test_user',password = 'adminpass')
        response = self.client.get(reverse('todo-detail',args=[str(self.task.id)]))
        is_passed = response.status_code == status.HTTP_200_OK

        TEST_RESULTS.append({
            'result':"Passed" if is_passed else "Failed",
            "test_name":inspect.currentframe().f_code.co_name,
            "test_description": "Task Detail retrieved Successfully"
        })

class CSVReportTest(APITestCase):
    def test_send_csv(self):
        send_test_csv_report(test_results=TEST_RESULTS)