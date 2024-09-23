from django.urls import include, re_path

from envelope.views import ContactView


class SubclassedContactView(ContactView):
    pass


urlpatterns = [
    re_path(r'', include('envelope.urls')),
    re_path(r'^class_contact/', ContactView.as_view(), name='class_contact'),

    re_path(r'^customized_class_contact/',
        ContactView.as_view(
            success_url='customized_class_contact',
            template_name='customized_contact.html'
        ),
        name='customized_class_contact'
    ),

    re_path(r'^subclassed_class_contact/',
        SubclassedContactView.as_view(),
        name='subclassed_class_contact'
    ),
]
