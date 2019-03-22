from django import forms
from .models import Structure, Object, StructureTypeChoice


class StructureForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=200)
    name.widget.attrs.update({'class': 'form-control'})

    type = forms.ChoiceField(label='Type', choices=[(tag.value, tag.name) for tag in StructureTypeChoice])
    type.widget.attrs.update({'class': 'form-control'})

    parent = forms.ModelChoiceField(label='Parent', queryset=Structure.objects, required=False)
    parent.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Structure
        fields = ('name', 'type', 'parent')


class ObjectForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=200)
    name.widget.attrs.update({'class': 'form-control'})

    price = forms.CharField(label='Price')
    price.widget.attrs.update({'class': 'form-control'})

    structure = forms.ModelChoiceField(label='Room',
                                       queryset=Structure.objects.filter(type=StructureTypeChoice.Room.value))
    structure.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Object
        fields = ('name', 'price', 'structure')
