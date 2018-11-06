from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})
    # return HttpResponse("<marquee behavior=alternate><b>BURASI POST/INDEX SAYFASI</b</marquee>")

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }
    return render(request, 'post/detail.html', context)
    # return HttpResponse("<marquee behavior=alternate><b>BURASI POST/DETAIL SAYFASI</b</marquee>")

def post_create(request):

    if not request.user.is_authenticated():
        return Http404()



    # if request.method == "POST":
    #     print(request.POST)
    #
    # title = request.POST.get("title")
    # content = request.POST.get("metin")
    # Post.objects.create(title=title, content=content)

    # if request.method == "POST":
    #     # Formdan gelen bilgileri kaydet
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     # Formu kullanıcıya göster
    #     form = PostForm()

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save()
        # yeni eklenen kısım başı
        messages.success(request, 'Gönderim Başarılı!')
	    # yeni eklenen kısım sonu
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, "post/form.html", context)
    # return HttpResponse("<marquee behavior=alternate><b>BURASI POST/CREATE SAYFASI</b</marquee>")

def post_update(request, id):

    if not request.user.is_authenticated():
        return Http404()

    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post) # bir üstteki post
    if form.is_valid():
        form.save()
        messages.success(request, 'Güncelleme başarılı!')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form
    }

    return render(request, "post/form.html", context)
    # return HttpResponse("<marquee behavior=alternate><b>BURASI POST/UPDATE SAYFASI</b</marquee>")

def post_delete(request, id):

    if not request.user.is_authenticated():
        return Http404()

    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("post:index")
    # return HttpResponse("<marquee behavior=alternate><b>BURASI POST/DELETE SAYFASI</b</marquee>")
