import factory.django


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "auth.User"

    username = factory.Faker("user_name")
    password = factory.Faker("password")

class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "courses.Course"

    title = factory.Faker("sentence", nb_words = 4)
    description = factory.Faker("text", max_nb_chars = 250)
    start_date = factory.Faker("date_object")
    end_date = factory.Faker("date_object")
    author = factory.SubFactory(UserFactory)
    price = factory.Faker("pydecimal", left_digits=4, right_digits = 2, positive =True)


class EnrollmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "courses.Enrollment"

    user = factory.SubFactory(UserFactory)
    course = factory.SubFactory(CourseFactory)


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "courses.Review"

    user = factory.SubFactory(UserFactory)
    course = factory.SubFactory(CourseFactory)
    rating = factory.Faker("random_int", min=1, max = 5)
    comment = factory.Faker("text", max_nb_chars=250)