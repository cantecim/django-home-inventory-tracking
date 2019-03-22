from enum import Enum
from django.db import models
from computedfields.models import ComputedFieldsModel, computed


class StructureTypeChoice(Enum):
    Building = "B"
    Apartment = "A"
    Room = "R"


class Structure(ComputedFieldsModel):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=[(tag.value, tag.name) for tag in StructureTypeChoice])
    parent = models.ForeignKey("Structure", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    @computed(
        models.DecimalField(max_digits=12, decimal_places=2, default=0),
        depends=['object_set#price']
    )
    def object_value(self):
        if self.type != StructureTypeChoice.Room.value:
            return sum([c.object_value for c in self.structure_set.all()])
        else:
            return sum([s.price for s in self.object_set.all()])

    def find_rooms(self, structures):
        result = []
        for s in structures:
            if s.type == StructureTypeChoice.Room.value:
                result.append(s)
            else:
                result += self.find_rooms(s.structure_set.all())
        return result

    def save(self, *args, **kwargs):
        result = super(Structure, self).save(*args, **kwargs)
        if self.parent:
            if self.type == StructureTypeChoice.Apartment.value:
                for r in self.structure_set.all():
                    if r.compute('object_value') != r.object_value:
                        r.save()
            self.parent.save()
        return result


class Object(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE)
