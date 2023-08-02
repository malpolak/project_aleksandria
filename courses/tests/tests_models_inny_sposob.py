from django.test import TestCase
from courses.models import Course, Review, Enrollment
from django.contrib.auth.models import User
from datetime import date



class BaseTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="1234")
        self.course = Course.objects.create(
            title="Python",
            description="Python course",
            start_date=date(2023, 1, 1),
            end_date=date(2023, 1, 18),
            author=self.user,
            price=100.00
        )


class TestCourseModel_1(BaseTest):

    def test_course_model_str_method_1(self):
        self.assertEqual(str(self.course), "Python")


class TestEnrollmentModel_1(BaseTest):

    def setUp(self):
        super().setUp()
        self.enrollment = Enrollment.objects.create(
            user=self.user,
            course=self.course,
        )

    def test_enrollment_model_str_method_1(self):
        self.assertEqual(str(self.enrollment), "testuser - Python")


class TestReviewModel_1(BaseTest):

    def setUp(self):
        super().setUp()
        self.review = Review.objects.create(
            user=self.user,
            course=self.course,
            comment="Great course",
            rating=5,
        )

    def test_review_model_str_method_1(self):
        expected_str = f"{self.user.username} - {self.course.title} - {self.review.rating}"
        self.assertEqual(str(self.review), expected_str)
