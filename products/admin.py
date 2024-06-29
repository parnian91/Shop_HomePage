from django.contrib import admin
from products.models import Product, UserProfile, Comment


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'product', 'approved', 'created_date')
    list_filter = ('product', 'approved')
    search_fields = ['name', 'product']

admin.site.register(Comment, CommentAdmin)
# Register your models here.
admin.site.register(Product)
admin.site.register(UserProfile)

