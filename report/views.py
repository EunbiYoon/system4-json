from django.shortcuts import render
from .models import Category, Post, Comment
from .forms import CommentForm
import json
from django.shortcuts import render
from django.conf import settings

def homeView(request):
    posts = list(Post.objects.all())[:3]
    context={
        'posts_set':posts,
    }
    return render(request, 'home.html', context)

def post_titles(request):
    titles=Post.objects.values_list('title', flat=True)
    return render(request,titles)

def detailView(request, slug, pk):
    #get the specific posts
    post = Post.objects.get(slug=slug, pk=pk)

    #get json data
    week_num=post.title
    json_path=settings.STATICFILES_DIRS[0]+'/json/data.json'
    with open(json_path,'r') as f:
        data=json.load(f)
    selected_data=data[week_num]
    value_data=selected_data["values"]
    label_data=selected_data["labels"]

    #comment function
    new_comment=None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=post)
        if comment_form.is_valid():
            name = request.user.username
            body = comment_form.cleaned_data['comment_body']
            new_comment = Comment(post=post, commenter_name=name, comment_body=body)
            new_comment.save()
        else:
            print('form is invalid')    
    else:
        comment_form = CommentForm()    

    context = {
        'post_detail':post,
        'new_comment': new_comment,
        'form_detail':comment_form,
        'labels':json.dumps(label_data),
        'data':json.dumps(value_data)
    }
    return render(request, 'detail.html', context)


def categoryView(request, slug):
    category=Category.objects.get(slug=slug)
    context={
        'category_pair':category
    }
    return render(request,'category.html', context)



