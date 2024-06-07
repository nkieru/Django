from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rating = models.IntegerField(default=0)

    def update_rating(self):
        p_rating = self.post_set.aggregate(models.Sum('p_rating')).get('p_rating__sum')
        c_rating = self.user.comment_set.aggregate(models.Sum('c_rating')).get('c_rating__sum')
        p_c_rating = self.post_set.aggregate(models.Sum('comment__c_rating')).get('comment__c_rating__sum')
        if not(isinstance(p_rating, int)):
            p_rating = 0
        if not(isinstance(c_rating, int)):
            c_rating = 0
        if not(isinstance(p_c_rating, int)):
            p_c_rating = 0
        self.user_rating = (p_rating * 3) + c_rating + p_c_rating
        self.save()

class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)


class Post(models.Model):

    news = 'N'
    article = 'A'

    TYPE = [
        (news, 'Новость'),
        (article, 'Статья')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=TYPE, default=news)
    date_time = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='Post_Category')
    header = models.CharField(max_length=255)
    text = models.TextField()
    p_rating = models.IntegerField(default=0)

    def like_post(self):
        self.p_rating += 1
        self.save()

    def dislike_post(self):
        self.p_rating -= 1
        self.save()

    def preview(self):
        return self.text[:124] + '...'

    def get_absolute_url(self):
        return f'/news/{self.id}'


class Post_Category(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    date_time_comment = models.DateTimeField(auto_now_add=True)
    c_rating = models.IntegerField(default=0)

    def like_comment(self):
        self.c_rating += 1
        self.save()

    def dislike_comment(self):
        self.c_rating -= 1
        self.save()