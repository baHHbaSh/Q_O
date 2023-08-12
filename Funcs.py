from random import randint
from fuzzywuzzy import fuzz
import os
from functools import cache
def getcwd():
	dir = list(__file__)
	Backslash = list(dir)[2]
	while dir[-1] != Backslash:
		dir.pop(-1)
	result = ""
	for Symb in dir:
		result = result + Symb
	return str(result)
def LaunchExe(path):
	os.startfile(path)
@cache
def ratio(s1: str, s2:str, koff:int = 80):
	s1 = s1.lower()
	s2 = s2.lower()
	return (fuzz.QRatio(s1, s2) > koff)
def rand_in_list(s1: list):
	return s1[randint(0, (len(s1)-1))]
def in_list(s1: str, s2:list) -> bool:
	if isinstance(s2, list):
		for i in s2:
			if i in s1:
				return True
		return False
	elif isinstance(s2, str):
		if s2 in s1:
			return True
		return False
def word_in(word:str, text:str):
	for i in text.split(" "):
		if word == i:
			return True
	return False
def first_word(word, text):
	if word == text.split(" ")[0]:
		return True
	return False
def on_end(s1: str, s2: str):
	s1 = s1.split(" ")
	if s1[-1] == s2:
		return True
	return False