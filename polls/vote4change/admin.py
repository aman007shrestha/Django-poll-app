from django.contrib import admin
from .models import Question, Choice
# Register your models here.


admin.site.site_header = "Vote4Change Admin"
admin.site.site_title = "Vote4Change Admin Area"
admin.site.index_title = "Welcome to the vote4change admin area"

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date information', {'fields' : ["pub_date"], 'classes':['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ["question_text"]



admin.site.register(Question, QuestionAdmin)
