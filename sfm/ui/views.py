from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models import Count
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, \
    FormView
from django.views.generic.edit import ModelFormMixin
from django.views.generic.base import ContextMixin
from django.views.generic.list import ListView

from braces.views import LoginRequiredMixin

from .forms import CollectionForm, SeedSetForm, SeedForm, CredentialForm, \
    SeedSetSelectTypeForm
from .models import Collection, SeedSet, Seed, Credential
from utils import schedule_harvest


class CollectionListView(LoginRequiredMixin, ListView):
    model = Collection
    template_name = 'ui/collection_list.html'
    paginate_by = 20
    allow_empty = True
    paginate_orphans = 0

    def get_context_data(self, **kwargs):
        context = super(CollectionListView, self).get_context_data(**kwargs)
        context['collection_list'] = Collection.objects.filter(
            group__in=self.request.user.groups.all()).annotate(
            num_seedsets=Count('seed_sets')).order_by(
            '-is_active', 'date_updated')
        return context


class CollectionDetailView(LoginRequiredMixin, DetailView):
    model = Collection
    template_name = 'ui/collection_detail.html'


class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'ui/collection_create.html'
    success_url = reverse_lazy('collection_list')


class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'ui/collection_update.html'

    def get_success_url(self):
        return reverse("collection_detail", args=(self.object.pk,))


class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'ui/collection_delete.html'
    success_url = reverse_lazy('collection_list')


class SeedSetSelectTypeView(FormView):
    form_class = SeedSetSelectTypeForm
    template_name = 'ui/seedset_type_select.html'

    def form_valid(self, form):
        seed_set_type = form.cleaned_data['seed_set_type']
        self.success_url = reverse('seedset_create',
                                   kwargs={'seed_set_type': seed_set_type})
        return super(FormView, self).form_valid(form)


class SeedSetListView(ListView):
    model = SeedSet
    template_name = 'ui/seedset_list.html'
    paginate_by = 20
    allow_empty = True
    paginate_orphans = 0


class SeedSetDetailView(DetailView):
    model = SeedSet
    template_name = 'ui/seedset_detail.html'


class SeedSetCreateView(CreateView, ContextMixin):
    model = SeedSet
    form_class = SeedSetForm
    template_name = 'ui/seedset_create.html'
    success_url = reverse_lazy('seedset_list')

    def get_context_data(self, **kwargs):
        seed_set_type = self.kwargs['seed_set_type']
        # We can pass more here if we need
        return {'seed_set_type': seed_set_type}


class SeedSetUpdateView(UpdateView):
    model = SeedSet
    form_class = SeedSetForm
    template_name = 'ui/seedset_update.html'

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        # To save data to database
        self.object = form.save()
        # To schedule harvest message for the current id
        d = self.get_object().id
        schedule = SeedSet.objects.filter(id=d).values(
            'schedule')[0]["schedule"]
        start_date = SeedSet.objects.filter(id=d).values(
            'start_date')[0]["start_date"]
        if start_date:
            # s = start_date.strftime('%Y-%m-%d')
            s = start_date.strftime('%Y-%m-%d %H:%M:%S')
        else:
            s = '2000-01-01'
        end_date = SeedSet.objects.filter(id=d).values(
            'end_date')[0]["end_date"]
        if end_date:
            # e = end_date.strftime('%Y-%m-%d')
            e = end_date.strftime('%Y-%m-%d %H:%M:%S')
        else:
            e = '2050-01-01'
        schedule_harvest(d, schedule, s, e)

        return super(ModelFormMixin, self).form_valid(form)

    def get_success_url(self):
        return reverse("seedset_detail", args=(self.object.pk,))


class SeedSetDeleteView(DeleteView):
    model = SeedSet
    template_name = 'ui/seedset_delete.html'
    success_url = reverse_lazy('seedset_list')


class SeedListView(ListView):
    model = Seed
    template_name = 'ui/seed_list.html'
    paginate_by = 20
    allow_empty = True
    paginate_orphans = 0


class SeedDetailView(DetailView):
    model = Seed
    template_name = 'ui/seed_detail.html'


class SeedCreateView(CreateView):
    model = Seed
    form_class = SeedForm
    template_name = 'ui/seed_create.html'
    success_url = reverse_lazy('seed_list')


class SeedUpdateView(UpdateView):
    model = Seed
    form_class = SeedForm
    template_name = 'ui/seed_update.html'

    def get_success_url(self):
        return reverse("seed_detail", args=(self.object.pk,))


class SeedDeleteView(DeleteView):
    model = Seed
    template_name = 'ui/seed_delete.html'
    success_url = reverse_lazy('seed_list')


class CredentialDetailView(LoginRequiredMixin, DetailView):
    model = Credential
    template_name = 'ui/credential_detail.html'


class CredentialCreateView(LoginRequiredMixin, CreateView):
    model = Credential
    form_class = CredentialForm
    template_name = 'ui/credential_create.html'
    success_url = reverse_lazy('credential_detail')


class CredentialListView(LoginRequiredMixin, ListView):
    model = Credential
    template_name = 'ui/credential_list.html'
    allow_empty = True
