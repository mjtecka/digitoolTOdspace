
def convertTag700(tag700, oai_id, categorize):
    if not 'a' in tag700.keys() or not '4' in tag700.keys():
        return {} #je to jen doplňková informace
    assert 'a' in tag700.keys() and '4' in tag700.keys()
    persons = tag700['a']
    roles = tag700['4']
    #assert len(persons) == len(roles)
    if len(persons) != len(roles):
        #print(oai_id, persons, roles)
        #TODO
        return {}
    ret = {}
    for i in range(len(persons)):
        if roles[i] == 'aut':
            ret['author'] = persons[i]
        elif roles[i] == 'edt':
            ret['editor']=persons[i]
        else:
            #print(oai_id, roles[i])
            #TODO mělo by být prázdné
            pass #neřeším others a dalšich pár
    return ret
