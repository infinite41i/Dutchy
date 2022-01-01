import uuid

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField()
    wallet = models.BigIntegerField(default=0)



class Group(models.Model):
    group_members = models.ManyToManyField(User, related_name="group_members", related_query_name="group_members")
    name = models.CharField(max_length=256)
    uuid = models.UUIDField(auto_created=uuid.uuid4())
    image = models.ImageField()
    description = models.TextField()

    def count_user(self):
        return self.group_members.all().count()


class Factor(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    factor_members = models.ManyToManyField(User, related_name="factor_members")
    description = models.TextField()
    factor_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="factor_owner",
                                     related_query_name="factor_owner")
    time = models.DateTimeField(auto_now_add=True)
    factor_group = models.ForeignKey(Group, on_delete=models.CASCADE)

    @property
    def divided_price(self):
        return self.factor_members.all().count()+1


