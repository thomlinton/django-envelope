from django.urls import include, re_path

from braces.views import FormMessagesMixin

from envelope.views import ContactView


class MessagesContactView(FormMessagesMixin, ContactView):
    form_invalid_message = "There was en error in the contact form."
    form_valid_message = "Thank you for your message."
    template_name = "envelope/messages_contact.html"


urlpatterns = [
    re_path(r"", include("envelope.urls")),
    re_path(
        r"^crispy/",
        ContactView.as_view(template_name="envelope/crispy_contact.html"),
        name="crispy-contact",
    ),
    re_path(r"^messages/", MessagesContactView.as_view(), name="messages-contact"),
]
