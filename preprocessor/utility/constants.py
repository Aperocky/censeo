# False 	class 	finally 	is 	return
# None 	continue 	for 	lambda 	try
# True 	def 	from 	nonlocal 	while
# and 	del 	global 	not 	with
# as 	elif 	if 	or 	yield
# assert 	else 	import 	pass
# break 	except 	in 	raise

# Basics Keywords
IMPORT_KEYWORD = "gravatus"
CLASS_KEYWORD = "species"
RETURN_KEYWORD = "redditus"
DEF_KEYWORD = "definitus"
YIELD_KEYWORD = "cessus"

# Boolean keywords
IF_KEYWORD = "si"
ELSEIF_KEYWORD = "aliud"
ELSE_KEYWORD = "nisi"
OR_KEYWORD = "vel"
IS_KEYWORD = "est"
AND_KEYWORD = "etiam"

# Loop keywords
WHILE_KEYWORD = "dum"
FOR_KEYWORD = "pro"
CONTINUE_KEYWORD = "persevero"

# Symbols
COLON_SYMBOL = "ergo"
EQUALITY_SYMBOL = "aequalis"
ASSIGNMENT_SYMBOL = "attributio"
GT_SYMBOL = "maior"
LT_SYMBOL = "minor"
PLUS_SYMBOL = "plus"
MINUS_SYMBOL = "minus"
COMMA_SYMBOL = "et"

# Built in functions
RANGE_FUNCTION = "range"
LIST_FUNCTION = "album"
DICT_FUNCTION = "tabula"
PRINT_FUNCTION = "scribo"

# CENSEO SPECIFICS
EMPTY_STRING = "inanis"
QUOTE_BEGINS = "quote"
QUOTE_ENDS = "quoto"
PARENTH_START = "sic"
PARENTH_END = "cis"
STATEMENT_ENDS = "positus"
BLOCK_ENDS = "finis"

DOT_SYMBOL = "ordinatis"

keyword_map = {
    IMPORT_KEYWORD : "import",
    CLASS_KEYWORD : "class",
    RETURN_KEYWORD : "return",
    DEF_KEYWORD : "def",
    YIELD_KEYWORD : "yield",

    IF_KEYWORD : "if",
    ELSEIF_KEYWORD : "else if",
    ELSE_KEYWORD : "else",
    OR_KEYWORD : "or",
    AND_KEYWORD : "and",
    IS_KEYWORD : "is",

    WHILE_KEYWORD : "while",
    FOR_KEYWORD : "pro",
    CONTINUE_KEYWORD : "continue",
}

symbol_map = {
    COLON_SYMBOL : "__COLON_LITERAL",
    EQUALITY_SYMBOL : "==",
    ASSIGNMENT_SYMBOL : "=",
    PLUS_SYMBOL : "+",
    MINUS_SYMBOL : "-",
    GT_SYMBOL : ">",
    LT_SYMBOL : "<",
    COMMA_SYMBOL : ",",
}

function_map = {
    RANGE_FUNCTION : "range",
    LIST_FUNCTION : "list",
    DICT_FUNCTION : "dict",
    PRINT_FUNCTION : "print",
}

censeo_map = {
    EMPTY_STRING : "\"\"",
    QUOTE_BEGINS : "\"",
    QUOTE_ENDS : "\"",
    PARENTH_START : "(",
    PARENTH_END : ")",
    STATEMENT_ENDS : "__STATEMENT_END_LITERAL",
    BLOCK_ENDS : "__BLOCK_END_LITERAL",
    DOT_SYMBOL : "__DOT_SYMBOL_LITERAL",
}
