from django.shortcuts import render, redirect
from.models import Course, Review, Enrollment
from django.contrib import messages

def course_list(request):
    return render(request, 'courses/course_list.html', {"courses": Course.objects.all()})

def course_detail(request, pk):

    context = {
        "course": Course.objects.get(id=pk),
        "reviews": Review.objects.filter(course=pk),
    }

    return render(request, 'courses/course_detail.html', context)


def add_review(request, pk):

    if request.method == "POST":
        course = Course.objects.get(id=pk)
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")
        user = request.user
        Review.objects.create(course=course, user=user, rating=rating, comment=comment)

    return redirect('course-detail', pk=pk)

def add_enroll(request, pk):
    course = Course.objects.get(pk=pk)
    enrollment, created = Enrollment.objects.get_or_create(user=request.user, course=course)
    if created:
        messages.success(request, 'You have successfully enrolled in the course')
    else:
        messages.success(request, 'You are already enrolled in the course')

    return redirect('course-detail', pk=pk)