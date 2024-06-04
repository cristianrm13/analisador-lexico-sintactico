import ply.lex as lex

# Lista de tokens
tokens = (
    'FOR', 'INT', 'ID', 'NUMBER', 'PLUS', 'LESS_EQUAL', 'SEMICOLON', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'DOT', 'OUT', 'PRINTLN', 'STRING', 'EQUALS', 'PLUSPLUS'
)

# Reglas de expresión regular para tokens simples
t_PLUS = r'\+'
t_LESS_EQUAL = r'<='
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DOT = r'\.'
t_EQUALS = r'='
t_PLUSPLUS = r'\+\+'
t_STRING = r'\".*?\"'

# Reglas de tokens con acciones asociadas
def t_FOR(t):
    r'for'
    return t

def t_INT(t):
    r'int'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_OUT(t):
    r'out'
    return t

def t_PRINTLN(t):
    r'println'
    return t

def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Construir el analizador léxico
lexer = lex.lex()
