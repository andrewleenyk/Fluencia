import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from cards.models import Term

# Adjectives
adjectives = [
    {'word': 'marrón', 'definition': 'The color brown.'},
    {'word': 'rojo', 'definition': 'Red'},
    {'word': 'alto', 'definition': 'Tall'},
    {'word': 'bonito', 'definition': 'Beautiful'},
    {'word': 'pequeño', 'definition': 'Small'},
    {'word': 'grande', 'definition': 'Big'},
    {'word': 'delgado', 'definition': 'Thin'},
    {'word': 'gordo', 'definition': 'Fat'},
    {'word': 'amable', 'definition': 'Kind'},
    {'word': 'triste', 'definition': 'Sad'},
    {'word': 'feliz', 'definition': 'Happy'},
    {'word': 'interesante', 'definition': 'Interesting'},
    {'word': 'aburrido', 'definition': 'Boring'},
    {'word': 'simpático', 'definition': 'Friendly'},
    {'word': 'hermoso', 'definition': 'Beautiful'},
]

for adj in adjectives:
    term = Term(
        word=adj['word'],
        definition=adj['definition'],
        wordType='adjective'
    )
    term.save()

# Nouns
nouns = [
    {'word': 'pez', 'definition': 'Fish'},
    {'word': 'casa', 'definition': 'House'},
    {'word': 'perro', 'definition': 'Dog'},
    {'word': 'gato', 'definition': 'Cat'},
    {'word': 'árbol', 'definition': 'Tree'},
    {'word': 'coche', 'definition': 'Car'},
    {'word': 'mesa', 'definition': 'Table'},
    {'word': 'libro', 'definition': 'Book'},
    {'word': 'sol', 'definition': 'Sun'},
    {'word': 'luna', 'definition': 'Moon'},
    {'word': 'playa', 'definition': 'Beach'},
    {'word': 'ciudad', 'definition': 'City'},
    {'word': 'amigo', 'definition': 'Friend'},
    {'word': 'familia', 'definition': 'Family'},
    {'word': 'trabajo', 'definition': 'Work'},
]

for noun in nouns:
    term = Term(
        word=noun['word'],
        definition=noun['definition'],
        wordType='noun'
    )
    term.save()

# Verbs
verbs = [
    {
        'word': 'ayudar',
        'definition': 'To help',
        'tense': 'past',
        'conjugations': {
            'yo': 'ayudé',
            'tú': 'ayudaste',
            'él/ella/usted': 'ayudó',
            'nosotros/nosotras': 'ayudamos',
            'vosotros/vosotras': 'ayudasteis',
            'ellos/ellas/ustedes': 'ayudaron'
        }
    },
    {
        'word': 'hablar',
        'definition': 'To speak',
        'tense': 'present',
        'conjugations': {
            'yo': 'hablo',
            'tú': 'hablas',
            'él/ella/usted': 'habla',
            'nosotros/nosotras': 'hablamos',
            'vosotros/vosotras': 'habláis',
            'ellos/ellas/ustedes': 'hablan'
        }
    },
    {
        'word': 'comer',
        'definition': 'To eat',
        'tense': 'present',
        'conjugations': {
            'yo': 'como',
            'tú': 'comes',
            'él/ella/usted': 'come',
            'nosotros/nosotras': 'comemos',
            'vosotros/vosotras': 'coméis',
            'ellos/ellas/ustedes': 'comen'
        }
    },
    {
        'word': 'correr',
        'definition': 'To run',
        'tense': 'present',
        'conjugations': {
            'yo': 'corro',
            'tú': 'corres',
            'él/ella/usted': 'corre',
            'nosotros/nosotras': 'corremos',
            'vosotros/vosotras': 'corréis',
            'ellos/ellas/ustedes': 'corren'
        }
    },
    {
        'word': 'escribir',
        'definition': 'To write',
        'tense': 'present',
        'conjugations': {
            'yo': 'escribo',
            'tú': 'escribes',
            'él/ella/usted': 'escribe',
            'nosotros/nosotras': 'escribimos',
            'vosotros/vosotras': 'escribís',
            'ellos/ellas/ustedes': 'escriben'
        }
    },
    {
        'word': 'leer',
        'definition': 'To read',
        'tense': 'present',
        'conjugations': {
            'yo': 'leo',
            'tú': 'lees',
            'él/ella/usted': 'lee',
            'nosotros/nosotras': 'leemos',
            'vosotros/vosotras': 'leéis',
            'ellos/ellas/ustedes': 'leen'
        }
    },
    {
        'word': 'vivir',
        'definition': 'To live',
        'tense': 'present',
        'conjugations': {
            'yo': 'vivo',
            'tú': 'vives',
            'él/ella/usted': 'vive',
            'nosotros/nosotras': 'vivimos',
            'vosotros/vosotras': 'vivís',
            'ellos/ellas/ustedes': 'viven'
        }
    },
    {
        'word': 'beber',
        'definition': 'To drink',
        'tense': 'present',
        'conjugations': {
            'yo': 'bebo',
            'tú': 'bebes',
            'él/ella/usted': 'bebe',
            'nosotros/nosotras': 'bebemos',
            'vosotros/vosotras': 'bebéis',
            'ellos/ellas/ustedes': 'beben'
        }
    },
    {
        'word': 'trabajar',
        'definition': 'To work',
        'tense': 'present',
        'conjugations': {
            'yo': 'trabajo',
            'tú': 'trabajas',
            'él/ella/usted': 'trabaja',
            'nosotros/nosotras': 'trabajamos',
            'vosotros/vosotras': 'trabajáis',
            'ellos/ellas/ustedes': 'trabajan'
        }
    },
    {
        'word': 'estudiar',
        'definition': 'To study',
        'tense': 'present',
        'conjugations': {
            'yo': 'estudio',
            'tú': 'estudias',
            'él/ella/usted': 'estudia',
            'nosotros/nosotras': 'estudiamos',
            'vosotros/vosotras': 'estudiáis',
            'ellos/ellas/ustedes': 'estudian'
        }
    },
    # Add more verbs here...
]


for verb in verbs:
    term = Term(
        word=verb['word'],
        definition=verb['definition'],
        wordType='verb',
        tense=verb['tense'],
        conjugations=verb['conjugations']
    )
    term.save()
