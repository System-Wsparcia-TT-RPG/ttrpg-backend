from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import (BooleanField, CharField, ForeignKey,
                              IntegerChoices, IntegerField, ManyToManyField,
                              Model, PositiveIntegerField, TextChoices)
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return f'User: {self.username}'

class Player(Model):
    name = CharField(max_length=100)


class DamageDice(Model):
    class Sides(IntegerChoices):
        D4 = 4
        D6 = 6
        D8 = 8
        D10 = 10
        D12 = 12
        D20 = 20

    count = PositiveIntegerField()
    sides = IntegerField(choices=Sides, default=Sides.D6)
    mod = IntegerField()


class Senses(Model): #PositiveIntegerField includes 0
    dark_vision = PositiveIntegerField()
    blind_sight = PositiveIntegerField()
    tremor_sense = PositiveIntegerField()
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
    hit_die = PositiveIntegerField() #hit_dice
    spell_casting = CharField(max_length=100)
    features = ManyToManyField(Feature)
    source = CharField(max_length=100)


class Details(Model):
    age = PositiveIntegerField()
    height = CharField(max_length=100)
    weight = PositiveIntegerField()
    eyes = CharField(max_length=100)
    skin = CharField(max_length=100)
    hair = CharField(max_length=100)
    personality = CharField(max_length=512)
    ideal = CharField(max_length=512)
    bond = CharField(max_length=512)
    flaw = CharField(max_length=512)
    backstory = CharField(max_length=1024)
    physical = CharField(max_length=1024) #physical_look


class Equipment(Model):
    name = CharField(max_length=100)
    weight = PositiveIntegerField() #TODO: tu można zmienić na FloatField, ale wymaga większego bagna
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
    strength = IntegerField(validators=[
        MinValueValidator(-20),
        MaxValueValidator(20),
    ])
    dexterity = IntegerField(validators=[
        MinValueValidator(-20),
        MaxValueValidator(20),
    ])
    constitution = IntegerField(validators=[
        MinValueValidator(-20),
        MaxValueValidator(20),
    ])
    intelligence = IntegerField(validators=[
        MinValueValidator(-20),
        MaxValueValidator(20),
    ])
    wisdom = IntegerField(validators=[
        MinValueValidator(-20),
        MaxValueValidator(20),
    ])
    charisma = IntegerField(validators=[
        MinValueValidator(-20),
        MaxValueValidator(20),
    ])


class DeathSaves(Model):
    successes = PositiveIntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(3),
    ])
    failures = PositiveIntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(3),
    ])


class CombatStats(Model):
    armor_class = PositiveIntegerField()
    initiative = IntegerField()
    speed = PositiveIntegerField() #ft
    hit_points = PositiveIntegerField() #TODO: current_hit_points
    hit_dice = CharField(max_length=100)
    death_saves = ForeignKey(DeathSaves, on_delete=models.CASCADE)


class Race(Model):
    class Size(TextChoices):
        TINY = 'T', gettext_lazy("Tiny")
        SMALL = 'S', gettext_lazy("Small")
        MEDIUM = 'M', gettext_lazy("Medium")
        LARGE = 'L', gettext_lazy("Large")
        HUGE = 'H', gettext_lazy("Huge")
        GARGANTUAN = 'G', gettext_lazy("Gargantuan")

    name = CharField(max_length=100)
    subtype = CharField(max_length=100) #subrace
    size = CharField(max_length=100, choices=Size, default=Size.MEDIUM)
    traits = ManyToManyField(Trait)
    actions = ManyToManyField(Action)
    senses = ForeignKey(Senses, on_delete=models.CASCADE)
    source = CharField(max_length=100)
    #TODO: description

class Components(Model):
    verbal = BooleanField()
    somatic = BooleanField()
    material = BooleanField()
    raw = CharField(max_length=100)


class Spell(Model):
    name = CharField(max_length=100)
    tags = ArrayField(CharField(max_length=100))
    type = CharField(max_length=100) #niepotrzebne jak kość ogonowa
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
