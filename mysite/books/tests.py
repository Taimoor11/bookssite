import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Publisher ,Books , Author


class modeltest(TestCase):

    def setUp(self):
        p1=Publisher.objects.create(name='abc', address='sa426', city='rwp',
                                 state='pubjab',country='pakistan',
                                 website='www.abc.com')
        p2=Publisher.objects.create(name='axyz', address='dk892', city='isb',
                                state='pubjab', country='pakistan',
                                website='www.xyz.com')
        a1=Author.objects.create(first_name='taimoor', last_name='arshad',
                              email='123@gmail.com')
        a2=Author.objects.create(first_name='taimoor', last_name='arshad',
                              email='123@gmail.com')
        b1=Books.objects.create(title='django', publication_date=datetime.date(2018, 9, 25), publisher=p2)
        b1.save()
        b1.authors.add(a1,a2)
        b1.save()



    def test_publisher_count(self):
        pubs = Publisher.objects.all()
        self.assertEqual(len(pubs),2)




    def test_author_countl(self):
        author_count = Author.objects.all()
        self.assertEqual(len(author_count),2)

    def test_recent_pub(self):
        futuredate = timezone.now().date() + datetime.timedelta(days=5)
        future_pub = Books(publication_date=futuredate)
        self.assertEqual(future_pub.recent_Publication(),True)

    def test_creation_author(self):
        w = Author.objects.filter(id=1)
        self.assertEqual(w[0].id,1)

    def test_verify_autgor(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.first_name,'taimoor')

    def test_verift_book(self):
        b2verify = Books.objects.get(id=1)
        self.assertTrue(isinstance(b2verify.publisher,Publisher))
        author_set = b2verify.authors.all()
        self.assertEqual(len(author_set),2)


    def test_verify_author_names(self):
        b1 = Books.objects.get(id=1)
        b1_authors = b1.authors.all()
        for item in b1_authors:
            self.assertGreaterEqual(len(item.first_name),1)











