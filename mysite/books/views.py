from django.shortcuts import render, get_object_or_404
from .models import Publisher, Books, Comment,Author,Category, ScrollAbleContent, MarketingContent, CenterContentModel, RATING_CHOICES
from django.http import Http404, HttpResponse
import datetime
from .forms import ContactForm, CommentForm, MovieFilterForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from tablib import Dataset
from django.conf import settings
from django.views.generic import ListView,DetailView,DeleteView, RedirectView

from .resources import BookResource
from django.conf import settings




# Create your views here.


@login_required
# def books_list(request):
#
#
#     b2 = Books.objects.all()
#
#     paginator = Paginator(b2, 4 )
#     page = request.GET.get('page')
#     try:
#         b1 = paginator.page(page)
#
#     except PageNotAnInteger:
#         b1 = paginator.page(1)
#     except EmptyPage:
#         b1 = paginator.page(paginator.num_pages)
#
#     return render(request,'books/movie_list.html',
#                    {'page':page,
#
#                     'b1':b1,
#
#                     }
#
#                 )

@login_required()
def books_list(request):
    qs = Books.objects.all()
    form = MovieFilterForm(data=request.GET)
    facets = {
        "selected": {},
        "categories": {
            "category": Category.objects.all(),
            "publishers": Publisher.objects.all(),
            "authors": Author.objects.all(),
            "ratings": RATING_CHOICES,
        }, }
    if form.is_valid():
        filters = (
            ("category", "category",),
            ("publisher", "directors",),
            ("author", "authors",),
            ("rating", "rating",),
        )
        qs = filter_facets(facets, qs, form, filters)
    if settings.DEBUG:
        # Let's log the facets for review when debugging
        import logging
        logger = logging.getLogger(__name__)
        logger.info(facets)
    context = {
        "form": form,
        "facets": facets,
        "object_list": qs,
    }
    return render(request, "books/movie_list.html", context)


def filter_facets(facets, qs, form, filters):
    for facet, key in filters:
        value = form.cleaned_data[facet]
        if value:
            selected_value = value
            if facet == "rating":
                rating = int(value)
                selected_value = (rating,dict(RATING_CHOICES)[rating])
                filter_args = {
                    f"{key}__gte": rating,
                    f"{key}__lt": rating + 1,
                }
            else:
                filter_args = {key: value}
            facets["selected"][facet] = selected_value
            qs = qs.filter(**filter_args).distinct()


    return qs



def search_form(request):

    return render(request, 'books/movie_list.html')


def dosearch(request):

    error = False
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Books.objects.filter(title__icontains=q)
            return render(request, 'books/movie_list.html',
                      {'books': books, 'query': q})
    else:


        return render(request,'search_form.html', {'error':True})


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email','abc@gmail.com'),
                ['xyz@gmail.com'],

            )
            return HttpResponseRedirect('/contact/thanks')
        else:
            form = ContactForm()
        return render(request, 'contact_form.html',
                      {'form':form})

def books_list_tem(request):
    return render(request,'books/movie_list.html')


def homepage(request):
    return render(request,
                  'home.html')


def book_detail(request, id, slug ):
    book = get_object_or_404(Books,
                             id=id,
                             slug=slug)
    comments = book.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request,
                  'books/movie_detail.html',
                  {'book':book,
                   'comments':comments,
                   'new_comment':new_comment,
                   'comment_form':comment_form})


def export(request):
    book_resource = BookResource()
    dataset = book_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'
    return response



def simple_upload(request):
    if request.method == 'POST':
        book_resource = BookResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = book_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            book_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')



class Center_Content_List(ListView):
    template_name = 'home.html'
    model = CenterContentModel



def Marketing_content(request):
    object_list= MarketingContent.object.all()
    return render(request, 'home.html',
                  {'object_list':object_list})


class Scrollable_Content_List(ListView):
    template_name = 'home.html'
    model = ScrollAbleContent