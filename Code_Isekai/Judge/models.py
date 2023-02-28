from django.db import models

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
    lang = models.IntegerField(choices=LANGUAGE_ID)
    code = models.TextField()
