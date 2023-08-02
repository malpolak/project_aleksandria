from django.shortcuts import render, redirect
from .models import Course, Review, Enrollment
from django.contrib import messages
def course_list(request):
    return render(request, 'courses/course_list.html', {"courses": Course.objects.all()})

def course_detail(request, pk):

    context = {
        "course": Course.objects.get(id=pk),
        "reviews": Review.objects.filter(course=pk),
        "user_enrolled": Enrollment.objects.filter(user=request.user, course=pk).exists(),
    }

    return render(
        request,
        'courses/course_detail.html',
        context
    )


def add_review(request, pk):

    if request.method == "POST":
        course = Course.objects.get(id=pk)
        rating = int(request.POST.get("rating"))
        comment = request.POST.get("comment")
        user = request.user

        Review.objects.create(
            course=course,
            user=user,
            rating=rating,
            comment=comment
        )

    return redirect('course-detail', pk=pk)


def add_enroll(request, pk): # /courses/<int:pk>/enroll/
    course = Course.objects.get(id=pk)
    enrollment, created = Enrollment.objects.get_or_create(user=request.user, course=course)
    if created:
        messages.success(request, 'You have successfully enrolled in the course.')
    else:
        messages.error(request, 'You are already enrolled in the course.')
    return redirect('course-detail', pk=pk)