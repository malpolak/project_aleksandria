from django.test import TestCase
from courses import factories

class TestCourseModel(TestCase):

    def setUp(self) -> None:
        self.course = factories.CourseFactory(title="Python")

    def test_course_model_str_method(self):
        self.assertEqual(str(self.course), "Python")


class TestEnrollmentModel(TestCase):

    def setUp(self):
        self.enrollment = factories.EnrollmentFactory()

    def test_enrollment_model_str_method(self):
        expected_str = f"{self.enrollment.user.username} - {self.enrollment.course.title}"
        self.assertEqual(str(self.enrollment), expected_str)


class TestReviewModel(TestCase):

    def setUp(self):
        self.review = factories.ReviewFactory()

    def test_review_model_str_method(self):
        expected_str = f"{self.review.user.username} - {self.review.course.title} - {self.review.rating}"
        self.assertEqual(str(self.review), expected_str)
