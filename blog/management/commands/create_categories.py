from django.core.management.base import BaseCommand
from blog.models import Category

class Command(BaseCommand):
    help = 'Creates default categories for the blog'

    def handle(self, *args, **options):
        categories = [
            {'name': 'Technology', 'slug': 'technology', 'description': 'Posts about technology, programming, and software'},
            {'name': 'Agricultural', 'slug': 'agricultural', 'description': 'Posts about agriculture, farming, and crops'},
            {'name': 'Design', 'slug': 'design', 'description': 'Posts about design, UI/UX, and creativity'},
            {'name': 'AI', 'slug': 'ai', 'description': 'Posts about artificial intelligence and machine learning'},
            {'name': 'Python', 'slug': 'python', 'description': 'Posts about Python programming'},
        ]
        
        created_count = 0
        for cat_data in categories:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={
                    'name': cat_data['name'],
                    'description': cat_data['description']
                }
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created category: {category.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Category already exists: {category.name}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'\n{created_count} new categories created!')
        )
