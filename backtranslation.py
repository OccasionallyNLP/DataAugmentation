# googletrans 설치해야됨.
! pip install googletrans
import googletrans 
class BackTranslate(self):
    def __init__(self):
        self.count = 0
        self.translator = googletrans.Translator() 
    def backtranslate(sentence, lang1, lang2):
        print(f'how many syllables {self.count}')
        lang2_result = translator.translate(sentence, str=lang1, dest=lang2) 
        self.count+=len(sentence)
        result = translator.translate(result.text, str=lang2, dest=lang1)
        self.count+=len(result.text)
        retun result
