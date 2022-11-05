import codecs

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file


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
    return count


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
    if request.method == 'POST' and request.FILES['my_file']:
        my_file = request.FILES['my_file']
        print(handle_uploaded_file(my_file))
        fs = FileSystemStorage()
        filename = fs.save(my_file.name, my_file)
        uploaded_file_url = fs.url(filename)
        return render(request, 'base.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'base.html')