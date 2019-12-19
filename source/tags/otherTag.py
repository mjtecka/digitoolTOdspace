import catalogue

def convertTag001(tag001,oai_id,categorize):
    return {'aleph_id': tag001} 

def convertTagC30(tagC30,oai_id,categorize):
    #print(oai_id, tagC30) 
    return {}

def convertTag020(tag020,oai_id,categorize):
    #print(oai_id, tag020) 
    return {}

def convertTag500(tag500,oai_id,categorize):
    #print(oai_id, tag500) 
    return {}

def convertTag490(tag490,oai_id,categorize):
    #print(oai_id, tag490) 
    return {}

def convertTagTYP(tagTYP,oai_id,categorize):
    #print(oai_id, tagTYP) 
    return {}


def convertTag008(tag008,oai_id,categorize):
    #print(oai_id, tag008)
    lang = tag008[35:38]
    if lang not in catalogue.convertLang.keys():
        #TODO kouknout kolik jich je a pak ignorovat?
        #print(oai_id, lang)
        return {}
    return {'lang': catalogue.convertLang[lang]}

def convertTag526(tag526,oai_id,categorize):
    ret = {'discipline': tag526['a'][0] }
    if len(tag526['a']) > 1:
        ret['program'] = tag526['a'][1]
    return ret

def convertTag600(tag600,oai_id,categorize):
    if '2' in tag600:
        return {'czenas': tag600['a']} 
    else:
        return {'keywords': tag600['a']} 

def convertTag610(tag610,oai_id,categorize):
    if '2' in tag610:
        return {'czenas': tag610['a']} 
    else:
        return {'keywords': tag610['a']} 

def convertTag630(tag630,oai_id,categorize):
    return {'keywords': tag630['a']} 

def convertTag648(tag648,oai_id,categorize):
    if '2' in tag648:
        return {'czenas': tag648['a']} 
    return {'keywords': tag648['a']} 

def convertTag651(tag651,oai_id,categorize):
    if '2' in tag651:
        return {'czenas': tag651['a']} 
    return {'keywords': tag651['a']} 

