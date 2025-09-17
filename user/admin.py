from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_trener')  # first_name - первое поле
    list_editable = ('last_name', 'email', 'is_trener')  # Уберите first_name из list_editable
    # ИЛИ
    list_display_links = ('first_name',)  # Явно укажите, что first_name - это ссылка