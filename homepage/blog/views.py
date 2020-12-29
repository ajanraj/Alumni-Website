from django.views import generic
from .models import Post
from django.contrib import messages
from django.shortcuts import render, redirect
from homepage.models import CustomUser as User
from homepage.blog.models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'frontend/blog/index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'frontend/blog/post_detail.html'


def addpost(request):
    if request.method == "POST":
        user = User.objects.filter(pk=request.user.id)

        if not user:
            messages.error(request, "Login to Continue!")
            return redirect('frontend.index')

        else:
            user = user.get()

        title = request.POST['title']
        slug = title.replace(" ", "-")
        slug = slug.replace(".", "-")
        content = request.POST['content']
        status = request.POST['status']
        try:
            post = Post(title=title, slug=slug, content=content,
                        status=status, author=user)
            post.save()
        except Exception as e:
            messages.success(
                request, e)
            return redirect("frontend.blog.addpost")

        messages.success(request, "Signed up successfully")
        return redirect("frontend.blog.index")

    else:
        # return redirect("admin.song.add")
        user = User.objects.filter(pk=request.user.id)

        if not user:
            messages.error(request, "Login to Continue!")
            return redirect('frontend.index')

        else:
            user = user.get()
        return render(request, 'frontend/blog/addpost.html', {'user': user})
