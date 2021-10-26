
from django.conf import settings
from string import ascii_letters, digits
from random import choice

URL_SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)
ALL_CHARS = ascii_letters + digits


def gen_text(chars=ALL_CHARS):
    return "".join(
        [choice(chars) for _ in range(URL_SIZE)]
    )


def gen_url(model_instance):
    generated_text = gen_text()
    model_class = model_instance.__class__

    # create new url if the generated already exists
    if model_class.objects.filter(shortened_url=generated_text).exists():
        return gen_url(model_instance)

    return generated_text
