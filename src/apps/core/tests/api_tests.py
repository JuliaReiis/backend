# from rest_framework.test import APITestCase
# from rest_framework import status
# from django.urls import reverse
# from ..models.model import Company, Doc, User

# class CompanyAPITests(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create(email="test@example.com", password="123456")
#         self.client.force_authenticate(user=self.user)

#     def test_create_company(self):
#         url = reverse('company-list-create')
#         data = {'name': 'Test Company'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Company.objects.count(), 1)
#         self.assertEqual(Company.objects.get().name, 'Test Company')

#     def test_get_company_list(self):
#         Company.objects.create(name='Company 1', created_by=self.user)
#         Company.objects.create(name='Company 2', created_by=self.user)
#         url = reverse('company-list-create')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 2)
