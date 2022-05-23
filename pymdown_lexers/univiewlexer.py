"""A Pygments lexer for Uniview"""
from pygments.lexer import RegexLexer, bygroups
from pygments.token import *


class UniviewLexer(RegexLexer):
	name: str = "Uniview"
	aliases = ['uniview', 'uv']
	filenames = ['*.uv']

	tokens = {
		'root': [
			(r'[^/]+', Text),
			(r'/\*', Comment.Multiline, 'comment'),
			(r'//.*?$', Comment.Singleline),
			(r'/', Text)
		],
		'comment': [
			(r'[^*/]+', Comment.Multiline),
			(r'/\*', Comment.Multiline, '#push'),
			(r'\*/', Comment.Multiline, '#pop'),
			(r'[*/]', Comment.Multiline)
		]
	}