from django.shortcuts import render
from django.views import View


# blog
class BlogView(View):
    def get(self, request):
        print("blog called")

        return render(request, 'web/blog_right_sidebar.html')


# blog detail
class BlogDetailView(View):
    def get(self, request):
        print("blog detail called")

        return render(request, 'web/blog_single_image.html')


# gallery
class GalleryView(View):
    def get(self, request):
        print("gallery called")

        return render(request, 'web/gallery.html')

