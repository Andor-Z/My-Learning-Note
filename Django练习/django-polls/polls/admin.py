from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
# class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # 字段排序
    # fields = ['pub_date', 'question_text']
    # 字段分割为自断集
    fieldsets = [
    (None, {'fields':['question_text']}),
    ('Date information', {'fields':['pub_date'], 'classes':['collapse']}),  # 指定HTML样式类
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)