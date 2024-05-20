from rest_framework import serializers
from .models import (
    Player, DamageDice, Senses, Trait, Background, Action, Feature, Feat,
    Class, Details, Equipment, Weapon, Treasure, AbilityScores, Skills,
    SavingThrows, DeathSaves, CombatStats, Race, Spell, Components, Character
)

# TODO: Automate the creation of these serializers, by revealing the models python dynamism, just like
#  admin panel was automated.

"""
from rest_framework import serializers
from .models import *

# Get all models from the models module
all_models = [cls for cls in globals().values() if isinstance(cls, type) and issubclass(cls, models.Model) and cls is not models.Model]

# Dynamically create a serializer for each model
for model in all_models:
    # Create Meta class
    Meta = type('Meta', (), {'model': model, 'fields': '__all__'})
    
    # Create Serializer class
    globals()[f'{model.__name__}Serializer'] = type(f'{model.__name__}Serializer', (serializers.ModelSerializer,), {'Meta': Meta})
"""

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class DamageDiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DamageDice
        fields = '__all__'


class SensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Senses
        fields = '__all__'


class TraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trait
        fields = '__all__'


class BackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Background
        fields = '__all__'


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'


class FeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feat
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Class
        fields = '__all__'


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'


class TreasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treasure
        fields = '__all__'


class AbilityScoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbilityScores
        fields = '__all__'


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'


class SavingThrowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingThrows
        fields = '__all__'


class DeathSavesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeathSaves
        fields = '__all__'


class CombatStatsSerializer(serializers.ModelSerializer):
    death_saves = DeathSavesSerializer()

    class Meta:
        model = CombatStats
        fields = '__all__'


class RaceSerializer(serializers.ModelSerializer):
    traits = TraitSerializer(many=True, read_only=True)
    actions = ActionSerializer(many=True, read_only=True)
    senses = SensesSerializer()

    class Meta:
        model = Race
        fields = '__all__'


class SpellSerializer(serializers.ModelSerializer):
    components = serializers.PrimaryKeyRelatedField(queryset=Components.objects.all())

    class Meta:
        model = Spell
        fields = '__all__'


class ComponentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Components
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    race = RaceSerializer()
    classes = ClassSerializer(many=True, read_only=True)
    background = BackgroundSerializer()
    details = DetailsSerializer()
    feats = FeatSerializer(many=True, read_only=True)
    spells = SpellSerializer(many=True, read_only=True)
    weapons = WeaponSerializer(many=True, read_only=True)
    equipment = EquipmentSerializer(many=True, read_only=True)
    treasure = TreasureSerializer()
    ability_scores = AbilityScoresSerializer()
    skills = SkillsSerializer()
    saving_throws = SavingThrowsSerializer()
    combat = CombatStatsSerializer()

    class Meta:
        model = Character
        fields = '__all__'
