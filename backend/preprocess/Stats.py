import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import WhitespaceTokenizer
import json
import re
import stanza
import itertools

class Stats:
    nltk.download('punkt')

    def count_tokens(self, text):
        return len(nltk.word_tokenize(text))

    def total_len(self, text):
        return len(text)

    def normostrana(self,text):
        return round(self.total_len(text)/1800,2)

    def len_without_spaces(self, text):
        return len(text.replace(" ", ""))

    def count_whitespaces(self, text):
        return text.count(" ")

    def count_words(self,text):
        text = re.sub(r'[^\w\s]', '', text)
        tokenizer = WhitespaceTokenizer()
        return len(tokenizer.tokenize(text))

    def unique_words(self, text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        tokenizer = WhitespaceTokenizer() 
        words = tokenizer.tokenize(text)
        count_unique = len(set(words))
        percent_uniqe = round(count_unique/len(words)*100,2)
        return len(set(words)), percent_uniqe

    def unique_words_list(self,text):
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        no_dupl = set(words)
        return list(no_dupl)

    def avg_word(self,list):
        unique_words_list = self.unique_words_list(list)
        return round(sum(len(word) for word in unique_words_list) / len(unique_words_list), 2)

    def avg_sentence_chars(self,text):
        sent = sent_tokenize(text)
        return round(sum(len(word) for word in sent) / len(sent))

    def avg_sentence_words(self, text):
        sent = sent_tokenize(text)
        return round(sum(len(x.split()) for x in sent) / len(sent))

    def num_sentences(self, text):
        return(len(sent_tokenize(text)))

    def word_stats(self, text):
        text = text.lower()
        text = text = re.sub(r'[^\w\s]', '', text)
        tags = []
        stanza.download('sk')
        nlp = stanza.Pipeline('sk', processors='tokenize, pos, lemma')
        doc = nlp(text)
        tags.append([f'{word.text}:{word.lemma}:{word.xpos[:2].upper()}:{word.upos.upper()}' for sent in doc.sentences for word in sent.words])
        tag_arr= []
        for tag in tags:
            for t in tag:
                line = t.split(":")
                tag_arr.append([line[0],#slovo
                                line[2],#tag
                                text.count(line[0]),#frekvencia slova
                                len(line[0]),#dlzka slova
                                line[1],#lema
                                text.count(line[1]),#frekvencia lemy
                                len(line[1]),#dlzka lemy
                                line[3]#upos
                                ]),                           
        no_dupl = []
        for l in tag_arr:
            if l not in no_dupl:
                no_dupl.append(l)
        
        upos_dict = {}
        upos_str = ""
        for tag in tag_arr:
            upos_str += tag[7]+" "             
        upos_dict["ADJ"] = upos_str.count("ADJ")
        upos_dict["ADP"] = upos_str.count("ADP")
        upos_dict["ADV"] = upos_str.count("ADV")
        upos_dict["CCONJ"] = upos_str.count("CCONJ")
        upos_dict["DET"] = upos_str.count("DET")
        upos_dict["INTJ"] = upos_str.count("INTJ")
        upos_dict["NOUN"] = upos_str.count("NOUN")
        upos_dict["NUM"] = upos_str.count("NUM")
        upos_dict["PRON"] = upos_str.count("PRON")
        upos_dict["PROPN"] = upos_str.count("PROPN")
        upos_dict["VERB"] = upos_str.count("VERB")
        
        
       
        
        
        return  no_dupl, upos_dict





