from keybert import KeyBERT
from sentence_transformers import SentenceTransformer

def keywordEx(rawdocs):

    sentence_model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
    kw_model = KeyBERT(model=sentence_model)

    temp = kw_model.extract_keywords(rawdocs, keyphrase_ngram_range=(1,1), stop_words=None)
    keywords = []
    for i in temp:
        keywords.append(i[0])
    return keywords