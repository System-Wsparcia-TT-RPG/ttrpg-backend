from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

# TODO : Update the model to the full version of the Character model
class Character(models.Model):
    nickname = models.CharField(max_length=100)
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    xp = models.IntegerField()
    race = models.ForeignKey('Race', on_delete=models.CASCADE)
    classes = classes = models.ManyToManyField('Class')
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



class Player(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField()

class Race(models.Model):
    name = models.CharField(max_length=100)
    subtype = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    traits = models.ManyToManyField('Trait')
    actions = models.ManyToManyField('Action')
    senses = models.ForeignKey('Senses', on_delete=models.CASCADE)
    source = models.ForeignKey('Source', on_delete=models.CASCADE)

class Trait(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)
    source = models.ForeignKey('Source', on_delete=models.CASCADE)

class Action(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)
    source = models.ForeignKey('Source', on_delete=models.CASCADE)
    damage_dice = models.ForeignKey('Damage_dice', on_delete=models.CASCADE)
    damage_bonus = models.IntegerField()
    legendary = models.BooleanField()
    reaction = models.BooleanField()
    source = models.ForeignKey('Source', on_delete=models.CASCADE)

class Damage_dice(models.Model):
    count = models.IntegerField()
    sides = models.IntegerField()
    mod = models.IntegerField()

class Damage (models.Model):
    dice = models.ForeignKey('Damage_dice', on_delete=models.CASCADE)
    type = models.CharField(max_length=100)

class Senses(models.Model):
    darkvision = models.IntegerField()
    blindsight = models.IntegerField()
    tremorsense = models.IntegerField()
    truesight = models.IntegerField()
    passive_perception = models.IntegerField()

class Class(models.Model):
    name = models.CharField(max_length=100)
    subtype = models.CharField(max_length=100)
    level = models.IntegerField()
    hit_die = models.IntegerField()
    spellcasting = models.TextChoices('Spellcasting ability', 'int wis cha')
    features = models.ManyToManyField('Feature')
    source = models.ForeignKey('Source', on_delete=models.CASCADE)


class Background(models.Model):
    name = models.CharField(max_length=100)
    option = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)
    source = models.ForeignKey('Source', on_delete=models.CASCADE)

class Feature(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)
    source = models.ForeignKey('Source', on_delete=models.CASCADE)

class Source(models.Model):
    text = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    href = models.CharField(max_length=100)

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

class Feat(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)
    source = models.ForeignKey('Source', on_delete=models.CASCADE)

class Spell(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    school = models.CharField(max_length=100)
    casting_time = models.CharField(max_length=100)
    range_area = models.CharField(max_length=100)
    components = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)
    higher_level = models.CharField(max_length=1024)
    ritual = models.BooleanField()
    concentration = models.BooleanField()
    attack_save = models.CharField(max_length=100)
    damage_effect = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tag')
    source = models.ForeignKey('Source', on_delete=models.CASCADE)

class Weapon(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    description = models.CharField(max_length=1024)
    attack_bonus = models.IntegerField()
    damage_dice = models.ForeignKey('Damage_dice', on_delete=models.CASCADE)
    damage_bonus = models.IntegerField()
    damage_type = models.CharField(max_length=100)
    properties = models.ManyToManyField('Property')
    source = models.ForeignKey('Source', on_delete=models.CASCADE)

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    description = models.CharField(max_length=1024)
    magic = models.BooleanField()
    quantity = models.IntegerField()
    source = models.ForeignKey('Source', on_delete=models.CASCADE)

class Property(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=100)

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

class CombatStats(models.Model):
    armor_class = models.IntegerField()
    initiative = models.IntegerField()
    speed = models.IntegerField()
    hit_points = models.IntegerField()
    hit_dice = models.CharField(max_length=100)
    death_saves = models.ForeignKey('DeathSaves', on_delete=models.CASCADE)

class DeathSaves(models.Model):
    successes = models.IntegerField()
    failures = models.IntegerField()