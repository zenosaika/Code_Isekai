from django.db import models
from django.conf import settings

class CodeEditor(models.Model):
    LANGUAGE_ID = (
        (50, "C"),
        (54, "C++"),
        (60, "Go"),
        (62, "Java"),
        (63, "JavaScript"),
        (74, "TypeScript"),
        (71, "Python"),
        (72, "Ruby"),
        (73, "Rust"),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lang = models.IntegerField(choices=LANGUAGE_ID, default=71)
    code = models.TextField(default='')
    token = models.CharField(max_length=255, default='')
    is_token_used = models.BooleanField(default=True)
    response = models.TextField(default='')
    stdout = models.TextField(default='')

    def __str__(self):
        return f'{self.user}'
