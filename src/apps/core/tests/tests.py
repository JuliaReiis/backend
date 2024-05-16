# from django.test import TestCase
# from django.utils import timezone
# from backend.src.apps.core.models.model import Company, Doc, User

# class ModelTests(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(email="test@example.com", password="123456")
#         self.company = Company.objects.create(name="Test Company", created_by=self.user)
#         self.doc = Doc.objects.create(name="Test Document", company=self.company, created_by=self.user)

#     def test_company_creation(self):
#         company = Company.objects.get(name="Test Company")
#         self.assertEqual(company.locate, "-03:00")
#         self.assertEqual(company.lang, "pt")

#     def test_doc_creation(self):
#         doc = Doc.objects.get(name="Test Document")
#         self.assertEqual(doc.deleted, False)

#     def test_user_creation(self):
#         user = User.objects.get(email="test@example.com")
#         self.assertEqual(user.email_verified, False)
#         self.assertTrue(user.password)

#     def test_last_update_at_auto_update(self):
#         old_last_update_at = self.doc.last_update_at
#         self.doc.name = "Updated Document"
#         self.doc.save()
#         updated_doc = Doc.objects.get(name="Updated Document")
#         self.assertGreater(updated_doc.last_update_at, old_last_update_at)

#     def test_sign_document(self):
#         self.assertFalse(self.doc.signed)
#         self.doc.signed = True
#         self.doc.save()
#         self.assertTrue(self.doc.signed)
