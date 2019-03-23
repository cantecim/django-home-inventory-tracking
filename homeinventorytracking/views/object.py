from django.urls import reverse_lazy, reverse
from django.views.generic.edit import UpdateView
from ..forms import ObjectForm
from .customized import CustomizedCreateView, CustomizedListView
from ..models import Object


class ObjectListView(CustomizedListView):
    model = Object
    template_name = 'hit/object_list.html'  # if not overridden looks for homeinventorytracking namespace
    page_title = 'Objects'
    action_url = 'object'

    def get_queryset(self):
        return Object.objects.filter(structure_id=self.kwargs['pk'])

    def get_action_url(self):
        return reverse("hit:object", kwargs={
            'building': self.kwargs['building'],
            'apartment': self.kwargs['apartment'],
            'room': self.kwargs['pk'],
            'pk': 0
        })[:-2]


class ObjectCreateView(CustomizedCreateView):
    model = Object
    template_name = 'hit/object_detail.html'
    page_title = 'Object'
    form_class = ObjectForm

    def get_success_url(self):
        return reverse_lazy('hit:objects', kwargs=self.kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['structure'].widget.attrs.update({
            'readonly': True
        })
        return context


class ObjectUpdateView(UpdateView):
    model = Object
    template_name = 'hit/object_detail.html'
    page_title = 'Room'
    form_class = ObjectForm

    def get_success_url(self):
        return reverse_lazy('hit:object', kwargs=self.kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.page_title
        context['is_update'] = True
        context['form'].fields['structure'].queryset = context['form'].fields['structure'].queryset.filter(
            parent_id=self.kwargs['apartment'])
        return context
