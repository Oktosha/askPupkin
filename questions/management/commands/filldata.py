from django.core.management.base import BaseCommand
from questions.models import UserWithAvatar, Tag, Question, Answer, Like
from django.core.files.images import ImageFile
from django.contrib.contenttypes.models import ContentType
import os
from django.utils import timezone

class Command(BaseCommand):
    help = 'Fills the database with dummy data'
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    def create_user(self, username, avatar):
        user = UserWithAvatar.objects.create_user(username, 'dkolodzey@ya.ru', '123')
        image = ImageFile(open('../avatars/' + str(avatar) + '.jpg', 'rb'))
        user.avatar.save('ava.jpg', image)
        user.save()

    def create_tag(self, tagname):
        tag = Tag(name=tagname)
        tag.save()

    def create_question(self, name):
        user = UserWithAvatar.objects.order_by('?')[:1][0]
        pub_date = timezone.now()
        title = "Could you help me with " + name + "?"
        text = self.lorem * 10
        tags = Tag.objects.order_by('?')[:5]
        question = Question(author=user, pub_date=pub_date, text=text, title=title)
        question.save()
        for tag in tags:
            question.tags.add(tag)
        question.save()

    def create_answer(self, name):
        question = Question.objects.order_by('?')[:1][0]
        author = UserWithAvatar.objects.order_by('?')[:1][0]
        pub_date = timezone.now()
        text = self.lorem
        answer = Answer(question=question, author=author, pub_date=pub_date, text=text)
        answer.save()

    def create_like_to_question(self):
        question = Question.objects.order_by('?')[:1][0]
        user = UserWithAvatar.objects.order_by('?')[:1][0]
        ct = ContentType.objects.get_for_model(question)
        object_id = question.id
        like, is_created = Like.objects.get_or_create(object_id=object_id, content_type=ct,
            author=user)
        like.is_enabled = True
        like.save()

    def create_like_to_answer(self):
        answer = Answer.objects.order_by('?')[:1][0]
        user = UserWithAvatar.objects.order_by('?')[:1][0]
        ct = ContentType.objects.get_for_model(answer)
        object_id = answer.id
        like, is_created = Like.objects.get_or_create(object_id=object_id, content_type=ct,
            author=user)
        like.is_enabled = True
        like.save()

    def set_right_answers(self):
        for question in Question.objects.all():
            answer = Answer.objects.filter(question=question).order_by('?')[:1][0]
            answer.is_right = True
            answer.save()

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
