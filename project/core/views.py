from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Book, BookCategory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .forms import AccountSettingsForm, CustomPasswordChangeForm, ProfileSettingsForm, ReviewForm, BookForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

# User Registration View
def register(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if already logged in
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the book listing page after registration
    else:
        form = UserCreationForm()
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
    category = request.GET.get('category', '')  # Get the selected category
    books = Book.objects.all()
    
    categories = BookCategory.objects.all()

    if query:
        books = books.filter(title__icontains=query) | books.filter(author__icontains=query)

    if category:
        books = books.filter(categories=category)

    return render(request, 'core/book_search.html', {'books': books, 'query': query, 'category': category, 'categories': categories})

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

    return render(request, 'core/book_details.html', {
        'book': book,
        'reviews': book.review_set.all(),  # Get all reviews for the book
        'review_form': review_form
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
            return redirect('book_details', book_id=book.id)  # Redirect to the book's detail page after editing
    else:
        form = BookForm(instance=book)


    categories = BookCategory.objects.all()

    return render(request, 'core/add_edit_book.html', {'form': form, 'book': book, 'categories': categories, 'action': 'Edit'})

# Account Settings View
@login_required
def account_settings(request):
    if request.method == 'POST':
        # Handle changes to username, email, and password
        form = AccountSettingsForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            return redirect('account_settings')  # Redirect after successful update
        
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, password_form.user)  # Keep the user logged in after changing password
            return redirect('account_settings')  # Redirect after password change
    else:
        form = AccountSettingsForm(instance=request.user)
        password_form = CustomPasswordChangeForm(request.user)

    return render(request, 'core/account_settings.html', {
        'form': form,
        'password_form': password_form
    })

# Profile Settings View
@login_required
def profile_settings(request):
    if request.method == 'POST':
        # Handle changes to bio, location, etc.
        form = ProfileSettingsForm(request.POST, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect('profile_settings')  # Redirect after successful update

    else:
        form = ProfileSettingsForm(instance=request.user.profile)

    return render(request, 'core/profile_settings.html', {'form': form})

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
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user  # Associate the book with the logged-in user
            book.save()
            return redirect('my_books')  # Redirect to the My Books page
    else:
        form = BookForm()
    return render(request, 'core/add_edit_book.html', {'form': form, 'action': 'Add'})


# View to delete a book
@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)  # Ensure the user is the owner
    if request.method == 'POST':
        book.delete()
        return redirect('my_books')  # Redirect to the My Books page after deletion
    return render(request, 'core/delete_book.html', {'book': book})
