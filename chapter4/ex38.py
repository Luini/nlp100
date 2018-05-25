import mecab
import ex36
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

if __name__ == "__main__":
    morphemesCount = ex36.count(mecab.formatter("neko.txt.mecab"))

    x = [count for count in morphemesCount.values()]
    plt.hist(x, log=True)

    fp = FontProperties(fname='/Users/yushi/Library/Fonts/IPAfont00303/ipag.ttf', size=14)
    plt.title('単語の出現頻度のヒストグラム', fontproperties=fp)
    plt.xlabel('出現回数', fontproperties=fp)
    plt.ylabel('単語の種類数（log）', fontproperties=fp)

    plt.show()
