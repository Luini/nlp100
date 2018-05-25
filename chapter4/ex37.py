import mecab
import ex36
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

if __name__ == "__main__":
    morphemesCount = ex36.count(mecab.formatter("neko.txt.mecab"))
    morphemesCount = sorted(morphemesCount.items(), key=lambda x: -x[1])
    morphemesCount = morphemesCount[:10]

    left = [1,2,3,4,5,6,7,8,9,10]
    height = [count for morpheme, count in morphemesCount]
    plt.bar(left, height)

    fp = FontProperties(fname='/Users/yushi/Library/Fonts/IPAfont00303/ipag.ttf', size=14)
    label = [morpheme for morpheme, count in morphemesCount]
    plt.xticks(left, label, fontproperties=fp)
    plt.title('頻度上位10語', fontproperties=fp)
    plt.xlabel('単語', fontproperties=fp)
    plt.ylabel('出現回数', fontproperties=fp)

    plt.show()
