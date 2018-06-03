import wikipedia
import datetime
import time
import pickle
import joblib
category = "Computer Science"

def isPageInRightCategory(page_str, cats):
    return page_str in cats
def getLinksFromPage(page_str):
    #print(wikipedia.page(page_str).categories)
    try:
        return list(set(wikipedia.page(page_str).links))
    except:
        time.sleep(2)
def crawl():
    all_pages=set()
    ret=500;
    next_offset = 0
    while len(all_pages)<9500:
        links_from_search = wikipedia.search("Computer Science", results=500, offset=next_offset)
        ret=len(links_from_search)
        next_offset += ret
        for p in links_from_search:
            all_pages.add(p)
        print(len(all_pages))
        time.sleep(2)
    with open('pagelist', 'wb') as fp:
        pickle.dump(all_pages, fp)
def load(item):
    with open(item, 'rb') as fp:
        return pickle.load(fp)

all_pages=load('longlist')

list_of_pages = []
print("Size of initial set:" , len(all_pages))
wikipedia.set_rate_limiting(True, min_wait=datetime.timedelta(0, 0, 50000))
for p_item in all_pages:
    try:
        for l_item in getLinksFromPage(p_item):
            try:
                if isPageInRightCategory(l_item, all_pages):
                    list_of_pages.append((p_item,l_item))
            except:
                pass
        print("size of edgelist: ", len(list_of_pages))
        with open('edgelist_long', 'wb') as fp:
            pickle.dump(list_of_pages, fp)
    except:
        pass

