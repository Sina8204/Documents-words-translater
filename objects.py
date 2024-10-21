from deep_translator import GoogleTranslator as gt
from persian_converter import fprint #for convert persian
from arabic_reshaper import reshape 
from bidi.algorithm import get_display 

class get_text ():
    #this function remove characters in word.txt file from our text
    def remove_extra_character(self , text:str):
        self.words = text.split(' ') # convert text to list
        with open ('word.txt' , 'r' , encoding='utf-8') as file : #open word.txt file to read
            self.content = file.read() + '\n '
            for i in self.content:
                for j in self.words :
                    if i in j:
                        #self.words.remove(j) #----> for delet this element
                        self.words[self.words.index(j)] = self.words[self.words.index(j)].replace(i , '')
        return self.words
    #
    #this function delete elements who are more than one in the list
    def similare_word_deleter(self , lst : list):
        self.output_list = []
        for i in lst:
            if i not in self.output_list:
                self.output_list.append(i)
        for i in self.output_list:
            if i == '':
                self.output_list.pop(self.output_list.index(i))
        return self.output_list
    #
    #this function save words who aren't in the saved_words.txt file
    def saving_words (self , text : list , adress : str):
        with open (adress , 'r' , encoding='utf-8') as file_read:
            self.saved_words = file_read.read()
        self.saved_words = self.saved_words.split('\n')
        with open (adress , 'a' , encoding='utf-8') as file_write:
            for i in text :
                if i not in self.saved_words:
                    file_write.write(f'{i}\n')
                else :
                    continue
            
    #
    #this function fix our farsi characters and words. for exampele (ﻡﻼﺳ --> سلام)
    def fix_text_saving (self , text:str):
        self.converted_text2 = fprint(text) # it convert to the farsi font but now it's bad 
        self.reshaped_text2 = reshape(self.converted_text2) # so we try to fix that
        self.bidi_text2 = get_display(self.reshaped_text2) # now it's fix :)
        return self.bidi_text2


class translater (gt):
    def __init__(self, source = "auto", target = "en", proxies = None, **kwargs):
        super().__init__(source, target, proxies, **kwargs)
    #
    #this function do translating our text
    def translate(self, text, **kwargs):
        self.output = super().translate(text, **kwargs)
        self.converted_text = self.output #fprint(self.output) # it convert to the farsi font but now it's bad 
        self.reshaped_text = reshape(self.converted_text) # so we try to fix that
        self.bidi_text = get_display(self.reshaped_text) # now it's fix :)
        return self.bidi_text
    

