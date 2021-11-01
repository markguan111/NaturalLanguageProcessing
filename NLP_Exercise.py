import matplotlib.pyplot as plt
from operator import itemgetter
from nltk.corpus import stopwords
from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd
from pathlib import Path
import imageio
from wordcloud import WordCloud

nltk.download("stopwords")

stops = stopwords.words("english")
print(stops)

blob = TextBlob(Path("book of John text.txt").read_text())

more_stops = ["thy", "ye", "verily", "thee", "hath", "say", 
               "thou", "art", "shall"]

stops += more_stops

items = blob.word_counts.items()

print(items)

clean_items = [i for i in items if i[0] not in stops]

sorted_list = sorted(clean_items, key=itemgetter(1), reverse=True)

Top15 = sorted_list[:16]

#df = pd.DataFrame(sorted_list, columns=["word", "count"])

print(Top15)

First = []  
for i in Top15:
    x = i[0]
    First.append(x)

#with open("file.txt", "w") as output:
    #output.write(str(First))

#text1 = Path('file.txt').read_text()
New_text = ' '.join(First)
mask_image = imageio.imread("mask_rectangle.png")

wordcloud = WordCloud(colormap="winter", mask=mask_image,
                      background_color="gray")

wordcloud = wordcloud.generate(New_text)

wordcloud = wordcloud.to_file("book of John tex.png")

print("done")



