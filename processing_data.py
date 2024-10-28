import re


def add_brackets(text, stem):
    pattern = rf'\b({stem}\w*)\b'
    return re.sub(pattern, r'<\1>', text, flags=re.IGNORECASE)

def clean_sentence(text):
    text = re.sub(r'<\/?s>', '', text)
    text = re.sub(r'\s+\.', '.', text)
    return text.strip()


def processing_df(df, word, stem, freq):
    df.rename(columns={'Sentence': 'example', 'GDEX score': 'gdex'}, inplace=True)
    df['example'] = df['example'].apply(lambda x: add_brackets(x, stem))
    df['example'] = df['example'].apply(clean_sentence)
    df['word'] = word
    df['frequency'] = freq
    df = df[['word','frequency','example','gdex']]
    return df


