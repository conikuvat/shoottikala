from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Message(models.Model):
    conversation = models.ForeignKey('shoottikala.Conversation')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL)
    body = models.TextField(
        verbose_name='Viesti',
        help_text='Viestin teksti näkyy vain sinulle ja keskustelun toiselle osapuolelle.'
    )

    shared_contact_details = models.ManyToManyField(
        'shoottikala.ContactDetail',
        blank=True,
        verbose_name='Jaa yhteystiedot',
        help_text='Sinä päätät, mitkä yhteystietosi jaat toisen osapuolen kanssa ja missä vaiheessa keskustelua.',
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
