from rest_framework import serializers

from web.api.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['nickname', 'player', 'xp', 'race', 'classes', 'background', 'details', 'weapon_proficiencies',
                  'armor_proficiencies', 'tool_proficiencies', 'feats', 'spells', 'weapons', 'equipment', 'treasure',
                  'ability_scores', 'skills', 'saving_throws', 'combat']
        depth = 10
