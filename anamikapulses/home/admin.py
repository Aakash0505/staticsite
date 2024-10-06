from django.contrib import admin
from home.models import *
from django.http import HttpResponse
import csv
from treebeard.forms import movenodeform_factory
from treebeard.admin import TreeAdmin
# Register your models here.


@admin.register(Homestatic)
class HomestaticAdmin(admin.ModelAdmin):
    list_display = ["updated_on","published"]


@admin.register(AreaOfInterest)
class AreaOfInterestAdmin(TreeAdmin, admin.ModelAdmin):

    list_display = ["published",'title']
    search_fields = ["published",'title']
    list_filter = ["published",'title']
    form = movenodeform_factory(AreaOfInterest)


@admin.register(Team)
class TeamAdmin(TreeAdmin, admin.ModelAdmin):

    list_display = ["published",'name']
    search_fields = ["published",'name']
    list_filter = ["published",'name']
    form = movenodeform_factory(Team)

@admin.register(Category)
class CategoryAdmin(TreeAdmin, admin.ModelAdmin):

    list_display = ["published",'name']
    search_fields = ["published",'name']
    list_filter = ["published",'name']
    form = movenodeform_factory(Category)


@admin.register(Product)
class ProductAdmin(TreeAdmin, admin.ModelAdmin):

    list_display = ["published",'name']
    search_fields = ["published",'name']
    list_filter = ["published",'category']
    form = movenodeform_factory(Product)




@admin.register(Contact)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_id', 'contact_no','area_of_interest', 'message', 'published', 'created_on'
                    )
    search_fields = ('name', 'email_id', 'contact_no','area_of_interest', 'message', 'published', 'created_on')
    list_filter = ('name', 'email_id', 'contact_no','area_of_interest', 'message', 'created_on')
    list_per_page = 20
    actions = ["export_as_csv"]
    ordering = ('-created_on',)
    readonly_fields = ['name', 'email_id', 'contact_no','area_of_interest', 'message', 'published', 'created_on']

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        # field_names = [field.name for field in meta.fields]
        field_names = ['name', 'email_id', 'contact_no','area_of_interest', 'message','document', 'published', 'created_on']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
            meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field)
                                   for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"
