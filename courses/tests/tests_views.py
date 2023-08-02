from django.test import TestCase
from courses import factories
from django.urls import reverse
from courses.models import Enrollment

class TestCourseListView(TestCase):

    def setUp(self) -> None:
        self.course_1 = factories.CourseFactory(title="course_1")
        self.course_2 = factories.CourseFactory(title="course_2")

    def test_course_list_view(self):
        list_url = reverse("course-list")
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "courses/course_list.html")
        #print(response.content.decode())
        self.assertContains(response, "course_1")
        self.assertContains(response, "course_2")
        self.assertNotContains(response, "course_3")
        self.assertContains(response, reverse("course-detail", kwargs={"pk": self.course_1.id}))
        self.assertContains(response, reverse("course-detail", kwargs={"pk": self.course_2.id}))


class TestEnrollmentView(TestCase):

    def setUp(self):
        self.course = factories.CourseFactory()
        self.user = factories.UserFactory()

    def test_enrollment_user_in_course(self):
        #self.client.login(username=self.user.username, password=self.user.password) optional
        self.client.force_login(self.user)
        enroll_url = reverse('course-enroll', kwargs={"pk": self.course.id}) #/courses/enroll

        self.assertEqual(self.course.enrollments.count(), 0) #or self.assertEqual(self.course.enrollment_set.count(), 0)
        response = self.client.post(enroll_url, follow=True) #if without follow, status_code will be 302
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'You have successfully enrolled in the course')
        self.assertEqual(self.course.enrollments.count(),1)
        self.assertEqual(Enrollment.objects.first().user, self.user)
        self.assertEqual(Enrollment.objects.first().course, self.course)

    def test_enrollment_user_already_in_course(self):
        self.client.force_login(self.user)
        enroll_url = reverse('course-enroll', kwargs={"pk": self.course.id})
        response = self.client.post(enroll_url, follow=True)
        response = self.client.post(enroll_url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'You are already enrolled in the course')



