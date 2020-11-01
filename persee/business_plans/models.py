from django.db import models

from projects.models import Project


class BusinessPlan(models.Model):
    """ A business plan synthesizes all informations about a business from general strategy to financial overview """
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

