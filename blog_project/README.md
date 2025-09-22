Django Blog Application
1. Create a Django Project
Project Name: blog_project
App Name: blog
2. Define Models
In the models.py file of the blog app, define the following model:

Post
Fields:
title - CharField: Title of the blog post.
content - TextField: Content of the blog post.
created_at - DateTimeField: Date and time when the post was created.
category - CharField: The category associated with the post.
3. Run Migrations
Generate and apply migrations to create the corresponding tables in the database:

python manage.py makemigrations
python manage.py migrate
4. Query the Database
In the Django shell or within a view, perform the following queries:

Create instances:

Create a few instance of Post.
Filter posts by category:

Filter posts that belong to a specific category.