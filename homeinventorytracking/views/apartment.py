from django.urls import reverse_lazy, reverse

from ..forms import StructureForm
from .customized import CustomizedCreateView, CustomizedListView, CustomizedUpdateView
from ..models import Structure, StructureTypeChoice


class ApartmentListView(CustomizedListView):
    model = Structure
    template_name = 'hit/structure_list.html'  # if not overridden looks for homeinventorytracking namespace
    page_title = 'Apartments'
    action_url = 'apartment'
    structure_type = StructureTypeChoice.Apartment.value

    def get_action_url(self):
        return reverse("hit:apartment", kwargs={
            'building': self.kwargs['pk'],
            'pk': 0
        })[:-2]


class ApartmentCreateView(CustomizedCreateView):
    model = Structure
    template_name = 'hit/structure_detail.html'
    page_title = 'Apartment'
    form_class = StructureForm
    current_structure_type = StructureTypeChoice.Apartment.value

    def get_success_url(self):
        return reverse_lazy('hit:apartments', kwargs={'pk': self.kwargs['pk']})


class ApartmentUpdateView(CustomizedUpdateView):
    model = Structure
    template_name = 'hit/structure_detail.html'
    page_title = 'Apartment'
    form_class = StructureForm
    current_structure_type = StructureTypeChoice.Apartment.value

    def get_success_url(self):
        return reverse_lazy('hit:apartment', kwargs=self.kwargs)
