# Endpoints Documentation

## API

### Model

Full model on how we have divided `../resources/example_character.json` - [\[Link\]](../resources/example_character.json)
is shown on ERD diagram provided here: `../resources/erd.png` - [\[Link\]](../resources/erd.png) (only tables beginning with
`api_`). However, because it is not really readable and practical to use it is highly advisable to see the model
manually via:
- Visiting the model definition file provided here `../../src/web/api/models.py` - [\[Link\]](../../src/web/api/models.py). (better option)
- Visiting the admin panel of django application.
  - You need to go to this url, when the backend app is running: `http://localhost:8000/admin/` - [\[Link\]](http://localhost:8000/admin/)
  - Login with provided username and password: `user`, `pass`.
  - Navigate to individual table and see their content.

Every table in model discussed previously is equipped with handy of endpoints. Here are the links to every one of them
including documentation.

### Damage Dice

Location can be found at `damage_dice.md` - [\[Link\]](damage_dice.md)

### Race

Location can be found at `race.md` - [\[Link\]](race.md)

### Components

Location can be found at `components.md` - [\[Link\]](components.md)

### Spell

Location can be found at `spell.md` - [\[Link\]](spell.md)

### Character

Location can be found at `character.md` - [\[Link\]](character.md)
