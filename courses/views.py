from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
from django.contrib import messages





def index(request):
    return render(request, 'courses/index.html')

#
# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'test.mysite.itc@gmail.com',
#                              ['timurhalilov9@gmail.com'], fail_silently=True)
#             if mail:
#                 messages.success(request, 'Письмо отправленно')
#                 return redirect('contact')
#             else:
#                 messages.error(request, 'Ошибка отправки')
#         else:
#             messages.error(request, "Ошибка регистрации")
#     else:
#         form = ContactForm()
#     return render(request, 'news/test.html', {'form': form})
#
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
#         context['title'] = 'Рады приветсвовать Вас'
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
#     return HttpResponseNotFound('<h1> Страница не найдена </h1>')
#
#
# lang = [{'title': "О сайте", "url_name": "about"},
#         {'title': "Добавить статью", "url_name": "add_page"},
#         {'title': "Обратная связь", "url_name": "contact"},
#         {'title': "Войти", "url_name": "login"},
#         ]
#
#
# def index(request):  # request это ссылка на класс HttpRequest(здесь инфа о запросах, о куки и т.д)
#     print(request.GET)
#     posts = Courses.objects.all()
#     cats = Category.objects.all()
#     # return render(request, 'courses/index.html', {'posts': posts, 'lang': lang, 'title': 'Главная страница'})
#     context = {
#         'posts': posts,
#         'cats': cats,
#         'lang': lang,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#     return render(request, 'courses/index.html', context=context)
#
#
# def about(request):
#     print(request.GET)
#     return HttpResponse('Что-то там')
#
#
# def contact(request):
#     print(request.GET)
#     return HttpResponse('Что-то там')
#
#
# def addpage(request):
#     print(request.GET)
#     return HttpResponse('Что-то там')
#
# def login(request):
#     print(request.GET)
#     return HttpResponse('Что-то там')
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
#         'title': 'Отображение по категории',
#         'cat_selected': cat_id,
#     }
#     return render(request, 'courses/index.html', context=context)

#
# def archive(request, year):
#     print(request.GET)
#     if int(year) > 2021:
#         return redirect('home')
#     return HttpResponse(f'<h1> Архив по годам </h> <p> {year} </p>')
