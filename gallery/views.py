from django.views.generic import (TemplateView, CreateView, DeleteView, ListView)
from .forms import GalleryForm
from .models import Gallery
from django.urls import reverse_lazy


class GalleryHome(ListView):
    """

    """
    template_name = 'gallery/home.html'
    queryset = Gallery.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        """

        """
        context = super(GalleryHome, self).get_context_data(**kwargs)
        context.update({'form': GalleryForm})
        return context


class AddImageView(CreateView):
    model = Gallery
    form_class = GalleryForm
    success_url = reverse_lazy('gallery_home')


class DeleteImageView(DeleteView):
    model = Gallery
    success_url = reverse_lazy('gallery_home')