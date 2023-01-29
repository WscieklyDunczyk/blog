from django.conf import settings
from django.db.models import *
from django.utils import timezone


class Post(Model):
    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    title = CharField(max_length=200)
    text = TextField()
    created_at = DateTimeField(default=timezone.now)
    published_date = DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title