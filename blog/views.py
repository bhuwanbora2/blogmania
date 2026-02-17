from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import BlogPost, Category
from .forms import BlogPostForm

def home(request):
    """Home page displaying all published blogs categorized"""
    categories = Category.objects.all()
    featured_posts = BlogPost.objects.filter(status='published').order_by('-published_at')[:3]
    latest_posts = BlogPost.objects.filter(status='published').order_by('-published_at')[:6]
    
    # Get posts by category
    posts_by_category = {}
    for category in categories:
        posts = BlogPost.objects.filter(
            category=category, 
            status='published'
        ).order_by('-published_at')[:3]
        if posts.exists():
            posts_by_category[category] = posts
    
    context = {
        'featured_posts': featured_posts,
        'latest_posts': latest_posts,
        'posts_by_category': posts_by_category,
        'categories': categories,
    }
    return render(request, 'blog/home.html', context)

def blog_detail(request, slug):
    """Display individual blog post"""
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    post.views += 1
    post.save(update_fields=['views'])
    
    # Get related posts from same category
    related_posts = BlogPost.objects.filter(
        category=post.category,
        status='published'
    ).exclude(id=post.id).order_by('-published_at')[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'blog/detail.html', context)

def category_view(request, slug):
    """Display posts by category"""
    category = get_object_or_404(Category, slug=slug)
    posts_list = BlogPost.objects.filter(
        category=category,
        status='published'
    ).order_by('-published_at')
    
    paginator = Paginator(posts_list, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/category.html', context)

@login_required
def dashboard(request):
    """Unified Dashboard for managing blogs and admin access"""
    user_posts = BlogPost.objects.filter(author=request.user).order_by('-created_at')
    
    # Statistics
    total_posts = user_posts.count()
    published_posts = user_posts.filter(status='published').count()
    draft_posts = user_posts.filter(status='draft').count()
    total_views = sum(post.views for post in user_posts)
    
    # Category statistics
    categories = Category.objects.all()
    category_stats = []
    for category in categories:
        cat_posts = BlogPost.objects.filter(category=category, author=request.user)
        category_stats.append({
            'category': category,
            'count': cat_posts.count(),
            'published': cat_posts.filter(status='published').count(),
        })
    
    # All posts statistics (for admin view)
    all_posts_count = BlogPost.objects.count() if request.user.is_staff else 0
    all_categories_count = Category.objects.count()
    
    # Pagination
    paginator = Paginator(user_posts, 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    context = {
        'posts': posts,
        'total_posts': total_posts,
        'published_posts': published_posts,
        'draft_posts': draft_posts,
        'total_views': total_views,
        'category_stats': category_stats,
        'all_posts_count': all_posts_count,
        'all_categories_count': all_categories_count,
        'categories': categories,
        'is_staff': request.user.is_staff,
    }
    return render(request, 'blog/dashboard.html', context)

@login_required
def blog_create(request):
    """Create a new blog post"""
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Blog post created successfully!')
            return redirect('blog:dashboard')
    else:
        form = BlogPostForm()
    
    context = {
        'form': form,
        'title': 'Create New Blog Post',
    }
    return render(request, 'blog/blog_form.html', context)

@login_required
def blog_update(request, slug):
    """Update an existing blog post"""
    post = get_object_or_404(BlogPost, slug=slug, author=request.user)
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post updated successfully!')
            return redirect('blog:dashboard')
    else:
        form = BlogPostForm(instance=post)
    
    context = {
        'form': form,
        'post': post,
        'title': 'Update Blog Post',
    }
    return render(request, 'blog/blog_form.html', context)

@login_required
def blog_delete(request, slug):
    """Delete a blog post"""
    post = get_object_or_404(BlogPost, slug=slug, author=request.user)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Blog post deleted successfully!')
        return redirect('blog:dashboard')
    
    context = {
        'post': post,
    }
    return render(request, 'blog/blog_confirm_delete.html', context)
