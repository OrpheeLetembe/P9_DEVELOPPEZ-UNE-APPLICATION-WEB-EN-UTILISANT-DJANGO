
# from django.dispatch import receiver
# from django.core.exceptions import ValidationError
# from django.db.models.signals import pre_save
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models

from PIL import Image


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Ticket(BaseModel):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    reviewed = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (200, 200)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()


class Review(BaseModel):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(BaseModel):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following")
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followed_by")

    class Meta:
        unique_together = ('user', 'followed_user', )

    """
   @receiver(pre_save, sender=user)
    def check_self_following(sender, instance, **kwargs):
        if instance.follower == instance.user:
            raise ValidationError('You can not follow yourself')
    """