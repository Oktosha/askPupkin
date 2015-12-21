from django.core.management.base import BaseCommand
from questions.models import UserWithAvatar
from django.core.files.images import ImageFile
import os

class Command(BaseCommand):
    help = 'Fills the database with dummy data'

    def create_user(self, username, avatar):
        user = UserWithAvatar.objects.create_user(username, 'dkolodzey@ya.ru', '123')
        image = ImageFile(open('../avatars/' + str(avatar) + '.jpg', 'rb'))
        user.avatar.save('ava.jpg', image)
        user.save()
        return

    def add_arguments(self, parser):
        parser.add_argument('n_users', type=int)

    def handle(self, *args, **options):
        for i in range(options['n_users']):
            self.create_user('user' + str(i), str(i % 5))
        return