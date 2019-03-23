from django.urls import reverse_lazy, reverse

from ..forms import StructureForm
from .customized import CustomizedCreateView, CustomizedListView, CustomizedUpdateView
from ..models import Structure, StructureTypeChoice


class RoomListView(CustomizedListView):
    model = Structure
    template_name = 'hit/structure_list.html'  # if not overridden looks for homeinventorytracking namespace
    page_title = 'Rooms'
    action_url = 'room'
    structure_type = StructureTypeChoice.Room.value

    def get_action_url(self):
        return reverse("hit:room", kwargs={
            'building': self.kwargs['building'],
            'apartment': self.kwargs['pk'],
            'pk': 0
        })[:-2]


class RoomCreateView(CustomizedCreateView):
    model = Structure
    template_name = 'hit/structure_detail.html'
    page_title = 'Room'
    form_class = StructureForm
    current_structure_type = StructureTypeChoice.Room.value

    def get_success_url(self):
        return reverse_lazy('hit:rooms', kwargs={'building': self.kwargs['building'], 'pk': self.kwargs['pk']})


class RoomUpdateView(CustomizedUpdateView):
    model = Structure
    template_name = 'hit/structure_detail.html'
    page_title = 'Room'
    form_class = StructureForm
    current_structure_type = StructureTypeChoice.Room.value

    def get_success_url(self):
        return reverse_lazy('hit:room', kwargs=self.kwargs)
