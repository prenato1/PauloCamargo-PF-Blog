from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE, verbose_name="Remetente")
    recipient = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE, verbose_name="Destinatário")
    subject = models.CharField(max_length=200, verbose_name="Assunto")
    body = models.TextField(verbose_name="Corpo da Mensagem")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Data de Envio")
    is_read = models.BooleanField(default=False, verbose_name="Lida")

    def __str__(self):
        return f"De: {self.sender} Para: {self.recipient} - {self.subject}"

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"
