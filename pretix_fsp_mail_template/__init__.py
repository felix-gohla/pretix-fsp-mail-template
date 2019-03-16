from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class PluginApp(AppConfig):
    name = 'pretix_fsp_mail_template'
    verbose_name = 'FSP Mail Template'

    class PretixPluginMeta:
        name = ugettext_lazy('FSP Mail Template')
        author = 'Felix Gohla'
        description = ugettext_lazy('Das Plugin beinhaltet eine E-Mail Vorlage für den FSP Ticketshop.')
        visible = True
        version = '1.0.0'

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'pretix_fsp_mail_template.PluginApp'
