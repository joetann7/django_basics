from django.contrib import admin

from notes.models import notes


class NoteAdmin(admin.ModelAdmin):
	list_display = (
		'id',
		'title',
		'note',
	)
	search_fields = (
		'title',
		'note',
	)