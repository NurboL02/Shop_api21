from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=9)

    @property
    def movie_count(self):
        return self.product_set.all().count()

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    @property
    def rating(self):
        total_amount = self.review_set.all().count()
        if total_amount == 0:
            return 0
        sum_ = 0
        for i in self.review_set.all():
            sum_ += i.stars
        return sum_ / total_amount

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(max_length=400)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(default=1, verbose_name="stars")

    def __str__(self):
        return self.text
