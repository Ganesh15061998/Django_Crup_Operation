from django.shortcuts import render, redirect,HttpResponse,HttpResponseRedirect
from .models import Student

from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
# Create your views here.

def add_show(request):
    errormagg = ""  # Initialize errormagg here to avoid an error in case 'name' is not empty.

    if request.method == "POST":
        data = Student()

        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        new_students = Student(name=name, email=email, password=password)
        if name == "":
            errormagg = "Name Is Required "
        else:
            new_students.save()
            return redirect('addandshow')

    studentdata = Student.objects.all()
    count = 1
    contects = {
        'studentdata': studentdata,
        'errormagg': errormagg,
        'count':count
    }

    return render(request, 'addandshow.html', contects)

def update_data(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return redirect('addandshow')

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Update the student object
        student.name = name
        student.email = email
        student.password = password
        student.save()

        return redirect('addandshow')

    return render(request, 'update.html', {'student': student})


def delete_data(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')  # Redirect to another view after deletion

