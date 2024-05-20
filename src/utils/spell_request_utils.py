from web.api.models import *

from utils.character_request_utils import get_fields, get_many_to_many


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
