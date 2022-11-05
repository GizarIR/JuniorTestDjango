from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .models import *


def handle_uploaded_file(file):
    # with open(file, 'r') as f:
    text =''
    text = file.read().decode()
    # зачистим текст от знаков препинания и больших букв
    text = text.lower()
    text = text.replace(';', '')
    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.replace(':', '')
    # преобразуем текст в список
    l_text = text.split()
    # создадим словарь для хранения подсчитываемых элементов
    count = {}
    for word in l_text:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    for k, v in count.items():
        print(k, v)
        Word.objects.create(text=k, num=v)
    return count


def clear_db():
    Word.objects.all().delete()

# def index(request):
#     # print(request.FILES['file'])
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         # print(form)
#         if form.is_valid():
#             print(request.FILES['file'])
#             handle_uploaded_file(request.FILES['my_file'])
#             return HttpResponseRedirect('home')
#     else:
#         form = UploadFileForm()
#     return render(request, 'base.html', {'form': form})

def index(request):
    if request.FILES:
        if request.method == 'POST' and request.FILES['my_file']:
            my_file = request.FILES['my_file']
            clear_db()
            handle_uploaded_file(my_file)
            fs = FileSystemStorage()
            filename = fs.save(my_file.name, my_file)
            uploaded_file_url = fs.url(filename)
            Word.objects.all().update(file_url=uploaded_file_url)
            return render(request, 'base.html', {
                'uploaded_file_url': uploaded_file_url
            })
    return render(request, 'base.html')

def wordcount(request):
    num=0
    file_url = Word.objects.first().file_url
    if request.POST.get('my_word', False):
        if request.method == 'POST' and request.POST['my_word']:
            my_word = request.POST['my_word']
            if Word.objects.filter(text=my_word).exists():
                finded_word = Word.objects.get(text=my_word)
                num = finded_word.num
                file_url = finded_word.file_url
            return render(request, 'base.html', {
                'my_word': my_word,
                'num': num,
                'uploaded_file_url': file_url,
            })
    return render(request, 'base.html')

def clear_memory(request):
    clear_db()
    return redirect('home')