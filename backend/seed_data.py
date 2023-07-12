import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from cards.models import Term, Category

# to seed, run python seed_data.py
Term.objects.all().delete()

# Categories
# Assuming you have a list of category names
category_names = ['beginner', 'intermediate', 'advanced']
for name in category_names:
    Category.objects.create(name=name)


# Adjectives
adjectives = [
    {'word': 'marrón', 'definition': 'The color brown.', 'category': 'beginner'},
    {'word': 'rojo', 'definition': 'Red', 'category': 'beginner'},
    {'word': 'alto', 'definition': 'Tall', 'category': 'beginner'},
    {'word': 'bonito', 'definition': 'Beautiful', 'category': 'beginner'},
    {'word': 'pequeño', 'definition': 'Small', 'category': 'beginner'},
    {'word': 'grande', 'definition': 'Big', 'category': 'beginner'},
    {'word': 'delgado', 'definition': 'Thin', 'category': 'beginner'},
    {'word': 'gordo', 'definition': 'Fat', 'category': 'beginner'},
    {'word': 'amable', 'definition': 'Kind', 'category': 'beginner'},
    {'word': 'triste', 'definition': 'Sad', 'category': 'beginner'},
    {'word': 'feliz', 'definition': 'Happy', 'category': 'beginner'},
    {'word': 'interesante', 'definition': 'Interesting', 'category': 'beginner'},
    {'word': 'aburrido', 'definition': 'Boring', 'category': 'beginner'},
    {'word': 'simpático', 'definition': 'Friendly', 'category': 'beginner'},
    {'word': 'hermoso', 'definition': 'Beautiful', 'category': 'beginner'},
]

intermediate_adjectives = [
    {'word': 'difícil', 'definition': 'Difficult', 'category': 'intermediate'},
    {'word': 'interesante', 'definition': 'Interesting', 'category': 'intermediate'},
    {'word': 'fácil', 'definition': 'Easy', 'category': 'intermediate'},
    {'word': 'importante', 'definition': 'Important', 'category': 'intermediate'},
    {'word': 'complejo', 'definition': 'Complex', 'category': 'intermediate'},
    {'word': 'sorprendente', 'definition': 'Surprising', 'category': 'intermediate'},
    {'word': 'útil', 'definition': 'Useful', 'category': 'intermediate'},
    {'word': 'perfecto', 'definition': 'Perfect', 'category': 'intermediate'},
    {'word': 'rápido', 'definition': 'Fast', 'category': 'intermediate'},
    {'word': 'necesario', 'definition': 'Necessary', 'category': 'intermediate'},
]

advanced_adjectives = [
    {'word': 'sofisticado', 'definition': 'Sophisticated', 'category': 'advanced'},
    {'word': 'innovador', 'definition': 'Innovative', 'category': 'advanced'},
    {'word': 'extraordinario', 'definition': 'Extraordinary', 'category': 'advanced'},
    {'word': 'exquisito', 'definition': 'Exquisite', 'category': 'advanced'},
    {'word': 'versátil', 'definition': 'Versatile', 'category': 'advanced'},
    {'word': 'poderoso', 'definition': 'Powerful', 'category': 'advanced'},
    {'word': 'inspirador', 'definition': 'Inspiring', 'category': 'advanced'},
    {'word': 'profundo', 'definition': 'Deep', 'category': 'advanced'},
    {'word': 'innovador', 'definition': 'Innovative', 'category': 'advanced'},
    {'word': 'sofisticado', 'definition': 'Sophisticated', 'category': 'advanced'},
]

adjectives.extend(intermediate_adjectives)
adjectives.extend(advanced_adjectives)


for adj in adjectives:
    term = Term(
        word=adj['word'],
        definition=adj['definition'],
        wordType='adjective'
    )
    term.save()
    categories = Category.objects.filter(name=adj['category'])
    term.categories.add(*categories)
    

