from django.db import models
from django.core.exceptions import ValidationError

class Car(models.Model):
    name = models.CharField(max_length=300)
    model = models.CharField(max_length=300)
    year = models.DateField()

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    issue = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.issue}"

    # validate if category already exists
    def clean(self):
        existing_category = Category.objects.filter(
            issue=self.issue).exclude(pk=self.pk)
        if existing_category.exists():
            raise ValidationError("Category with this name already exists.")

class Driver(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        ordering =['-email']


class Tracker(models.Model):
    car_name = models.ForeignKey(Car,max_length=300,on_delete=models.CASCADE)
    mileage = models.IntegerField()
    #issue = models.CharField(max_length=30,default=None,choices=ISSUES)
    issue = models.ForeignKey(Category,max_length=300,on_delete=models.CASCADE)
    describe_issues = models.TextField(max_length=3000,default=None)
    driver =models.ForeignKey(Driver,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.car_name

    class Meta:
        ordering =['-date_added','date_edited']



class Chat(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    heading = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading

    class Meta:
        ordering =['-date_added','date_edited']