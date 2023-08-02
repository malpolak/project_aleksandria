from django.core.exceptions import ValidationError
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"


class Review(models.Model):

    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    review_date = models.DateField(auto_now_add=True)
    rating = models.PositiveIntegerField(
        choices=RATING_CHOICES
    )
    comment = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        # print(self.rating, type(self.rating))
        if self.rating not in [x[0] for x in self.RATING_CHOICES]:
            raise ValidationError("Invalid rating.")

        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.user.username} - {self.course.title} - {self.rating}"


    # class Meta:
    #     unique_together = ['user', 'course']