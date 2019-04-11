import processing.chapter1 as chap1
import processing.chapter2 as chap2
import processing.chapter3 as chap3

# chapter1
chap1.p00.processing00().execute("stressed")
chap1.p01.processing01().execute("パタトクカシーー")
chap1.p02.processing02().execute(["パトカー", "タクシー"])
chap1.p03.processing03().execute("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.")
chap1.p04.processing04().execute("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.")
chap1.p05.processing05().execute("I am an NLPer")
chap1.p06.processing06().execute(["paraparaparadise","paragraph"])
chap1.p07.processing07().execute([12, "気温", 22.4])
chap1.p08.processing08().execute("Hello World !")
chap1.p09.processing09().execute("Hello World !")

# chapter2

# ファイルを開く
tempPath = "./data/hightemp.txt"
f = open(tempPath, "r", encoding="utf-8")

chap2.p10.processing10().execute(f)
chap2.p11.processing11().execute(f)
chap2.p12.processing12().execute(f)
chap2.p13.processing13().execute("")
chap2.p14.processing14().execute([f, 5])
chap2.p15.processing15().execute([f, 5])
chap2.p16.processing16().execute([tempPath, 5])
chap2.p17.processing17().execute(f)
chap2.p18.processing18().execute(f)
chap2.p19.processing19().execute(f)

f.close()

# chapter3
wikiPath = "./data/jawiki-country.json"
wiki = open(wikiPath, "r", encoding="utf-8")

uk = chap3.p20.processing20().execute(wiki)
chap3.p21.processing21().execute(uk)
chap3.p22.processing22().execute(uk)
chap3.p23.processing23().execute(uk)
chap3.p24.processing24().execute(uk)
chap3.p25.processing25().execute(uk)
chap3.p26.processing26().execute(uk)

wiki.close()
