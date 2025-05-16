import uuid

from django.core.validators import MinLengthValidator
from django.db import models
from django.conf import settings

# Create your models here.

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(
        validators=[MinLengthValidator(3, message="Task description is too short")],
    )
    OPTION_YES = 'Y'
    OPTION_NO = 'N'
    TIME_SENSITIVE_OPTIONS = [
        (OPTION_YES, 'Yes'),
        (OPTION_NO, 'No'),
    ]
    time_sensitive = models.CharField(max_length=1, choices=TIME_SENSITIVE_OPTIONS, default=OPTION_NO)
    time_to_complete = models.DateTimeField(null=True, blank=True,
                                            help_text="If time sensitive is yes then "
                                                      "enter time and date, else can leave blank"
                                            )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.description + str(self.author)
    class Meta:
        ordering = ['-created_at']