# Nouns
nouns = [
    {'word': 'pez', 'definition': 'Fish', 'category': 'beginner'},
    {'word': 'casa', 'definition': 'House', 'category': 'beginner'},
    {'word': 'perro', 'definition': 'Dog', 'category': 'beginner'},
    {'word': 'gato', 'definition': 'Cat', 'category': 'beginner'},
    {'word': 'árbol', 'definition': 'Tree', 'category': 'beginner'},
    {'word': 'coche', 'definition': 'Car', 'category': 'beginner'},
    {'word': 'mesa', 'definition': 'Table', 'category': 'beginner'},
    {'word': 'libro', 'definition': 'Book', 'category': 'beginner'},
    {'word': 'sol', 'definition': 'Sun', 'category': 'beginner'},
    {'word': 'luna', 'definition': 'Moon', 'category': 'beginner'},
    {'word': 'playa', 'definition': 'Beach', 'category': 'beginner'},
    {'word': 'ciudad', 'definition': 'City', 'category': 'beginner'},
    {'word': 'amigo', 'definition': 'Friend', 'category': 'beginner'},
    {'word': 'familia', 'definition': 'Family', 'category': 'beginner'},
    {'word': 'trabajo', 'definition': 'Work', 'category': 'beginner'},
]

intermediate_nouns = [
    {'word': 'río', 'definition': 'River', 'category': 'intermediate'},
    {'word': 'montaña', 'definition': 'Mountain', 'category': 'intermediate'},
    {'word': 'escuela', 'definition': 'School', 'category': 'intermediate'},
    {'word': 'cielo', 'definition': 'Sky', 'category': 'intermediate'},
    {'word': 'hombre', 'definition': 'Man', 'category': 'intermediate'},
    {'word': 'mujer', 'definition': 'Woman', 'category': 'intermediate'},
    {'word': 'niño', 'definition': 'Child', 'category': 'intermediate'},
    {'word': 'vida', 'definition': 'Life', 'category': 'intermediate'},
    {'word': 'momento', 'definition': 'Moment', 'category': 'intermediate'},
    {'word': 'voz', 'definition': 'Voice', 'category': 'intermediate'},
]

advanced_nouns = [
    {'word': 'universo', 'definition': 'Universe', 'category': 'advanced'},
    {'word': 'historia', 'definition': 'History', 'category': 'advanced'},
    {'word': 'sueño', 'definition': 'Dream', 'category': 'advanced'},
    {'word': 'corazón', 'definition': 'Heart', 'category': 'advanced'},
    {'word': 'pensamiento', 'definition': 'Thought', 'category': 'advanced'},
    {'word': 'problema', 'definition': 'Problem', 'category': 'advanced'},
    {'word': 'felicidad', 'definition': 'Happiness', 'category': 'advanced'},
    {'word': 'destino', 'definition': 'Destiny', 'category': 'advanced'},
    {'word': 'esperanza', 'definition': 'Hope', 'category': 'advanced'},
    {'word': 'éxito', 'definition': 'Success', 'category': 'advanced'},
]

nouns.extend(intermediate_nouns)
nouns.extend(advanced_nouns)


for noun in nouns:
    term = Term(
        word=noun['word'],
        definition=noun['definition'],
        wordType='noun'
    )
    term.save()
    categories = Category.objects.filter(name=adj['category'])
    term.categories.add(*categories)

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
        },
        'category': 'beginner',
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
        },
        'category': 'beginner',
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
        },
        'category': 'beginner',
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
        },
        'category': 'beginner',
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
        },
        'category': 'beginner',
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
        },
        'category': 'beginner',
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
        },
        'category': 'beginner',
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
        },
        'category': 'beginner',
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
        },
        'category': 'beginner',
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
        },
        'category': 'beginner',
    },
]

