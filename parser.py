import ply.yacc as yacc
from lexer import tokens

# Definición de la gramática específica
def p_statement_for(p):
    '''statement : FOR LPAREN INT ID EQUALS NUMBER SEMICOLON ID LESS_EQUAL NUMBER SEMICOLON ID PLUSPLUS RPAREN LBRACE print_statement RBRACE'''
    if (p[4] == "i" and p[6] == 1 and p[8] == "i" and p[10] == 10 and p[12] == "i"):
        p[0] = "Estructura FOR correcta"
    else:
        p[0] = "Estructura FOR incorrecta"

def p_print_statement(p):
    '''print_statement : ID DOT OUT DOT PRINTLN LPAREN STRING PLUS NUMBER RPAREN SEMICOLON'''
    if (p[1] == "system" and p[3] == "out" and p[5] == "println" and p[7] == '"Numero: "' and p[9] == 1):
        p[0] = "Estructura FOR correcta"
    else:
        p[0] = "Estructura FOR incorrecta"

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
        p[0] = "Estructura FOR incorrecta"
    else:
        print("Syntax error at EOF")
        p[0] = "Estructura FOR incorrecta"

# Construir el analizador sintáctico
parser = yacc.yacc()
