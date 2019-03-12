from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class PluginApp(AppConfig):
    name = 'pretix_fsp_mail'
    verbose_name = 'Mail Vorlage für Musikschule Fröhlich'

    class PretixPluginMeta:
        name = ugettext_lazy('Mail Vorlage für Musikschule Fröhlich')
        author = 'Felix Gohla'
        description = ugettext_lazy('Dieses Plugin beinhaltet eine E-Mail Vorlage für den FSP Ticket Shop.')
        visible = True
        version = '1.0.0'

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'pretix_fsp_mail.PluginApp'
