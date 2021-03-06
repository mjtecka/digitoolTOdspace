import catalogue
import string
import unicodedata

def convertTag260(tag,oai_id):
    ret = {}
    
    if 'a' in tag.keys():
        place = tag['a'][0]
        if place[-2:] == ' :':
            place = place[:-2]
        ret['place'] = place
    
    if 'b' in tag.keys():
        if len(tag['b']) == 1:
            institut = tag['b'][0]
        elif len(tag['b']) == 2:
            institut = tag['b'][0] + tag['b'][1]
        else:
            raise Exception()
        if institut[-1] == ',':
            institut = institut[:-1]
        ret['institut'] = institut

    if 'c' in tag.keys():
        assert len(tag['c']) == 1
        year = tag['c'][0] 
        if year[0] == '[' and year[-1] == ']': 
            year = year[1:-1] 
        assert len(year) == 4
        ret['year'] = year
    
    for k in tag.keys():
        assert k in 'abc'
    return ret
