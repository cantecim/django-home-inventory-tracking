from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from ..models import Structure, Object

from .building import (
    BuildingCreateView, BuildingListView, BuildingUpdateView
)
from .apartment import (
    ApartmentCreateView, ApartmentListView, ApartmentUpdateView
)
from .room import (
    RoomCreateView, RoomListView, RoomUpdateView
)
from .object import (
    ObjectCreateView, ObjectListView, ObjectUpdateView
)


def home_page(request):
    return render(request, 'hit/index.html')


def structure_delete(request, pk):
    obj = get_object_or_404(Structure, pk=pk)
    obj.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def object_delete(request, pk):
    obj = get_object_or_404(Object, pk=pk)
    obj.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
