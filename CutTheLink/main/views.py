from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib import messages
from .forms import AddLinkForm
from .models import Links
from django.conf import settings


def HomeView(request):
    return render(request, 'main/home.html', {'advert_links': list(reversed(Links.objects.all()))[:15]})


def AboutUs(request):
    return render(request, 'main/about.html', {'advert_links': list(reversed(Links.objects.all()))[:15]})


class AddLinkView(LoginRequiredMixin, CreateView, ListView):
    model = Links
    template_name = 'main/links_form.html'
    fields = ['title', 'short', 'long', 'user']
    context_object_name = "links"

    form = AddLinkForm()

    def post(self, request, *args, **kwargs):
        post = request.POST.copy()
        post['user'] = request.user
        request.POST = post
        form = AddLinkForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f'Ссылка "{title}" успешно добавлена!')
            return redirect('add-link')
        else:
            return render(request, self.template_name, {
                'form': form,
                'links': Links.objects.filter(user=request.user),
                'host': settings.SITE_URL,
                'advert_links': list(reversed(Links.objects.all()))[:15]
            })

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(AddLinkView, self).get_context_data(**kwargs)
        ctx['form'] = self.form
        ctx['host'] = settings.SITE_URL
        ctx['advert_links'] = list(reversed(Links.objects.all()))[:15]
        return ctx


def FollowLink(request, slug):
    link = Links.objects.filter(short=slug).first()
    if link:
        return redirect(link.long)
    else:
        return render(request, 'main/no_link.html', {'advert_links': list(reversed(Links.objects.all()))[:15]})
