import PyPDF2

import pandas as pd
import re

import spacy
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('sentencizer')
nlp.pipe_names

def extract_text_from_pdf(pdf_path):
    # import PyPDF2
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page_number in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_number]
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def transcript_transform(transcript):
    # convert transcript string to nlp doc
    doc = nlp(transcript)
    list_of_tokens = []
    # apply sentence tokenization
    for sentence in doc.sents:
        text = re.sub('\n', '', str(sentence))
        text = re.sub(r'\s{2,}', '', text)
        list_of_tokens.append(str(text))
    # convert to dataframe
    token_df = pd.DataFrame(data=list_of_tokens, columns=['sentence'])
    return token_df

def df_to_list(speech_df):
    dflist = speech_df['sentence'].astype(str).tolist()
    newlist = []

    for text in dflist:
        newlist.append(text)
    return newlist

