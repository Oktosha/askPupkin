from django.core.management.base import BaseCommand
from questions.models import UserWithAvatar, Tag, Question
from django.core.files.images import ImageFile
import os
from django.utils import timezone

class Command(BaseCommand):
    help = 'Fills the database with dummy data'
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent dictum lacinia tincidunt. Quisque scelerisque nisl sed arcu tristique, vel vestibulum magna congue. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed porttitor nunc id tempor gravida. Nullam non dui id felis lacinia pulvinar eu eget justo. Suspendisse luctus porttitor ultrices. Suspendisse tincidunt eleifend sapien, aliquam dapibus ligula consectetur eget. Morbi auctor justo quis arcu malesuada, eget rhoncus neque bibendum. Phasellus nec tortor ac lorem auctor condimentum. Duis venenatis felis eget ex finibus, viverra interdum sem vulputate. Fusce bibendum placerat urna nec vestibulum. Maecenas aliquet hendrerit lorem sed commodo. Nullam accumsan semper enim maximus vestibulum. Aenean vel interdum leo. Donec id orci pharetra, consequat dolor nec, tristique metus. Pellentesque molestie a sem ac varius."

    def create_user(self, username, avatar):
        user = UserWithAvatar.objects.create_user(username, 'dkolodzey@ya.ru', '123')
        image = ImageFile(open('../avatars/' + str(avatar) + '.jpg', 'rb'))
        user.avatar.save('ava.jpg', image)
        user.save()

    def create_tag(self, tagname):
        tag = Tag(name=tagname)
        tag.save()

    def create_question(self, name):
        user = UserWithAvatar.objects.order_by('?')[0]
        pub_date = timezone.now()
        title = "Could you help me with " + name + "?"
        text = self.lorem
        tags = Tag.objects.order_by('?')[:5]
        question = Question(author=user, pub_date=pub_date, text=text, title=title)
        question.save()
        for tag in tags:
            question.tags.add(tag)
        question.save()

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
