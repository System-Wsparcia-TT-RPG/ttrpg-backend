from web.api.models import *
from django.forms.models import model_to_dict
from django.db.models import Model

def get_fields(model: models.Model, fields: dict = None, ignore_models:list = []) -> dict:
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

"""
        "name": "Acid Splash",
        "tags": [
            "Conjuration",
            "cantrip"
        ],
        "type": "Conjuration cantrip",
        "ritual": false,
        "level": "cantrip",
        "school": "Conjuration",
        "casting_time": "1 action",
        "range": "60 feet",
        "components": 1,
        "duration": "Instantaneous",
        "description": "You hurl a bubble of acid. Choose one creature within range, or choose two creatures within range that are within 5 feet of each other. A target must succeed on a Dexterity saving throw or take 1d6 acid damage.\n\nThis spell's damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6)."
      }
"""
def create_spells_from_json(json_data: dict) -> Spell:

    components = Components.objects.create(**json_data['components'])
    del json_data['components']
    
    return Spell.objects.create(**json_data, components=components)

def get_spell(spell_id: int) -> Spell:
    return Spell.objects.get(pk=spell_id)

# Foreign Key

def get_spell_components(spell_id: int) -> Components:
    return Spell.objects.get(pk=spell_id).components







