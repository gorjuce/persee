from django.db import models


class Project(models.Model):
    """ A project is a startup definition. """
    title = models.CharField(max_length=125)
    presentation = models.TextField(blank=True)
    start_date = models.DateField(null=True)

    def __str__(self):
        return self.title


class Program(models.Model):
    """ Programs are a specification of grand nancy innovation, a french incubator. Each mentored project is related
    to a dedicated program. """
    title = models.CharField(max_length=125)

    def __str__(self):
        return self.title
