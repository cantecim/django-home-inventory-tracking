from django.urls import reverse_lazy, reverse

from ..forms import StructureForm
from .customized import CustomizedCreateView, CustomizedListView, CustomizedUpdateView
from ..models import Structure, StructureTypeChoice


class BuildingListView(CustomizedListView):
    model = Structure
    template_name = 'hit/structure_list.html'  # if not overridden looks for homeinventorytracking namespace
    page_title = 'Buildings'
    structure_type = StructureTypeChoice.Building.value

    def get_action_url(self):
        return reverse("hit:building", kwargs={
            'pk': 0
        })[:-2]


class BuildingCreateView(CustomizedCreateView):
    model = Structure
    template_name = 'hit/structure_detail.html'
    page_title = 'Building'
    form_class = StructureForm
    success_url = reverse_lazy('hit:buildings')
    current_structure_type = StructureTypeChoice.Building.value


class BuildingUpdateView(CustomizedUpdateView):
    model = Structure
    template_name = 'hit/structure_detail.html'
    page_title = 'Building'
    form_class = StructureForm
    current_structure_type = StructureTypeChoice.Building.value

    def get_success_url(self):
        return reverse_lazy('hit:building', kwargs=self.kwargs)
