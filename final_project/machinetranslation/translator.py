"""
    This is a Translator that translate from English to French and vice-versa
"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
        This function translate the input text from English to French
    """
    if english_text is not None:
        translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        print(english_text + "--->" + translation.get('translations')[0].get('translation'))
        french_text = translation.get('translations')[0].get('translation')
        return french_text
    return "The provided input is null"

def french_to_english(french_text):
    """
        This function translate the input text from French to English
    """
    if french_text is not None:
        translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        print(french_text + "--->" + translation.get('translations')[0].get('translation'))
        english_text = translation.get('translations')[0].get('translation')
        return english_text
    return "The provided input is null"
