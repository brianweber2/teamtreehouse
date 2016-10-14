from django.contrib import admin
from datetime import date

from . import models


def make_published(modelAdmin, request, queryset):
    queryset.update(status='p', is_live=True)
    

def make_in_review(modelAdmin, request, queryset):
    queryset.update(status='r', is_live=False)
    
    
def make_in_progress(modelAdmin, request, queryset):
    queryset.update(status='p', is_live=False)
    
make_published.short_description = "Mark selected courses as Published"

make_in_review.short_description = "Mark selected courses as In Review"

make_in_progress.short_description = "Mark selected courses as In Progress"


class TextInline(admin.StackedInline):
    model = models.Text
    
    fieldsets = (
        (None, {
             'fields': (('title', 'order'), 'description', 'content')
        }),    
    )


class QuizInline(admin.StackedInline):
    model = models.Quiz


class AnswerInline(admin.TabularInline):
    model = models.Answer
    
    
class YearListFilter(admin.SimpleListFilter):
    title ='year created'
    
    parameter_name = 'year'
    
    def lookups(self, request, model_admin):
        return (
            ('2015', '2015'),
            ('2016', '2016'),
        )
    
    def queryset(self, request, queryset):
        if self.value(): 
            return queryset.filter(
                created_at__gte=date(int(self.value()), 1, 1),
                created_at__lte=date(int(self.value()), 12, 31)
            )
    
    
class TopicListFilter(admin.SimpleListFilter):
    title ='topic'
    
    parameter_name = 'topic'
    
    def lookups(self, request, model_admin): 
        return (
            ('python','Python'),
            ('ruby', 'Ruby'),
            ('java', 'Java')
        )
    
    def queryset(self, request, queryset):
        if self.value(): 
            return queryset.filter(
                title__contains=self.value()
            )


class CourseAdmin(admin.ModelAdmin):
    inlines = [TextInline, QuizInline]
    
    search_fields = ['title', 'description']
    
    list_filter = ['created_at', 
                   'is_live', 
                   YearListFilter, 
                   TopicListFilter]
    
    list_display = ['title', 
                    'created_at', 
                    'is_live', 
                    'time_to_complete',
                    'status']
    
    list_editable = ['status']
    
    actions = [make_published, make_in_review, make_in_progress]
    
    admin.site.disable_action('delete_selected')
    
    class Media:
        js = ('js/vendor/markdown.js', 'js/preview.js')
        css = {
            'all': ('css/preview.css',)
        }


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline,]
    
    search_fields = ['prompt']
    
    list_display = ['prompt', 'quiz', 'order']
    
    list_editable = ['quiz', 'order']
    
    radio_fields = {'quiz': admin.HORIZONTAL}
    
    
class QuizAdmin(admin.ModelAdmin):
    fields = ['course', 
              'title', 
              'description', 
              'order', 
              'total_questions']
    
    search_fields = ['title', 'description']
    
    list_filter = ['course']
    
    list_display = ['title', 
                    'course', 
                    'number_correct_needed', 
                    'total_questions']
    
    list_editable = ['course', 'total_questions']
    
    
class TextAdmin(admin.ModelAdmin):
    # fields = ['course', 'title', 'order', 'description', 'content']
    
    fieldsets = (
        (None, {'fields': ('course', 'title', 'order', 'description')}),
        ('Add content', {'fields': ('content',),
                         'classes': ('collapse',)})
    )
    
    radio_fields = {'course': admin.VERTICAL}
    

admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Text, TextAdmin)
admin.site.register(models.Quiz, QuizAdmin)
admin.site.register(models.MultipleChoiceQuestion, QuestionAdmin)
admin.site.register(models.TrueFalseQuestion, QuestionAdmin)
