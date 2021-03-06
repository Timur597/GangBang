from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

# from .forms import ContactForm
from .models import *
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
from django.contrib import messages


def teachers(request):
    teacher1 = Teachers.objects.filter(id=1)
    teacher2 = Teachers.objects.filter(id=2)
    teacher3 = Teachers.objects.filter(id=3)
    teacher4 = Teachers.objects.filter(id=4)
    teacher5 = Teachers.objects.filter(id=5)
    teacher6 = Teachers.objects.filter(id=6)
    teacher7 = Teachers.objects.filter(id=7)
    teacher8 = Teachers.objects.filter(id=8)
    teacher9 = Teachers.objects.filter(id=9)
    context = {
        'teacher1': teacher1,
        'teacher2': teacher2,
        'teacher3': teacher3,
        'teacher4': teacher4,
        'teacher5': teacher5,
        'teacher6': teacher6,
        'teacher7': teacher7,
        'teacher8': teacher8,
        'teacher9': teacher9,
    }
    return render(request, 'teachers.html', context=context)


def students(request):
    student1 = Students.objects.filter(id=1)
    student2 = Students.objects.filter(id=2)
    student3 = Students.objects.filter(id=3)
    student4 = Students.objects.filter(id=4)
    student5 = Students.objects.filter(id=5)
    student6 = Students.objects.filter(id=6)
    student7 = Students.objects.filter(id=7)
    student8 = Students.objects.filter(id=8)
    student9 = Students.objects.filter(id=9)
    context = {

        'student1': student1,
        'student2': student2,
        'student3': student3,
        'student4': student4,
        'student5': student5,
        'student6': student6,
        'student7': student7,
        'student8': student8,
        'student9': student9,
    }
    return render(request, 'students.html', context=context)


def index(request):
    python = Courses.objects.filter(id=1)
    javascript = Courses.objects.filter(id=2)
    java = Courses.objects.filter(id=3)
    english = Courses.objects.filter(id=4)
    german = Courses.objects.filter(id=5)
    china = Courses.objects.filter(id=6)
    math = Courses.objects.filter(id=7)
    physics = Courses.objects.filter(id=8)
    chemistry = Courses.objects.filter(id=9)
    student1 = Students.objects.filter(id=1)
    student2 = Students.objects.filter(id=2)
    student3 = Students.objects.filter(id=3)
    student4 = Students.objects.filter(id=4)
    student5 = Students.objects.filter(id=5)
    student6 = Students.objects.filter(id=6)
    student7 = Students.objects.filter(id=7)
    student8 = Students.objects.filter(id=8)
    student9 = Students.objects.filter(id=9)
    teacher1 = Teachers.objects.filter(id=1)
    teacher2 = Teachers.objects.filter(id=2)
    teacher3 = Teachers.objects.filter(id=3)
    teacher4 = Teachers.objects.filter(id=4)
    teacher5 = Teachers.objects.filter(id=5)
    teacher6 = Teachers.objects.filter(id=6)
    teacher7 = Teachers.objects.filter(id=7)
    teacher8 = Teachers.objects.filter(id=8)
    teacher9 = Teachers.objects.filter(id=9)
    context = {
        'python': python,
        'title': 'Gang bang',
        'javascript': javascript,
        'java': java,
        'english': english,
        'german': german,
        'china': china,
        'math': math,
        'physics': physics,
        'chemistry': chemistry,
        'student1': student1,
        'student2': student2,
        'student3': student3,
        'student4': student4,
        'student5': student5,
        'student6': student6,
        'student7': student7,
        'student8': student8,
        'student9': student9,
        'teacher1': teacher1,
        'teacher2': teacher2,
        'teacher3': teacher3,
        'teacher4': teacher4,
        'teacher5': teacher5,
        'teacher6': teacher6,
        'teacher7': teacher7,
        'teacher8': teacher8,
        'teacher9': teacher9,
    }
    return render(request, 'base.html', context=context)


# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'test.mysite.itc@gmail.com',
#                              ['timurhalilov9@gmail.com'], fail_silently=True)
#             if mail:
#                 messages.success(request, '???????????? ??????????????????????')
#                 return redirect('contact')
#             else:
#                 messages.error(request, '???????????? ????????????????')
#         else:
#             messages.error(request, "???????????? ????????????????, ?????????????????? ????????")
#     else:
#         form = ContactForm()
#     return render(request, 'news/test.html', {'form': form})
# #
#
# class Home(ListView):
#     model = Courses
#     template_name = 'courses/index.html'
#     context_object_name = 'courses'
#
#
# class CoursesByCategory(ListView):
#     template_name = 'courses/index.html'
#     context_object_name = 'courses'
#     allow_empty = False
#
#     def get_queryset(self):
#         return Courses.objects.filter(category__slug=self.kwargs['slug'])
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = '???????? ?????????????????????????? ??????'
#         return context
#
#
#
#
#
#
#
#
#
































# def pageNotFound(request, exception):
#     print(request.GET)
#     return HttpResponseNotFound('<h1> ???????????????? ???? ?????????????? </h1>')
#
#
# lang = [{'title': "?? ??????????", "url_name": "about"},
#         {'title': "???????????????? ????????????", "url_name": "add_page"},
#         {'title': "???????????????? ??????????", "url_name": "contact"},
#         {'title': "??????????", "url_name": "login"},
#         ]
#
#
# def index(request):  # request ?????? ???????????? ???? ?????????? HttpRequest(?????????? ???????? ?? ????????????????, ?? ???????? ?? ??.??)
#     print(request.GET)
#     posts = Courses.objects.all()
#     cats = Category.objects.all()
#     # return render(request, 'courses/index.html', {'posts': posts, 'lang': lang, 'title': '?????????????? ????????????????'})
#     context = {
#         'posts': posts,
#         'cats': cats,
#         'lang': lang,
#         'title': '?????????????? ????????????????',
#         'cat_selected': 0,
#     }
#     return render(request, 'courses/index.html', context=context)
#
#
# def about(request):
#     print(request.GET)
#     return HttpResponse('??????-???? ??????')
#
#
# def contact(request):
#     print(request.GET)
#     return HttpResponse('??????-???? ??????')
#
#
# def addpage(request):
#     print(request.GET)
#     return HttpResponse('??????-???? ??????')
#
# def login(request):
#     print(request.GET)
#     return HttpResponse('??????-???? ??????')
#
#
# def show_category(request, cat_id):
#     print(request.GET)
#     posts = Courses.objects.filter(cat_id=cat_id)
#     if len(posts) == 0:
#         raise Http404
#
#     cats = Category.objects.all()
#     context = {
#         'posts': posts,
#         'cats': cats,
#         'lang': lang,
#         'title': '?????????????????????? ???? ??????????????????',
#         'cat_selected': cat_id,
#     }
#     return render(request, 'courses/index.html', context=context)

#
# def archive(request, year):
#     print(request.GET)
#     if int(year) > 2021:
#         return redirect('home')
#     return HttpResponse(f'<h1> ?????????? ???? ?????????? </h> <p> {year} </p>')
