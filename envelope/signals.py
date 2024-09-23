"""
Signals sent by the application.
"""
from django.dispatch import Signal


before_send = Signal()
after_send = Signal()
