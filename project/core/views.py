from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Book, BookCategory, Borrowing, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .forms import AccountSettingsForm, CustomPasswordChangeForm, CustomUserCreationForm, ProfileSettingsForm, ReviewForm, BookForm, BorrowingForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Avg

# Create your views here.

# User Registration View
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Create empty UserProfile
            UserProfile.objects.create(user=user)

            login(request, user)
            messages.success(request, "Welcome to BookBuddy!")
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if already logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to dashboard or home after login
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'core/login.html')

# Book List View
def book_list(request):
    books = Book.objects.all()  # Filter by user's location, availability, etc.
    return render(request, 'core/book_search.html', {'books': books})

# Book Search View
def book_search(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')  # Get the selected category
    books = Book.objects.all()

    category = None
    if category_id:
        try:
            category = BookCategory.objects.get(id=category_id)
        except BookCategory.DoesNotExist:
            category = None
    categories = BookCategory.objects.all()

    if query:
        books = books.filter(title__icontains=query) | books.filter(author__icontains=query)

    if category_id:
        books = books.filter(categories=category_id)

    return render(request, 'core/book_search.html', 
        {
            'books': books, 
            'query': query,
            'category': category,
            'categories': categories,
        })

def book_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    # Handle review form submission
    if request.method == 'POST' and request.user.is_authenticated:
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            print(review_form.cleaned_data)
            print(book)
            print(request.user)
            review = review_form.save(commit=False)
            review.book = book
            review.user = request.user
            print(review)
            review.save()
            return redirect('book_details', book_id=book.id)  # Redirect to the same page to show the new review
    else:
        review_form = ReviewForm()

    average_rating = book.review_set.aggregate(avg_rating=Avg('rating'))['avg_rating']

    return render(request, 'core/book_details.html', {
        'book': book,
        'reviews': book.review_set.all(),  # Get all reviews for the book
        'review_form': review_form,
        'average_rating': average_rating
    })
    
    
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Ensure that only the owner of the book can edit it
    if book.user != request.user:
        return redirect('book_details', book_id=book.id)  # Redirect if not the owner

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)  # Include request.FILES for image upload

        if form.is_valid():
            form.save()
            messages.success(request, 'Book saved successfully!')
            return redirect('book_details', book_id=book.id)  # Redirect to the book's detail page after editing
    else:
        form = BookForm(instance=book)

    categories = BookCategory.objects.all()
    return render(request, 'core/add_edit_book.html', {'form': form, 'book': book, 'categories': categories, 'action': 'Edit'})

# Account Settings View
@login_required
def change_password(request):
    user = request.user

    if request.method == 'POST':
        # Handle changes to username, email, and password
        password_form = CustomPasswordChangeForm(user, request.POST)
        
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, password_form.user)  # Keep the user logged in after changing password
            messages.success(request, "Password changed successfully!")
            return redirect('change_password')  # Redirect after password change
    else:
        password_form = CustomPasswordChangeForm(user)

    return render(request, 'core/change_password.html', {
        'password_form': password_form
    })

@login_required
def account_settings(request):
    user = request.user
    profile = user.userprofile

    if request.method == 'POST':
        user_form = AccountSettingsForm(request.POST, instance=user)
        profile_form = ProfileSettingsForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile changed successfully!")
            return redirect('account_settings')
    else:
        user_form = AccountSettingsForm(instance=user)
        profile_form = ProfileSettingsForm(instance=profile)

    return render(request, 'core/account_settings.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

# View for My Books page
@login_required
def my_books(request):
    # Get all books related to the logged-in user
    books = Book.objects.filter(user=request.user)
    return render(request, 'core/my_books.html', {'books': books})


# View to add a new book
@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user  # Associate the book with the logged-in user
            book.save()
            messages.success(request, "Book added successfully!")
            return redirect('my_books')  # Redirect to the My Books page
        print(form.errors)
    else:
        form = BookForm()

    categories = BookCategory.objects.all()
    return render(request, 'core/add_edit_book.html', {'form': form, 'categories': categories, 'action': 'Add'})


# View to delete a book
@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)  # Ensure the user is the owner
    if request.method == 'POST':
        book.delete()
        messages.success(request, "Book deleted successfully!")
        return redirect('my_books')  # Redirect to the My Books page after deletion
    return render(request, 'core/delete_book.html', {'book': book})

@login_required
def create_borrowing(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BorrowingForm(request.POST)
        if form.is_valid():
            borrowing = form.save(commit=False)
            borrowing.user = request.user
            borrowing.book = book
            borrowing.save()
            
            
            book.status = 'borrowed'
            book.save()
            messages.success(request, f"You've successfully borrowed '{ book.title }'. We'll contact you soon with pickup details.")
            return redirect('book_details', book_id=book.id)
    else:
        form = BorrowingForm()

    return render(request, 'core/borrowing_form.html', {'form': form, 'book': book})

@login_required
def my_borrowings_view(request):
    user = request.user

    # 1. Borrowing requests made by others to books I own
    incoming_requests = Borrowing.objects.filter(book__user=user).select_related('user', 'book')

    # 2. My own borrowing requests
    my_requests = Borrowing.objects.filter(user=user).select_related('book')

    return render(request, 'core/my_borrowings.html', {
        'incoming_requests': incoming_requests,
        'my_requests': my_requests,
    })

@login_required
def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.user == book.user or Borrowing.objects.filter(book=book, user=request.user).exists():
        book.status = 'available'
        book.save()

    messages.success(request, f"Book is now available.")
    return redirect('my_borrowings')
