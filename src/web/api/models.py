from enum import Enum

from django.db import models
from django.contrib.postgres.fields import ArrayField


class Player(models.Model):
    name = models.CharField(max_length=100)


class DamageDice(models.Model):
    count = models.IntegerField()
    sides = models.IntegerField()
    mod = models.IntegerField()


class Senses(models.Model):
    darkvision = models.IntegerField()
    blindsight = models.IntegerField()
    tremorsense = models.IntegerField()
    truesight = models.IntegerField()
    passive_perception = models.IntegerField()


class Trait(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)
    source = models.CharField(max_length=100)


class Background(models.Model):
    name = models.CharField(max_length=100)
    option = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)
    source = models.CharField(max_length=100)


class Action(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)
    source = models.CharField(max_length=100)
    damage_dice = models.ForeignKey('DamageDice', on_delete=models.CASCADE)
    damage_bonus = models.IntegerField()
    legendary = models.BooleanField()
    reaction = models.BooleanField()


class Feature(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)
    source = models.CharField(max_length=100)


class Feat(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)
    source = models.CharField(max_length=100)


class Class(models.Model):
    name = models.CharField(max_length=100)
    subtype = models.CharField(max_length=100)
    level = models.IntegerField()
    hit_die = models.IntegerField()
    spellcasting = models.CharField(max_length=100)
    features = models.ManyToManyField('Feature')
    source = models.CharField(max_length=100)


class Details(models.Model):
    age = models.IntegerField()
    height = models.CharField(max_length=100)
    weight = models.IntegerField()
    eyes = models.CharField(max_length=100)
    skin = models.CharField(max_length=100)
    hair = models.CharField(max_length=100)
    personality = models.CharField(max_length=100)
    ideal = models.CharField(max_length=100)
    bond = models.CharField(max_length=100)
    flaw = models.CharField(max_length=100)
    backstory = models.CharField(max_length=1024)
    physical = models.CharField(max_length=1024)


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    description = models.CharField(max_length=1024)
    magic = models.BooleanField()
    quantity = models.IntegerField()
    source = models.CharField(max_length=100)


class Weapon(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    description = models.CharField(max_length=1024)
    attack_bonus = models.IntegerField()
    damage_dice = models.ForeignKey('DamageDice', on_delete=models.CASCADE)
    damage_bonus = models.IntegerField()
    damage_type = models.CharField(max_length=100)
    properties = ArrayField(models.CharField(max_length=100))
    source = models.CharField(max_length=100)


class Treasure(models.Model):
    pp = models.IntegerField()
    gp = models.IntegerField()
    ep = models.IntegerField()
    sp = models.IntegerField()
    cp = models.IntegerField()


class AbilityScores(models.Model):
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()


class Skills(models.Model):
    acrobatics = models.IntegerField()
    animal_handling = models.IntegerField()
    arcana = models.IntegerField()
    athletics = models.IntegerField()
    deception = models.IntegerField()
    history = models.IntegerField()
    insight = models.IntegerField()
    intimidation = models.IntegerField()
    investigation = models.IntegerField()
    medicine = models.IntegerField()
    nature = models.IntegerField()
    perception = models.IntegerField()
    performance = models.IntegerField()
    persuasion = models.IntegerField()
    religion = models.IntegerField()
    sleight_of_hand = models.IntegerField()
    stealth = models.IntegerField()
    survival = models.IntegerField()


class SavingThrows(models.Model):
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()


class DeathSaves(models.Model):
    successes = models.IntegerField()
    failures = models.IntegerField()


class CombatStats(models.Model):
    armor_class = models.IntegerField()
    initiative = models.IntegerField()
    speed = models.IntegerField()
    hit_points = models.IntegerField()
    hit_dice = models.CharField(max_length=100)
    death_saves = models.ForeignKey('DeathSaves', on_delete=models.CASCADE)


class Race(models.Model):
    class Size(str, Enum):
        Tiny = 'Tiny'
        Small = 'Small'
        Medium = 'Medium'
        Large = 'Large'
        Huge = 'Huge'
        Gargantuan = 'Gargantuan'

    name = models.CharField(max_length=100)
    subtype = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    traits = models.ManyToManyField('Trait')
    actions = models.ManyToManyField('Action')
    senses = models.ForeignKey('Senses', on_delete=models.CASCADE)
    source = models.CharField(max_length=100)

class Spell(models.Model):
    name = models.CharField(max_length=100)
    tags = ArrayField(models.CharField(max_length=100))
    type = models.CharField(max_length=100)
    ritual = models.BooleanField()
    level = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    casting_time = models.CharField(max_length=100)
    range = models.CharField(max_length=100)
    components = models.ForeignKey('Components', on_delete=models.CASCADE)
    duration = models.CharField(max_length=100)
    description = models.CharField(max_length=2048)
    classes = ArrayField(models.CharField(max_length=100))
    higher_levels = models.CharField(max_length=2048)

class Components(models.Model):
    verbal = models.BooleanField()
    somatic = models.BooleanField()
    material = models.BooleanField()
    raw = models.CharField(max_length=100)

class Character(models.Model):
    nickname = models.CharField(max_length=100)
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    xp = models.IntegerField()
    race = models.ForeignKey('Race', on_delete=models.CASCADE)
    classes = models.ManyToManyField('Class')
    background = models.ForeignKey('Background', on_delete=models.CASCADE)
    details = models.ForeignKey('Details', on_delete=models.CASCADE)
    weapon_proficiencies = ArrayField(models.CharField(max_length=100))
    armor_proficiencies = ArrayField(models.CharField(max_length=100))
    tool_proficiencies = ArrayField(models.CharField(max_length=100))
    feats = models.ManyToManyField('Feat')
    spells = models.ManyToManyField('Spell')
    weapons = models.ManyToManyField('Weapon')
    equipment = models.ManyToManyField('Equipment')
    treasure = models.ForeignKey('Treasure', on_delete=models.CASCADE)
    ability_scores = models.ForeignKey('AbilityScores', on_delete=models.CASCADE)
    skills = models.ForeignKey('Skills', on_delete=models.CASCADE)
    saving_throws = models.ForeignKey('SavingThrows', on_delete=models.CASCADE)
    combat = models.ForeignKey('CombatStats', on_delete=models.CASCADE)
