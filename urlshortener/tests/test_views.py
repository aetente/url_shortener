from django.test import TestCase, Client
from urlshortener.models import UrlModel
from urlshortener.utils import gen_url


TEST_LINK = "https://google.com"


class ViewsTestCase(TestCase):
    # test redirects
    def test_redirect(self):
        c = Client()
        url_entity = UrlModel()
        url_entity.original_url = TEST_LINK

        # short url created on save
        short_url_ent = url_entity.save()
        shortened_url = short_url_ent.shortened_url
        response = c.get(
            "http://localhost:8000/s/"+shortened_url)
        self.assertRedirects(response, TEST_LINK,
                             status_code=302, fetch_redirect_response=False)

    # test non existing urls
    def test_non_existing_url(self):
        # it will generate a new url which we don't have
        non_existing_url = gen_url(UrlModel())
        response = self.client.get("localhost:8000/s/"+non_existing_url)
        self.assertEqual(response.status_code, 404)
