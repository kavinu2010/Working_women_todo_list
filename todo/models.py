# todo/models.py

from django.db import models

class Task(models.Model):
    CATEGORY_CHOICES = [
        ('Personal', 'Personal'),
        ('Work', 'Work'),
        ('Health', 'Health'),
        ('Education', 'Education'),
        ('Home Maintenance', 'Home Maintenance'),
        ('Finance', 'Finance'),
        ('Others', 'Others'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Deferred', 'Deferred'),
    ]

    RECURRENCE_CHOICES = [
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
        ('Yearly', 'Yearly'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Others')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_recurring = models.BooleanField(default=False)
    recurrence_interval = models.CharField(max_length=10, choices=RECURRENCE_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.title
