from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

admin.site.site_title = 'Бухгалтерские услуги'
admin.site.site_header = 'Бухгалтерские услуги'


class RequestsInLine(admin.TabularInline):
    model = ServiceRequest
    extra = 0


class ImagesInLine(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="100", height="100">')
    get_img.short_description = 'Изображение'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'url', 'publish')
    list_filter = ('publish',)
    list_search = ('title', 'text', 'url')
    list_editable = ('publish',)
    inlines = [ImagesInLine, RequestsInLine]
    actions = ['publish_now', 'unpublish']

    save_on_top = True
    save_as = True
    
    fieldsets = (
        ('text', {'fields': ('title', 'text')}),
        ('options', {'fields': (('url', 'publish'),),
                     'classes': ('collapse',)}),
        )

    def publish_now(self, request, queryset):
        row_update = queryset.update(publish=True)
        if row_update == 1:
            msg = '1 запись была опубликована'
        else:
            msg = f'{row_update} записей было опубликовано'
        self.message_user(request, msg)

    def unpublish(self, request, queryset):
        row_update = queryset.update(publish=False)
        if row_update == 1:
            msg = '1 запись была снята с публикации'
        else:
            msg = f'{row_update} записей было снято с пубикации'
        self.message_user(request, msg)

    publish_now.short_description = 'Опубликовать'
    publish_now.allowed_permissions = ('change',)

    unpublish.short_description = 'Снять с публикации'
    unpublish.allowed_permissions = ('change',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('service', 'title', 'get_img')
    readonly_fields = ('get_img',)
    list_filter = ('service',)
    list_search = ('title',)
    save_on_top = True

    def get_img(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="100" height="100"')
    get_img.short_description = 'Изображение'


@admin.register(SiteWrapper)
class SiteWrapperAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_about', 'about', 'footer_text', 'footer_link')
    list_search = ('name', 'show_about', 'about', 'footer_text', 'footer_link')


@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'text')
    list_search = ('title', 'description','text')


@admin.register(Guarantee)
class GuaranteeeAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')
    list_search = ('title', 'text')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'text')
    list_filter = ('type',)
    list_search = ('title', 'text')
    save_on_top = True


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'service', 'description', 'date', 'is_processed')
    list_filter = ('service', 'date', 'is_processed')
    list_search = ('name', 'phone', 'email', 'description')
    list_editable = ('is_processed',)
    save_on_top = True
    actions = ['set_processed', 'unset_processed']
    
    fieldsets = (
        ('Контакт', {'fields': (('name', 'phone', 'email'),),
                     'classes': ('collapse',)}),
        ('Услуга', {'fields': (('service', 'description'),),
                     'classes': ('collapse',)}),
        ('Дополнительно', {'fields': (('date', 'is_processed'),),
                     'classes': ('collapse',)}),
        )

    def set_processed(self, request, queryset):
        row_update = queryset.update(is_processed=True)
        if row_update == 1:
            msg = f'{row_update} запись обновлена'
        else:
            msg = f'{row_update} записей обновлено'
        self.message_user(request, msg)

    def unset_processed(self, request, queryset):
        row_update = queryset.update(is_processed=False)
        if row_update == 1:
            msg = f'{row_update} запись обновлена'
        else:
            msg = f'{row_update} записей обновлено'
        self.message_user(request, msg)

    set_processed.short_description = 'Обработано'
    set_processed.allowed_permissons = ('change',)
    
    unset_processed.short_description = 'Не обработано'
    unset_processed.allowed_permissons = ('change',)