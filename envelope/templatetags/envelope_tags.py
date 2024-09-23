# -*- coding: utf-8 -*-
"""
Template tags related to the contact form.
"""

from __future__ import unicode_literals

from django import template

import honeypot

register = template.Library()


# Register antispam_fields as an inclusion tag
@register.inclusion_tag('envelope/honeypot.html', takes_context=True)
def render_honeypot(context):
    return context


@register.inclusion_tag('envelope/contact_form.html', takes_context=True)
def render_contact_form(context):
    """
    Renders the contact form which must be in the template context.

    The most common use case for this template tag is to call it in the
    template rendered by :class:`~envelope.views.ContactView`. The template
    tag will then render a sub-template ``envelope/contact_form.html``.
    """
    if 'form' not in context:
        raise template.TemplateSyntaxError(
            "There is no 'form' variable in the template context."
        )
    return context
