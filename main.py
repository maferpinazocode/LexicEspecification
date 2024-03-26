# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# r'atring' -> r significa que la cadena es tradada sin caracteres de escape, 
# es decir r'\n' seria un \ seguido de n (no se interpretaria como salto de linea) 

 # List of token names.   This is always required
tokens = (
    'RETURN',
    'COMMENT',
    'FOR',
    'IF',
    'ELSE',
    'IN',
    'RANGE',
    'AND',
    'OR',
    'TRUE',
    'FALSE',
    'MAIN',
    'DISPLAY',
    'INPUT',
    'NUMBER',
    'FLOAT',
    'LITERAL',
    'DEF',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LSLASH',
    'RSLASH',
    'TYPEBOOL',
    'BOOL',
    'TYPEINT',
    'ID',
    'EQUALEQUAL',
    'EQUAL',
    'DIFERENCE',
    'LESS',
    'GREATER',
    'LESSEQUAL',
    'GREATEREQUAL',
    'LCORCH',
    'RCORCH',
    'TWODOTS',
    'COMMA',
    
)
 
 # Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQUALEQUAL = r'\=='
t_EQUAL   = r'\='
t_DIFERENCE = r'\!='
t_LESS    = r'\<'
t_GREATER = r'\>'
t_LESSEQUAL    = r'\<='
t_GREATEREQUAL = r'\>='
t_LSLASH  = r'\{'
t_RSLASH  = r'\}'
t_TWODOTS = r'\:'
t_COMMA   = r'\,'
t_LCORCH  = r'\['
t_RCORCH  = r'\]'
#t_NUMBER  = r'\d+'
 
# A regular expression rule with some action code
def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_FOR(t):
    r'for'
    return t

def t_INPUT(t):
    r'input'
    return t

def t_RANGE(t):
    r'range\b'
    return t

def t_RETURN(t):
    r'return'
    return t
    
def t_AND(t):
    r'and'
    return t
    
def t_OR(t):
    r'or'
    return t
    
def t_TRUE(t):
    r'True'
    return t
    
def t_FALSE(t):
    r'False'
    return t

def t_COMMENT(t):
    r'\#.*'
    return t

def t_MAIN(t):
    r'main'
    return t

def t_DISPLAY(t):
    r'display'
    return t
    
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)  # Convertir el valor a tipo float
    return t
    
def t_TYPEBOOL(t):
    r'bool'
    t.type = 'TYPEBOOL'
    return t

def t_BOOL(t):
    r'true|false|True|False'
    t.value = True if t.value.lower() == 'true' else False
    return t
    
def t_TYPEINT(t):
    r'int'
    t.type = 'TYPEINT'
    return t
    
def t_IN(t):
    r'in'
    return t
    
def t_DEF(t):
    r'rey'
    t.type = 'DEF'
    return t
    
def t_LITERAL(t):
    r"'([^']*)'"
    return t
    
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # guardamos el valor del lexema  
    #print("se reconocio el numero")
    return t
 
 # Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
 # A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
 # Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
 
# Build the lexer
lexer = lex.lex()

# Test it out
data = ''' 

saludo = mensaje + ' ' + nombre

x = 10 + 20 * 3 - 5 / 2
a = True
b = False

if x > 10:
    display('x es mayor que 10')
else:
    display('x es menor o igual a 10')

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    display(numero)

rey main () {
int numero
display ('Enter a number : ')
input ( n )
result = factorial (n )
display('Iterative factorial of ' + number + ': ' + result)
}

rey iterative_factorial ( int number ):
result = 1
for i in range (1 , n + 1):
resultado *= i
return result
    '''
 
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    #print(tok)
    print(tok.type, tok.value, tok.lineno, tok.lexpos)