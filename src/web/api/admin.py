from django.contrib import admin
from .models import Player, DamageDice, Senses, \
    Source, Trait, Background, Action, Feature, Feat, \
    Class, Details, Equipment, Property, Weapon, Tag, Treasure, \
    AbilityScores, Skills, SavingThrows, DeathSaves, CombatStats, \
    Race, Spell, ArmorProficiencies, WeaponProficiencies, ToolProficiencies, \
    Character

# Register your models here.

admin.site.register(Player)
admin.site.register(DamageDice)
admin.site.register(Senses)
admin.site.register(Source)
admin.site.register(Trait)
admin.site.register(Background)
admin.site.register(Action)
admin.site.register(Feature)
admin.site.register(Feat)
admin.site.register(Class)
admin.site.register(Details)
admin.site.register(Equipment)
admin.site.register(Property)
admin.site.register(Weapon)
admin.site.register(Tag)
admin.site.register(Treasure)
admin.site.register(AbilityScores)
admin.site.register(Skills)
admin.site.register(SavingThrows)
admin.site.register(DeathSaves)
admin.site.register(CombatStats)
admin.site.register(Race)
admin.site.register(Spell)
admin.site.register(ArmorProficiencies)
admin.site.register(WeaponProficiencies)
admin.site.register(ToolProficiencies)
admin.site.register(Character)