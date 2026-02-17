# Blog Posting System with CRUD Operations

A full-featured blog posting system built with Django, featuring CRUD operations, dashboard management, category-based organization, and advanced CSS styling.

## Features

✅ **Full CRUD Operations**
- Create new blog posts
- Read/view blog posts
- Update existing blog posts
- Delete blog posts

✅ **Dashboard**
- View all your blog posts
- Statistics (Total posts, Published, Drafts, Total views)
- Quick actions (Edit, Delete, View)
- Pagination support

✅ **Category Management**
- Organize posts by categories (Technology, Agricultural, etc.)
- Category-based filtering
- Category pages with pagination

✅ **Advanced Features**
- Featured images for blog posts
- Post status (Draft/Published)
- View counter
- Timestamps (Created, Updated, Published)
- Related posts
- Responsive design

✅ **Advanced CSS Styling**
- Modern gradient designs
- Smooth animations and transitions
- Hover effects
- Card-based layouts
- Mobile responsive

## Setup Instructions

### 1. Install Dependencies
Make sure you have Django installed:
```bash
pip install django
```

### 2. Run Migrations
```bash
python manage.py migrate
```

### 3. Create a Superuser
```bash
python manage.py createsuperuser
```

### 4. Create Categories
1. Log in to the admin panel at `/admin/`
2. Go to "Categories" section
3. Add categories like:
   - Technology
   - Agricultural
   - Design
   - AI
   - Python
   - etc.

### 5. Run the Development Server
```bash
python manage.py runserver
```

### 6. Access the Application
- **Home Page**: `http://127.0.0.1:8000/`
- **Dashboard**: `http://127.0.0.1:8000/dashboard/` (requires login)
- **Admin Panel**: `http://127.0.0.1:8000/admin/`

## Usage Guide

### Creating a Blog Post
1. Log in to your account
2. Navigate to Dashboard
3. Click "New Post" button
4. Fill in the form:
   - Title
   - Slug (URL-friendly version)
   - Category
   - Content
   - Excerpt (optional)
   - Featured Image (optional)
   - Status (Draft or Published)
5. Click "Save Post"

### Updating a Blog Post
1. Go to Dashboard
2. Find the post you want to edit
3. Click the Edit icon (pencil)
4. Make your changes
5. Click "Save Post"

### Deleting a Blog Post
1. Go to Dashboard
2. Find the post you want to delete
3. Click the Delete icon (trash)
4. Confirm deletion

### Viewing Posts by Category
- Click on any category in the navigation menu
- Or visit `/category/<category-slug>/`

## Project Structure

```
blog_main/
├── blog/                    # Main blog app
│   ├── models.py           # BlogPost and Category models
│   ├── views.py            # CRUD views
│   ├── forms.py            # Blog post form
│   ├── urls.py             # URL routing
│   ├── admin.py            # Admin configuration
│   ├── context_processors.py # Categories context
│   └── templates/
│       └── blog/
│           ├── base.html           # Base template
│           ├── home.html          # Home page
│           ├── dashboard.html     # Dashboard
│           ├── blog_form.html     # Create/Update form
│           ├── detail.html         # Post detail page
│           ├── category.html      # Category page
│           └── blog_confirm_delete.html # Delete confirmation
├── blog_main/
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   └── static/
│       └── css/
│           └── blog.css     # Advanced CSS styling
└── media/                   # User uploaded files (created automatically)
```

## Models

### Category
- `name`: Category name
- `slug`: URL-friendly identifier
- `description`: Optional description

### BlogPost
- `title`: Post title
- `slug`: URL-friendly identifier
- `author`: Foreign key to User
- `category`: Foreign key to Category
- `content`: Main post content
- `excerpt`: Short description
- `featured_image`: Optional image
- `status`: Draft or Published
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp
- `published_at`: Publication timestamp
- `views`: View counter

## URLs

- `/` - Home page
- `/post/<slug>/` - Blog post detail
- `/category/<slug>/` - Posts by category
- `/dashboard/` - User dashboard
- `/create/` - Create new post
- `/update/<slug>/` - Update post
- `/delete/<slug>/` - Delete post

## Styling Features

The CSS includes:
- CSS Variables for easy theming
- Gradient backgrounds
- Smooth transitions and animations
- Hover effects
- Card-based layouts
- Responsive design
- Modern typography
- Custom shadows and borders

## Notes

- Make sure to create categories before creating blog posts
- Only published posts appear on the home page
- Users can only edit/delete their own posts
- Images are stored in `media/blog_images/` directory

## Future Enhancements

Potential features to add:
- User authentication system (separate from admin)
- Comments system
- Tags in addition to categories
- Search functionality
- Rich text editor (WYSIWYG)
- Image optimization
- SEO meta tags
- RSS feed
