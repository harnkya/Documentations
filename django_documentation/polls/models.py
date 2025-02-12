from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin

# create your models here


class Question(models.Model):
    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    @admin.display( # DECORATOR
        boolean=True,  # False ayarlansaydı direkt True, False ya da None yazardı
        ordering="pub_date",  # pub_date'e göre sıralıyor
        description="Published recently?",  # sütun adı, header, bu olsun diyor
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(
        max_length=200
    )  # choice_text gibi Field isimleri database'de tabloların sütunları olarak kullanılacak
    votes = models.IntegerField(default=0)


"""
Finally, note a relationship is defined, using ForeignKey. That tells Django each Choice is related to a single Question. Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.
"""
