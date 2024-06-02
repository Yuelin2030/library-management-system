from django import forms
from .models import Article, LibraryMember, LibraryTransaction

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'content']  # Excluding 'published_date' because it's auto_now_add

class LibraryMemberForm(forms.ModelForm):
    class Meta:
        model = LibraryMember
        fields = ['name', 'email', 'phone', 'address']

class LibraryTransactionForm(forms.ModelForm):
    class Meta:
        model = LibraryTransaction
        fields = ['article', 'member', 'borrow_date', 'return_date', 'fee']
