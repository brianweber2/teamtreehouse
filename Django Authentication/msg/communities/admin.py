from django.contrib import admin

from . import models


class CommunityMemberInline(admin.TabularInline):
    model = models.CommunityMember


class CommunityAdmin(admin.ModelAdmin):
    inlines = [CommunityMemberInline]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(models.Community, CommunityAdmin)
