from django.shortcuts import render

from django.shortcuts import render
from myapp.models import Person


def index(request):
    if request.method == 'POST':
        # Обработка отправленной формы
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        person = Person(name=name, email=email, age=age)
        person.save()

    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})