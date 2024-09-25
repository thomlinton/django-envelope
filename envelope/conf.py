from django.conf import settings


HONEYPOT_FIELD_NAME = getattr(settings, "HONEYPOT_FIELD_NAME", "email2")
