# from unittest import TestCase
#
# from django.contrib.auth.models import User
#
# from users.models import DeliveryAddress
#
#
# class TestModelDeliveryAddress(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         # Set up non-modified objects used by all
#         # test methods
#         DeliveryAddress.objects.create(
#             user=User.objects.create(username='vasa'),
#             region="ВО",
#
#             city='ВРН',
#             street='4545645645',
#             phone='4545645645',
#             # organisation=DeliveryAddress.objects.create(id=1),
#
#         )
#
#     def test_region_label(self):
#         profile = DeliveryAddress.objects.get(id=1)
#         field_label = profile._meta.get_field('region').verbose_name
#         self.assertEqual(field_label, 'Область')
#
#     # def test_telegram_length(self):
#     #     profile = DeliveryAddress.objects.get(id=1)
#     #     max_length = profile._meta.get_field('telegram').max_length
#     #     self.assertEqual(max_length, 15)
