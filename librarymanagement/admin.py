from django.contrib import admin
from .models import Article, LibraryMember, LibraryTransaction, LibrarySettings
from .forms import ArticleForm, LibraryMemberForm, LibraryTransactionForm

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm

@admin.register(LibraryMember)
class LibraryMemberAdmin(admin.ModelAdmin):
    form = LibraryMemberForm

@admin.register(LibraryTransaction)
class LibraryTransactionAdmin(admin.ModelAdmin):
    form = LibraryTransactionForm

@admin.register(LibrarySettings)
class LibrarySettingsAdmin(admin.ModelAdmin):
    pass



