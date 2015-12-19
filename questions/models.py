from django.db import models
from django.contrib.auth.models import AbstractUser

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.id, filename)

class UserWithAvatar(AbstractUser):
    avatar = models.ImageField(upload_to=user_directory_path, blank=True)

class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(UserWithAvatar)

    def __str__(self):
        return self.author.__str__() + " asks " + self.title

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('questions:question', args=[str(self.id)])

class Answer(models.Model):
    text = models.TextField()
    author = models.ForeignKey(UserWithAvatar)
    pub_date = models.DateTimeField('date published')
    question = models.ForeignKey(Question)
    def __str__(self):
        return self.author.__str__() + " answers " + self.text[:50]

