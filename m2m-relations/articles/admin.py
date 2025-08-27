from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Tag, Article, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        has_main_tag = False
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data.get('is_main'):
                has_main_tag = True
        if not has_main_tag:
            raise ValidationError('Должен быть хотя бы один основной тег.')


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


