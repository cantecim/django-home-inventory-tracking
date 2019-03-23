from django.views import generic

from ..models import Structure, StructureTypeChoice


class CustomizedListView(generic.ListView):
    page_title = 'Title Not Set'
    action_url = 'building'
    structure_type = 'B'

    def get_childs_url(self):
        return ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.page_title
        context['action_url'] = self.get_action_url()
        context['childs_url'] = self.get_childs_url()
        context['structure_type'] = self.structure_type
        return context

    def get_action_url(self):
        return self.action_url

    def get_queryset(self):
        query = Structure.objects.order_by('id').filter(type=self.structure_type)
        if 'pk' in self.kwargs:
            query = query.filter(parent_id=self.kwargs['pk'])
        return query


class CustomizedCreateView(generic.edit.CreateView):
    page_title = 'Title Not Set'
    current_structure_type = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.page_title
        context['current_structure_type'] = self.current_structure_type
        if self.current_structure_type == StructureTypeChoice.Building.value:
            context['form'].fields['parent'].widget.attrs.update({
                'disabled': True
            })
        elif self.current_structure_type == StructureTypeChoice.Apartment.value:
            context['form'].fields['parent'].queryset = Structure.objects.filter(
                type=StructureTypeChoice.Building.value)
        elif self.current_structure_type == StructureTypeChoice.Room.value:
            context['form'].fields['parent'].queryset = Structure.objects.filter(
                type=StructureTypeChoice.Apartment.value)
        if 'pk' in self.kwargs:
            context['form'].initial.update({
                'parent' if 'parent' in context['form'].fields else 'structure': self.kwargs['pk']
            })
        return context


class CustomizedUpdateView(generic.edit.UpdateView):
    page_title = 'Title Not Set'
    current_structure_type = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.page_title
        context['is_update'] = True
        context['current_structure_type'] = self.current_structure_type
        context['form'].fields['type'].widget.attrs.update({
            'readonly': True
        })
        if self.object.type == StructureTypeChoice.Building.value:
            context['form'].fields['parent'].widget.attrs.update({
                'disabled': True
            })
        elif self.object.type == StructureTypeChoice.Apartment.value:
            context['form'].fields['parent'].queryset = Structure.objects.filter(
                type=StructureTypeChoice.Building.value)
        elif self.object.type == StructureTypeChoice.Room.value:
            context['form'].fields['parent'].queryset = Structure.objects.filter(
                type=StructureTypeChoice.Apartment.value,
            )
        return context
