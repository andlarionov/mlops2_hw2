import pandas as pd
import re


df = pd.read_csv('data.csv')


# Очистка текста
def clear_text(text):
    text = re.sub(r"[Â]+", "'", text)  # Замена Â символов на апостроф.
    text = re.sub(r"#\w+", "", text)  # Удаление хэштегов

    # Удаление эмодзи и спецсимволов, оставляя знаки препинания и цифры
    text = re.sub(r"[^\w\s,.!?;:0-9]", "", text)  # Оставляем буквы, пробелы, знаки препинания и цифры

    text = " ".join(text.split())  # Удаление лишних пробелов
    
    return text


# Очистка и лемматизация
df['rubrics'] = df['rubrics'].apply(clear_text)


df.to_csv('cleaned_data.csv', index=False)