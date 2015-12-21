from django.core.management.base import BaseCommand
from questions.models import UserWithAvatar, Tag
from django.core.files.images import ImageFile
import os

class Command(BaseCommand):
    help = 'Fills the database with dummy data'

    def create_user(self, username, avatar):
        user = UserWithAvatar.objects.create_user(username, 'dkolodzey@ya.ru', '123')
        image = ImageFile(open('../avatars/' + str(avatar) + '.jpg', 'rb'))
        user.avatar.save('ava.jpg', image)
        user.save()

    def create_tag(self, tagname):
        tag = Tag(name=tagname)
        tag.save()

    def create_question(self, name):
        pass

    def create_answer(self, name):
        pass

    def create_like_to_question(self):
        pass

    def create_like_to_answer(self):
        pass

    def set_right_answers(self):
        pass

    def add_arguments(self, parser):
        parser.add_argument('n_users', type=int)
        parser.add_argument('n_tags', type=int)
        parser.add_argument('n_questions', type=int)
        parser.add_argument('n_answers', type=int)
        parser.add_argument('n_likes_to_questions', type=int)
        parser.add_argument('n_likes_to_answers', type=int)

    def handle(self, *args, **options):
        self.n_users = options['n_users']
        self.n_tags = options['n_tags']
        self.n_questions = options['n_questions']
        self.n_answers = options['n_answers']
        self.n_likes_to_questions = options['n_likes_to_questions']
        self.n_likes_to_answers = options['n_likes_to_answers']

        for i in range(self.n_users):
            self.create_user('user' + str(i), str(i % 5))
        for i in range(self.n_tags):
            self.create_tag('tag' + str(i))
        for i in range(self.n_questions):
            self.create_question('question' + str(i))
        for i in range(self.n_answers):
            self.create_answer('answer' + str(i))
        for i in range(self.n_likes_to_questions):
            self.create_like_to_question()
        for i in range(self.n_likes_to_answers):
            self.create_like_to_answer()
        self.set_right_answers()
