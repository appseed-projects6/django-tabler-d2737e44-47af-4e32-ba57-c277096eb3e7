# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Model_Table(models.Model):

    #__Model_Table_FIELDS__
    model_name = models.CharField(max_length=255, null=True, blank=True)

    #__Model_Table_FIELDS__END

    class Meta:
        verbose_name        = _("Model_Table")
        verbose_name_plural = _("Model_Table")


class Prediction_Table(models.Model):

    #__Prediction_Table_FIELDS__
    prediction_name = models.CharField(max_length=255, null=True, blank=True)
    prediction_type = models.CharField(max_length=255, null=True, blank=True)

    #__Prediction_Table_FIELDS__END

    class Meta:
        verbose_name        = _("Prediction_Table")
        verbose_name_plural = _("Prediction_Table")



#__MODELS__END
