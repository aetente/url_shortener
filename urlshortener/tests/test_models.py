from django.test import TestCase
from urlshortener.models import UrlModel

TEST_LINK = "https://ravkavonline.co.il"


class ModelsTestCase(TestCase):
    # test creating url
    def test_url_create(self):
        url_ent = UrlModel.objects.create(
            original_url=TEST_LINK)
        url_ent.save()
        # test have their own database, it is always empty on start
        # so we just need to check that there is one object created
        self.assertEqual(len(UrlModel.objects.all()), 1)
