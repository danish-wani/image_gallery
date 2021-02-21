from django.views.generic import (TemplateView, CreateView, DeleteView, ListView)
from .forms import GalleryForm
from .models import Gallery
from django.urls import reverse_lazy


class GalleryHome(ListView):
    """

    """

    template_name = 'gallery/home.html'
    queryset = Gallery.objects.all()
    paginate_by = 4

    def get_context_data(self, **kwargs):
        """

        """
        context = super(GalleryHome, self).get_context_data(**kwargs)
        context.update({'form': GalleryForm()})
        if self.request.GET.copy().get('category'):
            category = self.request.GET.copy().get('category')
            context.update({'selected_category': category})
        return context

    def get(self, request, *args, **kwargs):
        """

        """
        if request.GET.copy().get('category'):
            category = request.GET.copy().get('category')
            self.queryset = self.queryset.filter(category=category)
        return super(GalleryHome, self).get(request, *args, **kwargs)


class AddImageView(CreateView):
    model = Gallery
    template_name = 'gallery/home.html'
    success_url = reverse_lazy('gallery_home')
    fields = '__all__'


class DeleteImageView(DeleteView):
    model = Gallery
    success_url = reverse_lazy('gallery_home')