intermediate_verbs = [
    {
        'word': 'pensar',
        'definition': 'To think',
        'tense': 'present',
        'conjugations': {
            'yo': 'pienso',
            'tú': 'piensas',
            'él/ella/usted': 'piensa',
            'nosotros/nosotras': 'pensamos',
            'vosotros/vosotras': 'pensáis',
            'ellos/ellas/ustedes': 'piensan'
        },
        'category': 'intermediate',
    },
    {
        'word': 'crear',
        'definition': 'To create',
        'tense': 'present',
        'conjugations': {
            'yo': 'creo',
            'tú': 'creas',
            'él/ella/usted': 'crea',
            'nosotros/nosotras': 'creamos',
            'vosotros/vosotras': 'creáis',
            'ellos/ellas/ustedes': 'crean'
        },
        'category': 'intermediate',
    },
    {
        'word': 'aprender',
        'definition': 'To learn',
        'tense': 'present',
        'conjugations': {
            'yo': 'aprendo',
            'tú': 'aprendes',
            'él/ella/usted': 'aprende',
            'nosotros/nosotras': 'aprendemos',
            'vosotros/vosotras': 'aprendéis',
            'ellos/ellas/ustedes': 'aprenden'
        },
        'category': 'intermediate',
    },
    {
        'word': 'comprender',
        'definition': 'To understand',
        'tense': 'present',
        'conjugations': {
            'yo': 'comprendo',
            'tú': 'comprendes',
            'él/ella/usted': 'comprende',
            'nosotros/nosotras': 'comprendemos',
            'vosotros/vosotras': 'comprendéis',
            'ellos/ellas/ustedes': 'comprenden'
        },
        'category': 'intermediate',
    },
    {
        'word': 'necesitar',
        'definition': 'To need',
        'tense': 'present',
        'conjugations': {
            'yo': 'necesito',
            'tú': 'necesitas',
            'él/ella/usted': 'necesita',
            'nosotros/nosotras': 'necesitamos',
            'vosotros/vosotras': 'necesitáis',
            'ellos/ellas/ustedes': 'necesitan'
        },
        'category': 'intermediate',
    },
    {
        'word': 'preferir',
        'definition': 'To prefer',
        'tense': 'present',
        'conjugations': {
            'yo': 'prefiero',
            'tú': 'prefieres',
            'él/ella/usted': 'prefiere',
            'nosotros/nosotras': 'preferimos',
            'vosotros/vosotras': 'preferís',
            'ellos/ellas/ustedes': 'prefieren'
        },
        'category': 'intermediate',
    },
    {
        'word': 'viajar',
        'definition': 'To travel',
        'tense': 'present',
        'conjugations': {
            'yo': 'viajo',
            'tú': 'viajas',
            'él/ella/usted': 'viaja',
            'nosotros/nosotras': 'viajamos',
            'vosotros/vosotras': 'viajáis',
            'ellos/ellas/ustedes': 'viajan'
        },
        'category': 'intermediate',
    },
    {
        'word': 'conocer',
        'definition': 'To know',
        'tense': 'present',
        'conjugations': {
            'yo': 'conozco',
            'tú': 'conoces',
            'él/ella/usted': 'conoce',
            'nosotros/nosotras': 'conocemos',
            'vosotros/vosotras': 'conocéis',
            'ellos/ellas/ustedes': 'conocen'
        },
        'category': 'intermediate',
    },
    {
        'word': 'sentir',
        'definition': 'To feel',
        'tense': 'present',
        'conjugations': {
            'yo': 'siento',
            'tú': 'sientes',
            'él/ella/usted': 'siente',
            'nosotros/nosotras': 'sentimos',
            'vosotros/vosotras': 'sentís',
            'ellos/ellas/ustedes': 'sienten'
        },
        'category': 'intermediate',
    },
    {
        'word': 'decidir',
        'definition': 'To decide',
        'tense': 'present',
        'conjugations': {
            'yo': 'decido',
            'tú': 'decides',
            'él/ella/usted': 'decide',
            'nosotros/nosotras': 'decidimos',
            'vosotros/vosotras': 'decidís',
            'ellos/ellas/ustedes': 'deciden'
        },
        'category': 'intermediate',
    },
]

