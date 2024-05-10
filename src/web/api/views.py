from json import load, loads

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View

from utils.character_validation import CharacterSerializer
from utils.http_options_decorator import add_http_options

from .models import *


class CharacterView:
    @add_http_options
    class Get(View):
        http_method_names = ["get"]

        @staticmethod
        def get(request) -> JsonResponse:
            all_characters = list(Character.objects.values())

            return JsonResponse({"characters": all_characters})

    @add_http_options
    class GetId(View):
        http_method_names = ["get"]

        @staticmethod
        def get(request, character_id: int) -> JsonResponse:
            try:
                character = Character.objects.values().get(id=character_id)

                return JsonResponse({"character": character}, status=200)
            except ObjectDoesNotExist as error:
                return JsonResponse({
                    "error": "Character with specified id is not found!",
                    "details": str(error),
                    "error_data": {
                        "id_not_found": character_id,
                    },
                }, status=404)

    @add_http_options
    class Post(View):
        http_method_names = ["post"]

        @staticmethod
        def post(request) -> JsonResponse:
            json_data = loads(request.body)
            
            # Validation and db entry creation
            data_ser = CharacterSerializer(data=json_data)
            if data_ser.is_valid():
                try:
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

                    new_char = Character.objects.create(**json_data, player=new_player, race = new_race, background=new_background, 
                                                        details=new_details, treasure=new_treasure, ability_scores=new_ability_scores,
                                                        skills=new_skills, saving_throws=new_saving_throws, combat=new_combat)

                    new_char.classes.set(char_classes_list)
                    new_char.feats.set(character_feats_list)
                    new_char.spells.set(character_spells_list)
                    new_char.weapons.set(character_weapons_list)
                    new_char.equipment.set(character_equipment_list)


                    return JsonResponse({"character": {"id": new_char.id, "data": {**json_data}}}, status=201)
                except Exception as e:
                    print("An unexpected Exception occured: ", str(e))

            else:
                return JsonResponse({"error": "Provided character data is invalid!"}, status=400)

    @add_http_options
    class Put(View):
        http_method_names = ["put"]

        @staticmethod
        def put(request, character_id: int) -> JsonResponse:
            if character_id < 0:
                return JsonResponse({"error": "Invalid character ID"}, status=400)
            

            print(character_id)
            # if character_id != 1:
            #     return JsonResponse({"error": "Character not found"}, status=404)


            json_data = loads(request.body)

            # Validation
            data_ser = CharacterSerializer(data=json_data)
            if data_ser.is_valid():
                return JsonResponse({"character": {"id": character_id, "data": {**json_data}}}, status=201)
            else:
                return JsonResponse({"error": "Provided character data is invalid"}, status=400)

            # with open("./src/web/api/static_json/1.json", "r", encoding="utf-8") as file:
            #     return JsonResponse({"character": load(file)})

    @add_http_options
    class Delete(View):
        http_method_names = ["delete"]

        @staticmethod
        def delete(request, character_id: int) -> HttpResponse:
            if character_id != 1:
                return JsonResponse({"error": "Character not found"}, status=404)

            return HttpResponse(status=204)

class RaceView:
    @add_http_options
    class GetRaceEnum(View):
        http_method_names = ['get']

        @staticmethod
        def get(request) -> JsonResponse:
            return JsonResponse({a: a.value for a in Race.Size}, status=200)


@add_http_options
class Index(View):
    http_method_names = ['get']

    @staticmethod
    def get(request) -> HttpResponse:
        return render(request, 'index.html')
