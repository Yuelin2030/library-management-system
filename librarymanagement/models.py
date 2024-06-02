from django.db import models
from django.core.exceptions import ValidationError

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class LibraryMember(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

class LibraryTransaction(models.Model):
    member = models.ForeignKey(LibraryMember, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    fee = models.DecimalField(max_digits=5, decimal_places=2)

    def clean(self):
        super().clean()
        member_transactions = LibraryTransaction.objects.filter(member=self.member, return_date__isnull=True).exclude(pk=self.pk)
        outstanding_debt = member_transactions.aggregate(total_debt=models.Sum('fee'))['total_debt'] or 0
        if outstanding_debt + self.fee > 500:
            raise ValidationError(f"{self.member.name} has an outstanding debt exceeding KES 500.")

    def __str__(self):
        return f"{self.member.name} - {self.article.title}"

class LibrarySettings(models.Model):
    setting_name = models.CharField(max_length=100)
    setting_value = models.CharField(max_length=255)

    def __str__(self):
        return self.setting_name

