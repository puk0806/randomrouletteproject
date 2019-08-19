from django.shortcuts import render,redirect

from .models import Goodmenu,Album,GoodComment
from django.views.generic import ListView, DetailView,UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from django.http import HttpResponseRedirect

from django.contrib import messages



# userlike import
from django.views.generic.base import View
from django.http import HttpResponseForbidden
from urllib.parse import urlparse

# Create your views here.

class AlbumList(ListView):
    model = Album

class AlbumDetail(DetailView):
    model = Album

class GoodmenuDetail(DetailView):
    model = Goodmenu

    def get_context_data(self, *args, **kwargs):
        context = super(GoodmenuDetail, self).get_context_data(*args, **kwargs)

        for key, value in self.request.GET.items():
            context[key] = value
        
        for key, value in self.request.POST.items():
            context[key] = value
        
        return context


class GoodMenuLike(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:    #로그인확인
            return HttpResponseForbidden()
        else:
            if 'goodmenu_id' in kwargs:
                goodmenu_id = kwargs['goodmenu_id']
                goodmenu = Goodmenu.objects.get(pk=goodmenu_id)
                user = request.user
                if user in goodmenu.like.all():
                    goodmenu.like.remove(user)
                else:
                    goodmenu.like.add(user)
            referer_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)


class GoodMenuFavorite(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:    #로그인확인
            return HttpResponseForbidden()
        else:
            if 'goodmenu_id' in kwargs:
                goodmenu_id = kwargs['goodmenu_id']
                goodmenu = Goodmenu.objects.get(pk=goodmenu_id)
                user = request.user
                if user in goodmenu.favorite.all():
                    goodmenu.favorite.remove(user)
                else:
                    goodmenu.favorite.add(user)
            referer_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)


class GoodMenuLikeList(ListView):
    model = Goodmenu
    template_name = 'goodmenu/goodmenu_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # 로그인확인
            messages.warning(request, '로그인을 먼저하세요')
            return HttpResponseRedirect('/')
        return super(GoodMenuLikeList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # 내가 좋아요한 글을 보여주
        user = self.request.user
        queryset = user.goodmenulike_post.all()
        return queryset


class GoodMenuFavoriteList(ListView):
    model = Goodmenu
    template_name = 'goodmenu/goodmenu_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # 로그인확인
            messages.warning(request, '로그인을 먼저하세요')
            return HttpResponseRedirect('/')
        return super(GoodMenuFavoriteList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # 내가 좋아요한 글을 보여주기
        user = self.request.user
        queryset = user.goodmenufavorite_post.all()
        return queryset

class GoodCommentDetail(DetailView):
    model = GoodComment

class GoodCommentCreate(LoginRequiredMixin,CreateView):
    model = GoodComment
    fields = ['goodmenucomment','goodstarcomment','title','body']
    template_name = 'goodmenu/comment_create.html'
    template_name_suffix = '_commentcreate'
    success_url = '/goodmenu/album/'

    def form_valid(self, form, *args, **kwargs):
        form.instance.goodauthorcomment = self.request.user 
        return super(GoodCommentCreate, self).form_valid(form)

class GoodCommentUpdate(UpdateView):
    model = GoodComment
    fields = ['goodstarcomment','title','body']
    template_name = 'goodmenu/comment_update.html'
    template_name_suffix = '_commentupdate'
    success_url = '/goodmenu/ablum/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.goodauthorcomment != request.user:
            messages.warning(request, '수정할 권한이 없습니다.')
            return HttpResponseRedirect('/goodmenu/album')
        else:
            return super(GoodCommentUpdate, self).dispatch(request, *args, **kwargs)

class GoodCommentDelete(DeleteView):
    model = GoodComment
    template_name = 'goodmenu/comment_delete.html'
    template_name_suffix = '_commentdelete'
    success_url = '/goodmenu/album/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.goodauthorcomment != request.user:
            messages.warning(request, '삭제할 권한이 없습니다.')
            return HttpResponseRedirect('/goodmenu/album')
        else:
            return super(GoodCommentDelete, self).dispatch(request, *args, **kwargs)