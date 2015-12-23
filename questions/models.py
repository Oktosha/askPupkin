from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.id, filename)

class UserWithAvatar(AbstractUser):
    avatar = models.ImageField(upload_to=user_directory_path, blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Like(models.Model):
    author = models.ForeignKey(UserWithAvatar)
    is_enabled = models.BooleanField(default=False)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        ans = str(self.author)
        if self.is_enabled:
            ans += " likes "
        else:
            ans += " "
        ans += str(self.content_type) + " " + str(self.object_id)
        return  ans


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(UserWithAvatar)
    tags = models.ManyToManyField(Tag)
    likes = GenericRelation(Like)

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
    is_right = models.BooleanField(default=False)
    likes = GenericRelation(Like)
    def __str__(self):
        return self.author.__str__() + " answers " + self.text[:50]

