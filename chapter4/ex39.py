import mecab
import ex36
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

if __name__ == "__main__":
    morphemesCount = ex36.count(mecab.formatter("neko.txt.mecab"))
    morphemesCount = sorted(morphemesCount.items(), key=lambda x: -x[1])

    x = [i+1 for i in range(len(morphemesCount))]
    y = [m[1] for m in morphemesCount]
    plt.xscale("log")
    plt.yscale("log")
    plt.plot(x, y)

    fp = FontProperties(fname='/Users/yushi/Library/Fonts/IPAfont00303/ipag.ttf', size=14)
    plt.title('両対数グラフ', fontproperties=fp)
    plt.xlabel('出現頻度順位（log）', fontproperties=fp)
    plt.ylabel('出現頻度（log）', fontproperties=fp)

    plt.show()
