import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# class Account(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.user.username
#     def get_account_id(self):
#         return self.id


class Game(models.Model):
    users = models.ManyToManyField(User)
    game_text = models.CharField(max_length=200)
    campaign_text = models.CharField(max_length=200)
    game_type = models.CharField(max_length=100)
    # participants = models.ManyToManyField(Account)
    creation_date = models.DateTimeField(('date created'), default=timezone.now)
    host_id = models.IntegerField()
    accepting_players = models.BooleanField(default=True)
    def __str__(self):
        return self.game_text
    def get_absolute_url(self):
        return reverse('group_finder:detail', kwargs={'pk': self.pk})



class Character(models.Model):
    name_text = models.CharField(max_length=50)
    player_text = models.CharField(max_length=30)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    def __str__(self):
        return self.name_text