from django.db import models



class Article(models.Model):
    author_name = models.CharField(max_length=80)
    article_tag = models.CharField(max_length=50)
    article_title = models.CharField(max_length=200)
    article_content = models.TextField()

    def __str__(self):
        return self.article_title[0:20]