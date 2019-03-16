from pretix.base.email import TemplateBasedMailRenderer


class FSPMailRenderer(TemplateBasedMailRenderer):
    verbose_name = 'FSP Mail Vorlage'
    identifier = 'fspmail'
    thumbnail_filename = 'pretix_fsp_mail/thumb.png'
    template_name = 'pretix_fsp_mail/fsp_plainwrapper.html'
