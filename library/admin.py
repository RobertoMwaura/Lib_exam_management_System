from django.contrib import admin
from .models import Category, Book, AllUsers, Users, MyUsers,PremiumBook,Categoryp,BookSearch
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug': ('name',)}

class CategorypAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug': ('name',)}

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug': ('title',)}
admin.site.register(Category)
admin.site.register(Book, BookAdmin)

class PremiumBookAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug': ('title',)}
admin.site.register(Categoryp)
admin.site.register(PremiumBook, PremiumBookAdmin)

class BookSearchAdmin(admin.ModelAdmin):
    admin.site.register(BookSearch)

class AllUsersAdmin(admin.ModelAdmin):
    admin.site.register(AllUsers)

class UsersAdmin(admin.ModelAdmin):
    admin.site.register(Users)

class MyUsersAdmin(admin.ModelAdmin):
    admin.site.register(MyUsers)


