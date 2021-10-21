from typing import Tuple
from django.db import models
from django.contrib.auth.models import User



class Account(User):
    
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username