from django.contrib import admin
from .models import MentorshipRequest, MentorSession


@admin.register(MentorshipRequest)
class MentorshipRequestAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'seeker', 'status', 'requested_at')
    list_filter = ('status', 'requested_at')
    search_fields = ('mentor__user__username', 'seeker__user__username', 'message')
    date_hierarchy = 'requested_at'
    ordering = ('-requested_at',)


@admin.register(MentorSession)
class MentorSessionAdmin(admin.ModelAdmin):
    list_display = ('mentorship_request', 'topic', 'session_time', 'created_at')
    list_filter = ('session_time', 'created_at')
    search_fields = ('topic', 'mentorship_request__mentor__user__username', 'mentorship_request__seeker__user__username')
    date_hierarchy = 'session_time'
    ordering = ('session_time',)
