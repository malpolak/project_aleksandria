from django.test import TestCase
from courses import factories
from django.urls import reverse
from courses.models import Enrollment

class TestCourseListView(TestCase):

    def setUp(self):
        self.course_1 = factories.CourseFactory()
        self.course_2 = factories.CourseFactory()

    def test_course_list_view(self):
        list_url = reverse("course-list")
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "courses/course_list.html")
        self.assertContains(response, self.course_1.title)
        self.assertContains(response, self.course_2.title)
        self.assertContains(response, reverse("course-detail", kwargs={"pk": self.course_1.id}))
        self.assertContains(response, reverse("course-detail", kwargs={"pk": self.course_2.id}))


class TestEnrollmentView(TestCase):
     def setUp(self):
         self.course = factories.CourseFactory()
         self.user = factories.UserFactory()

     def test_enrollment_user_in_course(self):
         # self.client.login(username=self.user.username, password=self.user.password)
         self.client.force_login(self.user)
         enroll_url = reverse("course-enroll", kwargs={"pk": self.course.id})  # /courses/1/enroll/

         self.assertEqual(self.course.enrollments.count(), 0)
         response = self.client.post(enroll_url, follow=True)
         self.assertEqual(response.status_code, 200)
         self.assertContains(response, 'You have successfully enrolled in the course.')
         self.assertEqual(self.course.enrollments.count(), 1)
         self.assertEqual(Enrollment.objects.first().user, self.user)
         self.assertEqual(Enrollment.objects.first().course, self.course)

     def test_enrollment_user_already_in_course(self):
         self.client.force_login(self.user)
         enroll_url = reverse("course-enroll", kwargs={"pk": self.course.id})
         response = self.client.post(enroll_url, follow=True)
         response = self.client.post(enroll_url, follow=True)
         self.assertEqual(response.status_code, 200)
         self.assertContains(response, 'You are already enrolled in the course.')


class TestReviewView(TestCase):
    def setUp(self):
        self.course = factories.CourseFactory()
        self.user = factories.UserFactory()

    def test_add_review(self):
        review_data = {"rating":4,
                       "comment":"aaaa"
                       }

        self.client.force_login(self.user)
        review_url = reverse("add-review", kwargs={"pk": self.course.id})  # /courses/1/enroll/
        self.assertEqual(self.course.review_set.count(), 0)
        response = self.client.post(review_url, follow=True, data=review_data)
        self.assertEqual(self.course.review_set.count(), 1)
        self.assertEqual(self.course.review_set.last().rating,review_data["rating"])

