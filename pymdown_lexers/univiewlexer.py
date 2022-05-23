"""A Pygments lexer for Uniview"""
from pygments.lexer import RegexLexer, include, bygroups, words, default
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
		Number, Punctuation, Whitespace


__all__ = ['UniviewLexer']

class UniviewLexer(RegexLexer):
	name: str = "Uniview"
	aliases = ['uniview', 'uv']
	filenames = ['*.uv']
	mimetypes = ['text/uniview', 'text/x-uniview']

	keyword_types = (words((
		'u8', 'u16', 'u32', 'u64', 'i8', 'i16', 'i32', 'i64', 'int',
		'size', 'f32', 'f64', 'cstring', 'bool',
	), suffix=r'\b'), Keyword.Type)

	tokens = {
		'root': [
			(r'#![^[\r\n].*$', Comment.Preproc),
			default('base'),
		],
		'base': [
			# (r'/\*', Comment.Multiline, 'comment'),
			# (r'//.*?$', Comment.Singleline),
			# Whitespace and Comments
			(r'\n', Whitespace),
			(r'\s+', Whitespace),
			(r'//.*?$', Comment.Single),
			(r'/\*', Comment.Multiline, 'comment'),
			
			# Keywords
			(words(('as', 'else', 'external', 'if', 'return', 'delete', 'import'),
			suffix=r'\b'), Keyword),

			(r'(true|false)\b', Keyword.Constant),
			(r'this\b', Name.Builtin.Pseudo),
			(r'let\b', Keyword.Declaration),
			(r'fn\b', Keyword, 'funcname'),
			(r'(struct|class)\b', Keyword, 'typename'),

			# Path separators, so types don't catch them.
			(r'::\b', Text),
			# Types in positions.
			(r'(?::|->)', Text, 'typename'),

			(r'[0-9][0-9_]*', Number.Integer, 'number_lit'),

			# # String literals
			(r'"', String, 'string'),
			(r'(?s)b?r(#*)".*?"\1', String),

			# # Operators and Punctuation
			(r'\.\.=?', Operator),
			(r'[{}()\[\]\#,.;]', Punctuation),
			(r'[+\-*/%&|<>^!~\@\$=:?]', Operator),

			# Identifiers
			(r'[a-zA-Z_]\w*', Name),
			
			(r'[^/]+', Text),
		],
		'comment': [
			(r'[^*/]+', Comment.Multiline),
			(r'/\*', Comment.Multiline, '#push'),
			(r'\*/', Comment.Multiline, '#pop'),
			(r'[*/]', Comment.Multiline),
		],
		'funcname': [
			(r'\s+', Text),
			(r'[a-zA-Z_]\w*', Name.Function, '#pop'),
			default('#pop'),
		],
		'typename': [
			(r'\s+', Text),
			(r"$", Operator),
			(r"@", Operator),
			keyword_types,
			(r'[a-zA-Z_]\w*', Name.Class, '#pop'),
			default('#pop'),
		],
		'number_lit': [
			(r'[ui](8|16|32|64|size)', Keyword, '#pop'),
			(r'f(32|64)', Keyword, '#pop'),
			default('#pop'),
		],
		'string': [
			(r'"', String, '#pop'),
			(r"""\\['"\\nrt]|\\x[0-7][0-9a-fA-F]|\\0"""
			 r"""|\\u\{[0-9a-fA-F]{1,6}\}""", String.Escape),
			(r'[^\\"]+', String),
			(r'\\', String),
		]
	}