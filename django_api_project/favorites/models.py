from django.db import models
from django.contrib.auth.models import User

class FavoriteCharacter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character_id = models.IntegerField()
    name = models.CharField(max_length=100)
    image_url = models.URLField()

    class Meta:
        unique_together = ('user', 'character_id')

    def __str__(self):
        return f"{self.user.username}'s favorite: {self.name}"