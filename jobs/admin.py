from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from .models import Company, Job, JobApplication, JobReport


# -----------------------
# Company Admin
# -----------------------
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'industry', 'is_verified', 'created_by')
    list_filter = ('is_verified', 'industry')
    search_fields = ('name', 'location', 'created_by__user__username')
    list_editable = ('is_verified',)
    actions = ['verify_companies', 'unverify_companies']

    def verify_companies(self, request, queryset):
        queryset.update(is_verified=True)
        self.message_user(request, f'{queryset.count()} companies verified.')
    verify_companies.short_description = "Verify selected companies"

    def unverify_companies(self, request, queryset):
        queryset.update(is_verified=False)
        self.message_user(request, f'{queryset.count()} companies unverified.')
    unverify_companies.short_description = "Unverify selected companies"


# -----------------------
# Job Admin
# -----------------------
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'provider', 'location', 'job_type', 'is_active', 'verification_status', 'report_count', 'created_at')
    list_filter = ('job_type', 'is_active', 'is_verified', 'created_at')
    search_fields = ('title', 'company__name', 'skills_required', 'provider__user__username')
    list_editable = ('is_active',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at', 'verified_at')
    actions = ['verify_jobs', 'unverify_jobs']

    fieldsets = (
        ('Job Information', {
            'fields': ('title', 'company', 'provider', 'description', 'location', 'salary')
        }),
        ('Requirements', {
            'fields': ('job_type', 'skills_required', 'experience_required')
        }),
        ('Status', {
            'fields': ('is_active', 'is_verified', 'verified_at')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def verification_status(self, obj):
        if obj.is_verified:
            return format_html('<span style="color: green; font-weight: bold;">✓ Verified</span>')
        return format_html('<span style="color: orange;">⏳ Pending</span>')
    verification_status.short_description = 'Verification'

    def report_count(self, obj):
        count = obj.reports.filter(status='pending').count()
        if count > 0:
            return format_html('<span style="color: red; font-weight: bold;">⚠ {}</span>', count)
        return '0'
    report_count.short_description = 'Reports'

    def verify_jobs(self, request, queryset):
        queryset.update(is_verified=True, verified_at=timezone.now())
        self.message_user(request, f'{queryset.count()} jobs verified.')
    verify_jobs.short_description = "Verify selected jobs"

    def unverify_jobs(self, request, queryset):
        queryset.update(is_verified=False, verified_at=None)
        self.message_user(request, f'{queryset.count()} jobs unverified.')
    unverify_jobs.short_description = "Unverify selected jobs"


# -----------------------
# Job Application Admin
# -----------------------
@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'seeker', 'status', 'skill_match_display', 'applied_at')
    list_filter = ('status', 'applied_at')
    search_fields = ('job__title', 'seeker__user__username')
    ordering = ('-applied_at',)
    date_hierarchy = 'applied_at'
    readonly_fields = ('skill_match_percentage', 'applied_at')

    def skill_match_display(self, obj):
        percentage = obj.skill_match_percentage
        if percentage >= 70:
            color = 'green'
        elif percentage >= 40:
            color = 'orange'
        else:
            color = 'red'
        return format_html('<span style="color: {}; font-weight: bold;">{}%</span>', color, percentage)
    skill_match_display.short_description = 'Skill Match'


# -----------------------
# Job Report Admin
# -----------------------
@admin.register(JobReport)
class JobReportAdmin(admin.ModelAdmin):
    list_display = ('job', 'reported_by', 'reason', 'status', 'created_at')
    list_filter = ('status', 'reason', 'created_at')
    search_fields = ('job__title', 'reported_by__user__username', 'description')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_editable = ('status',)
    readonly_fields = ('job', 'reported_by', 'reason', 'description', 'created_at')
    
    fieldsets = (
        ('Report Details', {
            'fields': ('job', 'reported_by', 'reason', 'description', 'created_at')
        }),
        ('Admin Actions', {
            'fields': ('status', 'admin_notes', 'resolved_at')
        }),
    )

    actions = ['mark_investigating', 'mark_resolved', 'mark_dismissed']

    def mark_investigating(self, request, queryset):
        queryset.update(status='investigating')
        self.message_user(request, f'{queryset.count()} reports marked as investigating.')
    mark_investigating.short_description = "Mark as Under Investigation"

    def mark_resolved(self, request, queryset):
        queryset.update(status='resolved', resolved_at=timezone.now())
        self.message_user(request, f'{queryset.count()} reports resolved.')
    mark_resolved.short_description = "Mark as Resolved"

    def mark_dismissed(self, request, queryset):
        queryset.update(status='dismissed', resolved_at=timezone.now())
        self.message_user(request, f'{queryset.count()} reports dismissed.')
    mark_dismissed.short_description = "Dismiss Reports"