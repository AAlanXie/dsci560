import pandas as pd
import json


import re
import contractions

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk


from transformers import pipeline
import yake
from keybert import KeyBERT


class Sentence_Analyzer:
    def __init__(self, sentence):
        self.sentence = sentence
        self.tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}
        self.lemmatizer = WordNetLemmatizer()
        self.stop = stopwords.words('english')
        self.stop += ['rt', 'la', 'los', 'angeles', 'de', 'en', 'un', 'e', 'el', 'por', 'con', 'le', 'del']

    # def bart(self):
    #     summarizer = pipeline("summarization", model="facebook/bart-large-xsum")
    #     # print(summarizer(text, min_length=5, do_sample=False))
    #     # tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
    #     # model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
    #     # input_tokens = tokenizer.batch_encode_plus([example], return_tensors="pt",
    #     #                                            max_length=1024, truncation=True)["input_ids"]
    #     # encoded_ids = model.generate(input_tokens,num_beams=4, length_penalty=2.0,
    #     #                              no_repeat_ngram_size=3)
    #     # summary = tokenizer.decode(encoded_ids.squeeze(), skip_specail_tokens=True)
    #     # print(textwrap.fill(summary, 100))
    #     sum_result = summarizer(self.sentence, min_length=5, do_sample=False)[0]['summary_text']
    #     return sum_result
    #
    # def text_summarization(self):
    #     result = self.bart()
    #     return result
    def bart_summarize(self):
        summarizer = pipeline("summarization", model="facebook/bart-large-xsum")
        sum_result = summarizer(self.sentence, min_length=5, do_sample=False)[0]['summary_text']
        return sum_result


    def yake_function(self, numOfKeywords):
        # Specifying Parameters
        language = "en"
        max_ngram_size = 1
        deduplication_thresold = 0.9
        deduplication_algo = 'seqm'
        windowSize = 1
        numOfKeywords = numOfKeywords

        custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold,
                                                    dedupFunc=deduplication_algo, windowsSize=windowSize,
                                                    top=numOfKeywords,
                                                    features=None)
        keywords = custom_kw_extractor.extract_keywords(self.sentence)
        list1 = []
        for kw in keywords:
            list1.append(kw[0])
        return list1

    def keyword_extraction_1(self):
        return self.yake_function(5)




    def keybert_function(self):
        kw_model = KeyBERT("distilbert-base-nli-mean-tokens")
        # kw_words = kw_model.extract_keywords(example, keyphrase_ngram_range==(3,3), stop_words='english', use_mmr=True, diversity=0.5)
        kw_words = kw_model.extract_keywords(self.sentence)
        # print(kw_words)
        list1 = []
        for kw in kw_words:
            list1.append(kw[0])
        return list1

    def keyword_extraction_2(self):
        return self.keybert_function()


    # data cleaning
    def clean_text(self):
        text_lc = self.sentence.lower()  # to lowercase
        text_html = re.sub(r'<[^>]*>', ' ', text_lc)  # remove html
        text_url = re.sub(r'http\S+', ' ', text_html)  # remove url
        text_contract = contractions.fix(text_url)  # expand contractions
        text_alpha = re.sub(r'\W+', ' ', text_contract)  # remove non-alphabetical characters
        text_space = ' '.join(text_alpha.split())  # remove extra spaces
        text_token = word_tokenize(text_space)  # # tokenization
        text_stop = [word for word in text_token if word not in self.stop]  # remove the stop words
        text_tag = nltk.pos_tag(text_stop)  # tag text
        text_tag = [(wt[0], self.tag_dict.get(wt[1][0].upper(), wordnet.NOUN)) for wt in text_tag]
        text_lemma = [self.lemmatizer.lemmatize(wt[0], wt[1]) for wt in text_tag]  # lemmatization
        text = ' '.join(text_lemma)
        return text

    def sentiment_analysis(self):
        score = SentimentIntensityAnalyzer().polarity_scores(self.sentence)
        return score


if __name__ == '__main__':
    user_input = "La is beautiful"

    if user_input:
        sa = Sentence_Analyzer(user_input)
        # clean_text = sa.clean_text()
        # sentiment = sa.sentiment_analysis()
        # yake_keyword = sa.keyword_extraction_1()
        # keybert_keyword = sa.keyword_extraction_2()
        summerization = sa.bart_summarize()

        print(summerization)