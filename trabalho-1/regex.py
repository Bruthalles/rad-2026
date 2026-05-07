import re

text = 'Olá mundo 2026, email exemplo@dominio.com e phone 55-11-99999-0000'

# 1) Palavra completa: começa e termina em limite de palavra
#    \b = limite de palavra, \w = caractere de palavra, + = um ou mais
pattern_word = r'\b\w+\b'  # encontra palavras como 'Olá', 'mundo', '2026'

# 2) Dígitos: qualquer número de 0 a 9
#    \d = dígito, + = um ou mais
pattern_digits = r'\d+'  # encontra sequências de dígitos como '2026', '55', '11', '99999', '0000'

# 3) Não dígitos: caracteres que não são números
#    \D = não dígito, + = um ou mais
pattern_non_digits = r'\D+'  # encontra texto que não é dígito, como 'Olá mundo '

# 4) Espaços em branco: espaço, tab, nova linha
#    \s = espaço em branco, + = um ou mais
pattern_spaces = r'\s+'  # encontra espaços entre palavras

# 5) Não espaços: qualquer caractere que não seja espaço
#    \S = não espaço em branco, + = um ou mais
pattern_non_spaces = r'\S+'  # encontra palavras e símbolos juntos

# 6) Qualquer caractere (exceto nova linha)
#    . = qualquer caractere, + = um ou mais
pattern_any = r'.+'  # encontra toda linha de texto não vazia

# 6.1) Quantificador lazy (não guloso)
#    .*? = qualquer caractere, o mínimo possível até a próxima parte corresponder
pattern_lazy = r'\b\w+.*?\d+\b'  # encontra primeira palavra seguida da menor sequência até dígitos

# 7) Início e fim de linha
#    ^ = início da linha ou string
#    $ = fim da linha ou string
#    \w+ = palavra no começo, .* = qualquer texto no meio, \w+ = palavra no fim
pattern_line = r'^\w+.*\w+$'  # começa com palavra e termina com palavra na mesma linha

# 8) Classe de caracteres: qualquer letra minúscula ou maiúscula
#    [A-Za-z] = letras de a até z e de A até Z, + = um ou mais
pattern_letters = r'[A-Za-z]+'  # encontra sequências apenas de letras

# 9) Classe negada: qualquer caractere que não seja letra ou dígito
#    [^\w] = não caractere de palavra, + = um ou mais
pattern_not_word = r'[^\w]+'  # encontra espaços e pontuação como ', ' e ' '

# 10) Quantificador opcional: zero ou uma ocorrência
#    o? = zero ou uma letra 'o'
pattern_optional = r'colou?r'  # encontra 'color' ou 'colour'

# 11) Quantificador de repetição exata / faixa
#    {2,3} = entre 2 e 3 ocorrências do dígito
pattern_repeat = r'\d{2,3}'  # encontra sequências de 2 ou 3 dígitos, como '55' e '11'

# 12) Grupo e alternância: uma das palavras dentro do parêntese
#    ( ... ) = grupo, | = ou
pattern_group = r'(email|phone|mundo)'  # encontra 'email', 'phone' ou 'mundo'

patterns = [
    ('palavra', pattern_word),
    ('dígitos', pattern_digits),
    ('não dígitos', pattern_non_digits),
    ('espaços', pattern_spaces),
    ('não espaços', pattern_non_spaces),
    ('qualquer caractere', pattern_any),
    ('lazy (não guloso)', pattern_lazy),
    ('início e fim', pattern_line),
    ('letras', pattern_letters),
    ('não palavra', pattern_not_word),
    ('opcional', pattern_optional),
    ('repetição', pattern_repeat),
    ('grupo/alternância', pattern_group),
]

for name, pattern in patterns:
    matches = re.findall(pattern, text)
    print(f'{name}:', pattern, '=>', matches)