advanced_verbs = [
    {
        'word': 'investigar',
        'definition': 'To investigate',
        'tense': 'present',
        'conjugations': {
            'yo': 'investigo',
            'tú': 'investigas',
            'él/ella/usted': 'investiga',
            'nosotros/nosotras': 'investigamos',
            'vosotros/vosotras': 'investigáis',
            'ellos/ellas/ustedes': 'investigan'
        },
        'category': 'advanced',
    },
    {
        'word': 'desarrollar',
        'definition': 'To develop',
        'tense': 'present',
        'conjugations': {
            'yo': 'desarrollo',
            'tú': 'desarrollas',
            'él/ella/usted': 'desarrolla',
            'nosotros/nosotras': 'desarrollamos',
            'vosotros/vosotras': 'desarrolláis',
            'ellos/ellas/ustedes': 'desarrollan'
        },
        'category': 'advanced',
    },
    {
        'word': 'analizar',
        'definition': 'To analyze',
        'tense': 'present',
        'conjugations': {
            'yo': 'analizo',
            'tú': 'analizas',
            'él/ella/usted': 'analiza',
            'nosotros/nosotras': 'analizamos',
            'vosotros/vosotras': 'analizáis',
            'ellos/ellas/ustedes': 'analizan'
        },
        'category': 'advanced',
    },
    {
        'word': 'negociar',
        'definition': 'To negotiate',
        'tense': 'present',
        'conjugations': {
            'yo': 'negocio',
            'tú': 'negocias',
            'él/ella/usted': 'negocia',
            'nosotros/nosotras': 'negociamos',
            'vosotros/vosotras': 'negociáis',
            'ellos/ellas/ustedes': 'negocian'
        },
        'category': 'advanced',
    },
    {
        'word': 'experimentar',
        'definition': 'To experiment',
        'tense': 'present',
        'conjugations': {
            'yo': 'experimento',
            'tú': 'experimentas',
            'él/ella/usted': 'experimenta',
            'nosotros/nosotras': 'experimentamos',
            'vosotros/vosotras': 'experimentáis',
            'ellos/ellas/ustedes': 'experimentan'
        },
        'category': 'advanced',
    },
    {
        'word': 'implementar',
        'definition': 'To implement',
        'tense': 'present',
        'conjugations': {
            'yo': 'implemento',
            'tú': 'implementas',
            'él/ella/usted': 'implementa',
            'nosotros/nosotras': 'implementamos',
            'vosotros/vosotras': 'implementáis',
            'ellos/ellas/ustedes': 'implementan'
        },
        'category': 'advanced',
    },
    {
        'word': 'optimizar',
        'definition': 'To optimize',
        'tense': 'present',
        'conjugations': {
            'yo': 'optimizo',
            'tú': 'optimizas',
            'él/ella/usted': 'optimiza',
            'nosotros/nosotras': 'optimizamos',
            'vosotros/vosotras': 'optimizáis',
            'ellos/ellas/ustedes': 'optimizan'
        },
        'category': 'advanced',
    },
    {
        'word': 'investir',
        'definition': 'To invest',
        'tense': 'present',
        'conjugations': {
            'yo': 'invisto',
            'tú': 'inviertes',
            'él/ella/usted': 'inviste',
            'nosotros/nosotras': 'invertimos',
            'vosotros/vosotras': 'invertís',
            'ellos/ellas/ustedes': 'invisten'
        },
        'category': 'advanced',
    },
    {
        'word': 'colaborar',
        'definition': 'To collaborate',
        'tense': 'present',
        'conjugations': {
            'yo': 'colaboro',
            'tú': 'colaboras',
            'él/ella/usted': 'colabora',
            'nosotros/nosotras': 'colaboramos',
            'vosotros/vosotras': 'colaboráis',
            'ellos/ellas/ustedes': 'colaboran'
        },
        'category': 'advanced',
    },
    {
        'word': 'liderar',
        'definition': 'To lead',
        'tense': 'present',
        'conjugations': {
            'yo': 'lidero',
            'tú': 'lideras',
            'él/ella/usted': 'lidera',
            'nosotros/nosotras': 'lideramos',
            'vosotros/vosotras': 'lideráis',
            'ellos/ellas/ustedes': 'lideran'
        },
        'category': 'advanced',
    },
]

verbs.extend(intermediate_verbs)
nouns.extend(advanced_verbs)


for verb in verbs:
    term = Term(
        word=verb['word'],
        definition=verb['definition'],
        wordType='verb',
        tense=verb['tense'],
        conjugations=verb['conjugations']
    )
    term.save()
    categories = Category.objects.filter(name=adj['category'])
    term.categories.add(*categories)
