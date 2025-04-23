from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud_image(text):
    wc = WordCloud(width=800, height=400, background_color="white", font_path="simhei.ttf")
    wc.generate(text)
    wc.to_file("static/wordcloud.png")