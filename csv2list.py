import csv
import pickle
lst=[]
with open('crawled.csv', 'r', encoding="utf8") as csvfile:
    rdr=csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in rdr:
        try:
            tmp=row[1].replace('"', '')
            print(tmp)
            if not tmp==('title'):
                lst.append(tmp)
        except:
            pass
with open('longlist', 'wb') as fp:
    pickle.dump(lst, fp)
