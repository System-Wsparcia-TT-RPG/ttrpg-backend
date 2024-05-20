from web.api.models import *


def get_fields(model: models.Model, fields: dict = None, ignore_models: list = []) -> dict:
    if not fields:
        fields = {}
        for f in model._meta.fields:
            fields[f.name] = getattr(model, f.name)

        for f in model._meta.many_to_many:
            fields[f.name] = get_many_to_many(getattr(model, f.name))

    for name, value in fields.items():
        if not isinstance(value, models.Model):
            # skip non-relational (ForeignKey) fields            
            continue
        fields[name] = getattr(value, "pk") if name in ignore_models else get_fields(value)
    return fields


def get_many_to_many(many_to_many) -> list:
    ret_list = []
    for val in many_to_many.all():
        ret_list.append(get_fields(val))
    return ret_list


def create_spells_from_json(json_data: dict) -> Spell:
    new_components = Components.objects.create(**json_data['components'])
    del json_data['components']

    new_classes = []
    for class_name in json_data['classes']:
        new_classes.append(Class.objects.get_or_create(name=class_name))
    del json_data['classes']

    return Spell.objects.create(**json_data, components=new_components, classes=new_classes)


def get_spell(spell_id: int) -> Spell:
    return Spell.objects.get(pk=spell_id)


# Foreign Key

def get_spell_components(spell_id: int) -> Components:
    return Spell.objects.get(pk=spell_id).components
