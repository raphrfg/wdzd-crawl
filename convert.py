import pickle
with open('edgelist', 'rb') as fp:
    edges=pickle.load(fp)
with open('pagelist', 'rb') as fp:
    vertices = list(pickle.load(fp))
elist_gephi = []
'''for pair in edges:
    elist_gephi.append((vertices.index(pair[0]), vertices.index(pair[1])))'''
print("writing")
with open('nodes_gephi.csv', 'w') as fp:
    print('title',ig ';', file=fp)
    for item in vertices:
        try:
            print(item,';', file=fp)
        except:
            print('undefined', file=fp)
with open('edges_gephi_names.csv', 'w') as fp:
    for pair in edges:
        try:
            print(pair[0].replace(';',''),  ";" , pair[1].replace(';','') , file=fp)
        except:
            pass
