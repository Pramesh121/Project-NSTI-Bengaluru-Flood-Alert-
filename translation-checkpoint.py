from googletrans import Translator

def translate_message(message, dest_language='hi'):
    translator = Translator()
    translated = translator.translate(message, dest=dest_language)
    return translated.text
