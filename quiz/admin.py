from django.contrib import admin
from .models import Question, Answer, Category, Student, Interest

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'reg_date')
    search_fields = ['question']

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'category', 'reg_date')
    search_fields = ['answer']

class InterestAdmin(admin.ModelAdmin):
    list_display = ('title', 'students', 'quantity', 'reg_date')
    search_fields = ['title', 'students__name']

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'number', 'reg_date')
    search_fields = ['name', 'number']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'reg_date')  
    search_fields = ('title',)  



admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(Student, StudentAdmin)
