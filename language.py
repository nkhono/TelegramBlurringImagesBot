import json
from config import *

translations = None

def refreshTranslation():
	global translations

	try:
		translations = json.loads(open(languageFile, 'r').read())
	except:
		translations = defaultStructure
		open(languageFile, 'w').write(json.dumps(translations))


def translate(language, word):
	refreshTranslation()

	if language in translations.keys():
		return translations[language][word]

	else:
		return translations['else'][word]


refreshTranslation()