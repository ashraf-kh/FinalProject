import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('Uxor8LslBYi1ex-r6BRH3vxR2v-it84cvdTeMkuwn4z2')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/b3753125-2e0d-446c-9660-afd720e8f619')


def english_to_french(english_text):
    translation = language_translator.translate(text=english_text, model_id="en-fr").get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text1):
    translation = language_translator.translate(text=french_text1,model_id="fr-en").get_result()
    english_text1 = translation['translations'][0]['translation']
    return english_text1
