from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(text_file):
    with open(text_file, 'r') as file:
        text = file.read()
    wordcloud = WordCloud(width=800, height=400).generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    # Guardar la imagen directamente en lugar de mostrarla
    plt.savefig('wordcloud.png')


