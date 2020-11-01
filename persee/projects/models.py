from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=125)
    program = models.ForeignKey(
        'program',
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Program(models.Model):
    title = models.CharField(max_length=125)

    def __str__(self):
        return self.title
