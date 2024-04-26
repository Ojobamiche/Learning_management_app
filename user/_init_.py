# views.py
from django.shortcuts import render
from .models import Course  # assuming you have a Course model

def course_selection_view(request):
    courses = Course.objects.all()  # retrieve all courses from the database
    if request.method == 'POST':
        # Process the form submission
        selected_courses = request.POST.getlist('courses')
        # Save the user's selections, etc.
        # ...
        return render(request, 'selection_saved.html')  # redirect or show confirmation
    return render(request, 'courseselection.html', {'courses': courses})
# urls.py
from django.urls import path
from . import views  
urlpatterns =