from .models import Category

def categories(request):
    """Add all categories to template context"""
    return {
        'categories': Category.objects.all()
    }
