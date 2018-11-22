import datetime
from django.utils import timezone
from django.db import models
from enum import Enum
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

RATING_CHOICES = (
(1, "★☆☆☆☆☆☆☆☆☆"),
(2, "★★☆☆☆☆☆☆☆☆"),
(3, "★★★☆☆☆☆☆☆☆"),
(4, "★★★★☆☆☆☆☆☆"),
(5, "★★★★★☆☆☆☆☆"),
(6, "★★★★★★☆☆☆☆"),
(7, "★★★★★★★☆☆☆"),
(8, "★★★★★★★★☆☆"),
(9, "★★★★★★★★★☆"),
(10, "★★★★★★★★★★"),
)

class Publisher(models.Model):

    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=40)
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Author(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def __str__(self):
        return u'% s %s' % (self.first_name, self.last_name)



class Category(models.Model):
    name = models.CharField(max_length=100, default='abc1')
    slug = models.SlugField(max_length=100, unique=True)


    def __str__(self):
        return self.name


class Books(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='books',
                                 on_delete=models.CASCADE)
    title = models.CharField('Title',max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField(blank=True, null=True)
    book_type = models.IntegerField(choices=((1, ("Books")),
                                             (2, ("Video"))),
                                    default=1)
    series = models.TextField(max_length=250, null=True)
    level = models.TextField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, db_index=True, null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    isbn_no = models.TextField(max_length=250, null=True)
    features = models.TextField(max_length=250 , null=True)
    rating = models.PositiveIntegerField('Rating', choices=RATING_CHOICES, null=True, default=1)

    def get_absolute_url(self):
        return reverse('books:book_detail',
                            args=[self.id, self.slug])

    class Meta:
        ordering = ('-title',)
        index_together = (('id', 'slug'),)


    def __str__(self):
        return self.title

    def recent_Publication(self):
        return self.publication_date >= timezone.now().date() - datetime.timedelta(weeks=8)



class Comment(models.Model):
    book = models.ForeignKey(Books,
                             related_name='comments',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'comment by {} on {}'.format(self.name, self.book)



class CenterContentModel(models.Model):
    title = models.CharField(max_length=40)
    discription = models.TextField(max_length=250)
    call_to_action_value = models.URLField()
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    html_content = models.TextField(max_length=250)

    def __str__(self):
        return self.title

class MarketingContent(models.Model):

    title = models.CharField(max_length=50)
    html_content = models.TextField(max_length=250)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    sequence_no = models.IntegerField()

    def __str__(self):
        return self.title

class ScrollAbleContent(models.Model):
    title = models.CharField(max_length=50)
    html_content = models.TextField(max_length=250)

    def __str__(self):
        return self.title


