from django.contrib import admin
from .models import UserProfile, BookCategory, Book, Review, Borrowing

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user__email', 'phone', 'city', 'postal_code')
    search_fields = ('user__username', 'user__email', 'phone', 'city')

# Register the Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'user', 'get_categories', 'condition', 'is_available', 'location')  # Display these fields in the list
    list_filter = ('is_available', 'condition', 'categories__name')  # Add filters for availability and condition
    search_fields = ('title', 'author', 'location')  # Allow search by title, author, or location

    # Show the categories associated with each book in the list
    def get_categories(self, obj):
        print(obj);
        return ", ".join([category.name for category in obj.categories.all()])
    get_categories.short_description = 'Categories'

admin.site.register(Book, BookAdmin)

# Register the Review model
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'rating', 'created_at')  # Display user, book, rating, and review date
    search_fields = ('user__username', 'book__title')  # Allow search by user and book title
    list_filter = ('rating',)  # Filter reviews by rating

admin.site.register(Review, ReviewAdmin)
admin.site.register(BookCategory)

class BorrowingAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'phone', 'city', 'postal_code', 'created_at')
    search_fields = ('user__username', 'book__title', 'city', 'postal_code')
    list_filter = ('created_at', 'city')
    
admin.site.register(Borrowing)
