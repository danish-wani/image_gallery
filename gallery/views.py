# __author__ = 'danish-wani'


from django.views.generic import (CreateView, DeleteView, ListView)
from .forms import GalleryForm
from .models import Gallery
from django.urls import reverse_lazy


class GalleryHome(ListView):

    template_name = 'gallery/home.html'
    queryset = Gallery.objects.all()
    paginate_by = 8

    def get_context_data(self, **kwargs):
        """
            Update default context data with form and selected category if needed
        """
        context = super(GalleryHome, self).get_context_data(**kwargs)
        context.update({'form': GalleryForm()})
        if self.request.GET.get('category'):
            category = self.request.GET.get('category')
            context.update({'selected_category': category})
        return context

    def get_queryset(self):
        """
            To preserve selected category on subsequent pages for paginator
        """
        if self.request.GET.copy().get('category'):
            category = self.request.GET.get('category')
            return self.queryset.filter(category=category)

        return self.queryset


class AddImageView(CreateView):
    model = Gallery
    template_name = 'gallery/home.html'
    success_url = reverse_lazy('gallery_home')
    fields = '__all__'


class DeleteImageView(DeleteView):
    model = Gallery
    success_url = reverse_lazy('gallery_home')
