from django.shortcuts import render, HttpResponse

def post_index(request):
    return HttpResponse("<marquee behavior=alternate><b>BURASI POST/INDEX SAYFASI</b</marquee>")

def post_detail(request):
    return HttpResponse("<marquee behavior=alternate><b>BURASI POST/DETAIL SAYFASI</b</marquee>")

def post_create(request):
    return HttpResponse("<marquee behavior=alternate><b>BURASI POST/CREATE SAYFASI</b</marquee>")

def post_update(request):
    return HttpResponse("<marquee behavior=alternate><b>BURASI POST/UPDATE SAYFASI</b</marquee>")

def post_delete(request):
    return HttpResponse("<marquee behavior=alternate><b>BURASI POST/DELETE SAYFASI</b</marquee>")
