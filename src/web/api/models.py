from django.db import models


# Create your models here.

# TODO : Update the model to the full version of the Character model
class Character(models.Model):
    nickname = models.CharField(max_length=100)
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    xp = models.IntegerField()
    race = models.ForeignKey('Race', on_delete=models.CASCADE)
    classes = classes = models.ManyToManyField('Class')
    background = models.ForeignKey('Background', on_delete=models.CASCADE)
    details = BLANK
    weapon_proficiencies = BLANK
    armor_proficiencies = BLANK
    tool_proficiencies = BLANK
    feats = BLANK
    spells = BLANK
    weapons = BLANK
    equipment = BLANK
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
    traits = BLANK
    abilities = BLANK
    senses = BLANK
    source = models.ForeignKey('Source', on_delete=models.CASCADE)

class Class(models.Model):
    name = models.CharField(max_length=100)
    subtype = models.CharField(max_length=100)
    level = models.IntegerField()
    hit_die = models.IntegerField()
    spellcasting = models.TextChoices('Spellcasting ability', 'int wis cha')
    features = BLANK
    source = models.ForeignKey('Source', on_delete=models.CASCADE)


class Background(models.Model):
    name = models.CharField(max_length=100)
    option = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)
    source = models.ForeignKey('Source', on_delete=models.CASCADE)

class Source(models.Model):
    text = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    href = models.CharField(max_length=100)

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