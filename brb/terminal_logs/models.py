from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Log(models.Model):
    """Log Model
    Stores terminal logs in the db
    """
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'[Log model] {self.content}'
