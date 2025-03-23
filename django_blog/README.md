# Django Blog Authentication System

## Features
- User Registration
- User Login & Logout
- Profile Viewing & Editing

## Comment Feature
This feature allows users to add comments to blog posts.

### Features:
- Users can read comments on a post.
- Authenticated users can create new comments.
- Comment authors can edit or delete their own comments.
- Secure permissions using Django's LoginRequiredMixin and UserPassesTestMixin.

### URLs:
- `/post/<int:post_id>/comment/new/` - Add a new comment
- `/comment/<int:pk>/edit/` - Edit a comment
- `/comment/<int:pk>/delete/` - Delete a comment

### How to Use:
1. Log in to add a comment.
2. Use the form on the post detail page to submit a comment.
3. If you're the author, you can edit or delete your comment using the links provided.

