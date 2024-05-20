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


def create_character_from_json(json_data: dict) -> Character:
    new_player = Player.objects.create(**json_data['player'])
    del json_data['player']

    race_senses = Senses.objects.create(**json_data['race']['senses'])
    del json_data['race']['senses']

    race_trait_list = []
    for race_json_trait in json_data['race']['traits']:
        race_trait_list.append(Trait.objects.create(**race_json_trait))

    del json_data['race']['traits']

    race_action_list = []
    for race_json_action in json_data['race']['actions']:
        damage_dice = DamageDice.objects.create(**race_json_action['damage_dice'])
        del race_json_action['damage_dice']
        race_action_list.append(Action.objects.create(**race_json_action, damage_dice=damage_dice))

    del json_data['race']['actions']

    new_race = Race.objects.create(**json_data['race'], senses=race_senses)

    new_race.traits.set(race_trait_list)
    new_race.actions.set(race_action_list)
    del json_data['race']

    char_classes_list = []

    for class_json in json_data['classes']:
        feature_list = []
        for feature_json in class_json['features']:
            feature_list.append(Feature.objects.create(**feature_json))

        del class_json['features']

        new_class = Class.objects.create(**class_json)
        new_class.features.set(feature_list)
        char_classes_list.append(new_class)

    del json_data['classes']

    new_background = Background.objects.create(**json_data['background'])
    del json_data['background']

    new_details = Details.objects.create(**json_data['details'])
    del json_data['details']

    character_feats_list = []
    for feat in json_data['feats']:
        character_feats_list.append(Feat.objects.create(**feat))
    del json_data['feats']

    character_spells_list = []
    for spell in json_data['spells']:
        character_spells_list.append(Spell.objects.create(**spell))
    del json_data['spells']

    character_weapons_list = []
    for weapon in json_data['weapons']:
        damage_dice = DamageDice.objects.create(**weapon['damage_dice'])
        del weapon['damage_dice']
        character_weapons_list.append(Weapon.objects.create(**weapon, damage_dice=damage_dice))
    del json_data['weapons']

    character_equipment_list = []
    for eq in json_data['equipment']:
        character_equipment_list.append(Equipment.objects.create(**eq))
    del json_data['equipment']

    new_treasure = Treasure.objects.create(**json_data['treasure'])
    del json_data['treasure']

    new_ability_scores = AbilityScores.objects.create(**json_data['Ability Scores'])
    del json_data['Ability Scores']

    new_skills = Skills.objects.create(**json_data['Skills'])
    del json_data['Skills']

    new_saving_throws = SavingThrows.objects.create(**json_data['Saving Throws'])
    del json_data['Saving Throws']

    new_combat_death_saves = DeathSaves.objects.create(**json_data['Combat']['Death Saves'])
    del json_data['Combat']['Death Saves']

    new_combat = CombatStats.objects.create(**json_data['Combat'], death_saves=new_combat_death_saves)
    del json_data['Combat']

    new_char = Character.objects.create(**json_data, player=new_player, race=new_race, background=new_background,
                                        details=new_details, treasure=new_treasure, ability_scores=new_ability_scores,
                                        skills=new_skills, saving_throws=new_saving_throws, combat=new_combat)

    new_char.classes.set(char_classes_list)
    new_char.feats.set(character_feats_list)
    new_char.spells.set(character_spells_list)
    new_char.weapons.set(character_weapons_list)
    new_char.equipment.set(character_equipment_list)

    return new_char


# Foreign keys

def get_race(race_id: int) -> dict:
    race = Race.objects.get(id=race_id)
    race_dict = get_fields(model=race)
    return race_dict


def get_player(player_id: int) -> dict:
    return get_fields(Player.objects.get(id=player_id))


def get_background(background_id: int) -> dict:
    return get_fields(Background.objects.get(id=background_id))


def get_details(details_id: int) -> dict:
    return get_fields(Details.objects.get(id=details_id))


def get_treasure(treasure_id: int) -> dict:
    return get_fields(Treasure.objects.get(id=treasure_id))


def get_ability_scores(ability_score_id: int) -> dict:
    return get_fields(AbilityScores.objects.get(id=ability_score_id))


# Many to many fields

def get_classes(character_id: int) -> list:
    return get_many_to_many(Character.objects.get(id=character_id).classes)


def get_feats(character_id: int) -> list:
    return get_many_to_many(Character.objects.get(id=character_id).feats)


def get_spells(character_id: int) -> list:
    return get_many_to_many(Character.objects.get(id=character_id).spells)


def get_weapons(character_id: int) -> list:
    return get_many_to_many(Character.objects.get(id=character_id).weapons)


def get_equipment(character_id: int) -> list:
    return get_many_to_many(Character.objects.get(id=character_id).equipment)
