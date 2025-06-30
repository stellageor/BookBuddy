from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

class BookCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Book Category'  # Singular name for the admin sidebar
        verbose_name_plural = 'Book Categories'  # Plural name for the admin sidebar

class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('unavailable', 'Not Available'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    condition = models.CharField(max_length=100)  # e.g., "New", "Good", etc.
    image = models.ImageField(upload_to='books/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)  # Location of the book
    is_available = models.BooleanField(default=True)  # Whether the book is available for lending
    # category = models.ForeignKey(BookCategory, related_name='books', on_delete=models.SET_NULL, null=True, blank=True)
    categories = models.ManyToManyField(BookCategory, related_name='books')  # Many-to-many relationship
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return self.title

class Borrowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # optional if you want to associate it
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} borrowing {self.book.title}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()  # Rating between 1 and 5 stars
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.book.title} by {self.user}'
