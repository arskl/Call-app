from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    platform_choices = (
    ('macOS', 'macOS'),
    ('Windows', 'Windows'),
    )

    subscription_choices = (
    ('Premium', 'Premium'),
    ('Basic', 'Basic'),
    )

    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    platform = models.CharField(max_length=7, choices=platform_choices)
    subscription = models.CharField(max_length=8, null=True, blank=True, choices=subscription_choices)
    comment = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Call(models.Model):
    call_status = (
    ('Answered', 'Answered'),
    ('Missed', 'Missed'),
    )
    agent = models.ForeignKey(User, on_delete= models.SET('Unknown'), null=True, blank=True)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete= models.SET('Unknown'))
    number = models.CharField(max_length=11, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(max_length=8, choices=call_status, null=True, blank=True)
    comment = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        line = str(self.number) + ", " + str(self.customer)
        return line

    class Meta:
        ordering = ['-date']

class Task(models.Model):
    status_choices = (
    ('Completed', 'Completed'),
    ('Incompleted', 'Incompleted'),
    )

    title = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(max_length=11, choices=status_choices, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete= models.SET('Unknown'), null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
