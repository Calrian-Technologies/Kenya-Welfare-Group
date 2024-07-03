from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError
from users.serializers import RegisterSerializer
from donations.models import CustomUser

class CustomUserManagerTests(TestCase):

    def setUp(self):
        self.user_data = {
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'first_name': 'Test',
            'last_name': 'User',
            'phone': '1234567890',
            'national_id': '12345678',
            'county': 'Nairobi',
            'country': 'Kenya'
        }

    def test_create_user_with_email_successful(self):
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertEqual(user.email, self.user_data['email'])
        self.assertTrue(user.check_password(self.user_data['password']))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(
                email='test@test.com',
                password='testpassword',
                first_name='Test',
                last_name='User',
                phone='1234567890',
                national_id='12345678',
                county='Nairobi',
                country='Kenya'
            )

    def test_create_superuser_successful(self):
        user = CustomUser.objects.create_superuser(**self.user_data)
        self.assertEqual(user.email, self.user_data['email'])
        self.assertTrue(user.check_password(self.user_data['password']))
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_superuser_without_is_staff_raises_error(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_superuser(
                email='testsuperuser@example.com',
                password='testpassword',
                first_name='Test',
                last_name='Superuser',
                phone='1234567890',
                national_id='12345678',
                county='Nairobi',
                country='Kenya',
                is_staff=False
            )

    def test_create_superuser_without_is_superuser_raises_error(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_superuser(
                email='testsuperuser@example.com',
                password='testpassword',
                first_name='Test',
                last_name='Superuser',
                phone='1234567890',
                national_id='12345678',
                county='Nairobi',
                country='Kenya',
                is_superuser=False
            )

class CustomUserModelTests(TestCase):

    def setUp(self):
        self.user_data = {
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'first_name': 'Test',
            'last_name': 'User',
            'phone': '1234567890',
            'national_id': '12345678',
            'county': 'Nairobi',
            'country': 'Kenya'
        }

    def test_string_representation(self):
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertEqual(str(user), user.email)

    def test_default_date_joined(self):
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertIsNotNone(user.date_joined)
        self.assertAlmostEqual(user.date_joined, timezone.now(), delta=timezone.timedelta(seconds=1))

    def test_unique_constraints(self):
        CustomUser.objects.create_user(**self.user_data)
        with self.assertRaises(ValidationError):
            user = CustomUser(**self.user_data)
            user.full_clean()
class RegisterSerializerTests(TestCase):

    def setUp(self):
        self.valid_data = {
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'first_name': 'Test',
            'last_name': 'User',
            'phone': '1234567890',
            'national_id': '12345678',
            'county': 'Nairobi',
            'country': 'Kenya'
        }
        self.invalid_data = {
            'email': 'invalid-email',
            'password': 'short',
            'first_name': '',
            'last_name': '',
            'phone': 'invalid-phone',
            'national_id': '',
            'county': '',
            'country': ''
        }

    def test_create_user_with_valid_data(self):
        serializer = RegisterSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.email, self.valid_data['email'])
        self.assertTrue(user.check_password(self.valid_data['password']))
        self.assertEqual(user.first_name, self.valid_data['first_name'])
        self.assertEqual(user.last_name, self.valid_data['last_name'])
        self.assertEqual(user.phone, self.valid_data['phone'])
        self.assertEqual(user.national_id, self.valid_data['national_id'])
        self.assertEqual(user.county, self.valid_data['county'])
        self.assertEqual(user.country, self.valid_data['country'])

    def test_create_user_with_missing_fields(self):
        invalid_data = self.valid_data.copy()
        invalid_data.pop('email')
        serializer = RegisterSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)

    def test_create_user_with_invalid_data(self):
        serializer = RegisterSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)
        self.assertIn('password', serializer.errors)
        self.assertIn('first_name', serializer.errors)
        self.assertIn('last_name', serializer.errors)
        self.assertIn('phone', serializer.errors)
        self.assertIn('national_id', serializer.errors)
        self.assertIn('county', serializer.errors)
        self.assertIn('country', serializer.errors)
