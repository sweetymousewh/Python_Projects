import itchat
import numpy as np
import pandas as pd
from collections import defaultdict
import re
import jieba
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image


itchat.login()
friends = itchat.get_friends(update=True)
count1 = 0
count2 = 0
count = 0
for i in range(0, len(friends)):
    if friends[i]['Sex'] == 1:
        count1 += 1
    elif friends[i]['Sex'] == 0:
        count2 += 1
    else:
        count += 1
print(count, count1, count2)
