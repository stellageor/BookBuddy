from django.contrib import admin
from .models import Profile, BookCategory, Book, Message, Review

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'location')  # Display user, bio, and location in the list
    search_fields = ('user__username', 'location')  # Allow search by username or location

admin.site.register(Profile, ProfileAdmin)

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

# Register the Message model
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content', 'sent_at')  # Display sender, receiver, message, and time sent
    search_fields = ('sender__username', 'receiver__username', 'content')  # Search by sender, receiver, or message content
    list_filter = ('sent_at',)  # Filter by time sent

admin.site.register(Message, MessageAdmin)

# Register the Review model
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'rating', 'created_at')  # Display user, book, rating, and review date
    search_fields = ('user__username', 'book__title')  # Allow search by user and book title
    list_filter = ('rating',)  # Filter reviews by rating

admin.site.register(Review, ReviewAdmin)
admin.site.register(BookCategory)
