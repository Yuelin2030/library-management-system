from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from .models import Article, LibraryMember, LibraryTransaction, LibrarySettings
from .forms import ArticleForm, LibraryMemberForm, LibraryTransactionForm

def index(request):
    return render(request, 'library/index.html')

# Article Views
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'library/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'library/article_detail.html', {'article': article})

def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'library/article_edit.html', {'form': form})

def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'library/article_edit.html', {'form': form})

def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')

# Member Views
def member_list(request):
    members = LibraryMember.objects.all()
    return render(request, 'library/member_list.html', {'members': members})

def member_detail(request, pk):
    member = get_object_or_404(LibraryMember, pk=pk)
    return render(request, 'library/member_detail.html', {'member': member})

def member_new(request):
    if request.method == "POST":
        form = LibraryMemberForm(request.POST)
        if form.is_valid():
            member = form.save()
            return redirect('member_detail', pk=member.pk)
    else:
        form = LibraryMemberForm()
    return render(request, 'library/member_edit.html', {'form': form})

def member_edit(request, pk):
    member = get_object_or_404(LibraryMember, pk=pk)
    if request.method == "POST":
        form = LibraryMemberForm(request.POST, instance=member)
        if form.is_valid():
            member = form.save()
            return redirect('member_detail', pk=member.pk)
    else:
        form = LibraryMemberForm(instance=member)
    return render(request, 'library/member_edit.html', {'form': form})

def member_delete(request, pk):
    member = get_object_or_404(LibraryMember, pk=pk)
    member.delete()
    return redirect('member_list')

# Transaction Views
def transaction_list(request):
    transactions = LibraryTransaction.objects.all()
    return render(request, 'library/transaction_list.html', {'transactions': transactions})

def transaction_detail(request, pk):
    transaction = get_object_or_404(LibraryTransaction, pk=pk)
    return render(request, 'library/transaction_detail.html', {'transaction': transaction})

def transaction_new(request):
    if request.method == "POST":
        form = LibraryTransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            try:
                transaction.clean()  # Call clean method to check debt
                transaction.save()
                return redirect('transaction_detail', pk=transaction.pk)
            except ValidationError as e:
                form.add_error(None, e.message)
    else:
        form = LibraryTransactionForm()
    return render(request, 'library/transaction_edit.html', {'form': form})

def transaction_edit(request, pk):
    transaction = get_object_or_404(LibraryTransaction, pk=pk)
    if request.method == "POST":
        form = LibraryTransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            try:
                transaction = form.save(commit=False)
                transaction.clean()  # Call clean method to check debt
                transaction.save()
                return redirect('transaction_detail', pk=transaction.pk)
            except ValidationError as e:
                form.add_error(None, e.message)
    else:
        form = LibraryTransactionForm(instance=transaction)
    return render(request, 'library/transaction_edit.html', {'form': form})

def transaction_delete(request, pk):
    transaction = get_object_or_404(LibraryTransaction, pk=pk)
    transaction.delete()
    return redirect('transaction_list')

# Settings Views
def library_settings_view(request):
    settings = LibrarySettings.objects.all()
    return render(request, 'library/settings.html', {'settings': settings})


