
def convertTag100(tag100,oai_id):
    ret = {}
    if 'a' in tag100.keys():
        assert len(tag100['a']) == 1, tag100
        author = tag100['a'][0]
        if author[-1] == ',':
            author = author[:-1]
        ret['author'] = [author]
    if 'c' in tag100.keys(): # má tam být Dr a pod nikoliv 'psychologie'
        assert len(tag100['c']) == 1
        if not tag100['c'] in ['PhDr','ml','Dr']:
            raise Exception("100c neznámá hodnota  {}".format(tag100['c']))
    if 'd' in tag100.keys(): # narození (a úmrti) autora
        pass 
    if 'q' in tag100.keys():
        assert 'obhaj' in tag100['q'][0]
    if '4' in tag100.keys():
        if not tag100['4'][0] in ['dis','aut','ths']:
            pass
    if '7' in tag100.keys():
        pass
    if 'u' in tag100.keys():
        pass
    for key in tag100.keys():
        if not key in 'acdq47u':
            raise Exception("Unkown key {}".format(key))
    return ret
