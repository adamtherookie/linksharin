from django.contrib import admin

from .models import User, Page, Category, Link, Style, Colorscheme

admin.site.register(User)
admin.site.register(Page)
admin.site.register(Category)
admin.site.register(Link)
admin.site.register(Style)
admin.site.register(Colorscheme)
