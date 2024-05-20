from enum import Enum

from django.db import models
from django.db.models import (
    Model, CharField, IntegerField, PositiveIntegerField, ForeignKey, ManyToManyField, BooleanField
)
from django.contrib.postgres.fields import ArrayField


class Player(Model):
    name = CharField(max_length=100)


class DamageDice(Model):
    count = PositiveIntegerField()
    sides = PositiveIntegerField()
    mod = PositiveIntegerField()


class Senses(Model):
    darkvision = PositiveIntegerField()
    blindsight = PositiveIntegerField()
    tremorsense = PositiveIntegerField()
    truesight = PositiveIntegerField()
    passive_perception = PositiveIntegerField()


class Trait(Model):
    name = CharField(max_length=100)
    description = CharField(max_length=1024)
    source = CharField(max_length=100)


class Background(Model):
    name = CharField(max_length=100)
    option = CharField(max_length=100)
    description = CharField(max_length=1024)
    source = CharField(max_length=100)


class Action(Model):
    name = CharField(max_length=100)
    description = CharField(max_length=1024)
    source = CharField(max_length=100)
    damage_dice = ForeignKey(DamageDice, on_delete=models.CASCADE)
    damage_bonus = IntegerField()
    legendary = BooleanField()
    reaction = BooleanField()


class Feature(Model):
    name = CharField(max_length=100)
    description = CharField(max_length=1024)
    source = CharField(max_length=100)


class Feat(Model):
    name = CharField(max_length=100)
    description = CharField(max_length=1024)
    source = CharField(max_length=100)


class Class(Model):
    name = CharField(max_length=100)
    subtype = CharField(max_length=100)
    level = PositiveIntegerField()
    hit_die = PositiveIntegerField()
    spellcasting = CharField(max_length=100)
    features = ManyToManyField(Feature)
    source = CharField(max_length=100)


class Details(Model):
    age = PositiveIntegerField()
    height = CharField(max_length=100)
    weight = PositiveIntegerField()
    eyes = CharField(max_length=100)
    skin = CharField(max_length=100)
    hair = CharField(max_length=100)
    personality = CharField(max_length=100)
    ideal = CharField(max_length=100)
    bond = CharField(max_length=100)
    flaw = CharField(max_length=100)
    backstory = CharField(max_length=1024)
    physical = CharField(max_length=1024)


class Equipment(Model):
    name = CharField(max_length=100)
    weight = PositiveIntegerField()
    description = CharField(max_length=1024)
    magic = BooleanField()
    quantity = PositiveIntegerField()
    source = CharField(max_length=100)


class Weapon(Model):
    name = CharField(max_length=100)
    weight = PositiveIntegerField()
    description = CharField(max_length=1024)
    attack_bonus = IntegerField()
    damage_dice = ForeignKey(DamageDice, on_delete=models.CASCADE)
    damage_bonus = IntegerField()
    damage_type = CharField(max_length=100)
    properties = ArrayField(CharField(max_length=100))
    source = CharField(max_length=100)


class Treasure(Model):
    pp = PositiveIntegerField()
    gp = PositiveIntegerField()
    ep = PositiveIntegerField()
    sp = PositiveIntegerField()
    cp = PositiveIntegerField()


class AbilityScores(Model):
    strength = PositiveIntegerField()
    dexterity = PositiveIntegerField()
    constitution = PositiveIntegerField()
    intelligence = PositiveIntegerField()
    wisdom = PositiveIntegerField()
    charisma = PositiveIntegerField()


class Skills(Model):
    acrobatics = PositiveIntegerField()
    animal_handling = PositiveIntegerField()
    arcana = PositiveIntegerField()
    athletics = PositiveIntegerField()
    deception = PositiveIntegerField()
    history = PositiveIntegerField()
    insight = PositiveIntegerField()
    intimidation = PositiveIntegerField()
    investigation = PositiveIntegerField()
    medicine = PositiveIntegerField()
    nature = PositiveIntegerField()
    perception = PositiveIntegerField()
    performance = PositiveIntegerField()
    persuasion = PositiveIntegerField()
    religion = PositiveIntegerField()
    sleight_of_hand = PositiveIntegerField()
    stealth = PositiveIntegerField()
    survival = PositiveIntegerField()


class SavingThrows(Model):
    strength = IntegerField()
    dexterity = IntegerField()
    constitution = IntegerField()
    intelligence = IntegerField()
    wisdom = IntegerField()
    charisma = IntegerField()


class DeathSaves(Model):
    successes = PositiveIntegerField()
    failures = PositiveIntegerField()


class CombatStats(Model):
    armor_class = PositiveIntegerField()
    initiative = PositiveIntegerField()
    speed = PositiveIntegerField()
    hit_points = PositiveIntegerField()
    hit_dice = CharField(max_length=100)
    death_saves = ForeignKey(DeathSaves, on_delete=models.CASCADE)


class Race(Model):
    class Size(str, Enum):
        Tiny = 'Tiny'
        Small = 'Small'
        Medium = 'Medium'
        Large = 'Large'
        Huge = 'Huge'
        Gargantuan = 'Gargantuan'

    name = CharField(max_length=100)
    subtype = CharField(max_length=100)
    size = CharField(max_length=100)
    traits = ManyToManyField(Trait)
    actions = ManyToManyField(Action)
    senses = ForeignKey(Senses, on_delete=models.CASCADE)
    source = CharField(max_length=100)


class Components(Model):
    verbal = BooleanField()
    somatic = BooleanField()
    material = BooleanField()
    raw = CharField(max_length=100)


class Spell(Model):
    name = CharField(max_length=100)
    tags = ArrayField(CharField(max_length=100))
    type = CharField(max_length=100)
    ritual = BooleanField()
    level = CharField(max_length=100)
    school = CharField(max_length=100)
    casting_time = CharField(max_length=100)
    range = CharField(max_length=100)
    components = ForeignKey(Components, on_delete=models.CASCADE)
    duration = CharField(max_length=100)
    description = CharField(max_length=2048)
    classes = ArrayField(CharField(max_length=100), null=True)
    higher_levels = CharField(max_length=2048, null=True)


class Character(Model):
    nickname = CharField(max_length=100)
    player = ForeignKey(Player, on_delete=models.CASCADE)
    xp = PositiveIntegerField()
    race = ForeignKey(Race, on_delete=models.CASCADE)
    classes = ManyToManyField(Class)
    background = ForeignKey(Background, on_delete=models.CASCADE)
    details = ForeignKey(Details, on_delete=models.CASCADE)
    weapon_proficiencies = ArrayField(CharField(max_length=100))
    armor_proficiencies = ArrayField(CharField(max_length=100))
    tool_proficiencies = ArrayField(CharField(max_length=100))
    feats = ManyToManyField(Feat)
    spells = ManyToManyField(Spell)
    weapons = ManyToManyField(Weapon)
    equipment = ManyToManyField(Equipment)
    treasure = ForeignKey(Treasure, on_delete=models.CASCADE)
    ability_scores = ForeignKey(AbilityScores, on_delete=models.CASCADE)
    skills = ForeignKey(Skills, on_delete=models.CASCADE)
    saving_throws = ForeignKey(SavingThrows, on_delete=models.CASCADE)
    combat = ForeignKey(CombatStats, on_delete=models.CASCADE)
