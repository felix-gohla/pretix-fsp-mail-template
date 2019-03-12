# Register your receivers here
from django.dispatch import receiver

from pretix.base.signals import register_html_mail_renderers

@receiver(register_html_mail_renderers, dispatch_uid="renderer_custom")
def register_mail_renderers(sender, **kwargs):
    from .email import FSPMailRenderer
    return FSPMailRenderer
