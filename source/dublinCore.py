import commonTag
# seznam už ověřených / pročištěných
# transtledet je vždy ten druhý z (en,cz)
# subject je keywords a '53 - Fyzika' TODO nechat tam?, přidat description? (ve kterém je zadání) 
# dayAccepted, abscract, name nejsou všude přestože jsou povinné
# contributor není vyplněn místo toho je advisor a referee
# do modified vyplnit vlastní datum
# dc:type vyplnit i pro přílohy
# identifier je třeba překopat - handle
# degree vůbec neexistuje
dcParsed = '''
{http://purl.org/dc/elements/1.1/}language
{http://purl.org/dc/elements/1.1/}title
{http://purl.org/dc/terms/}translated
{http://purl.org/dc/terms/}alternative
{http://purl.org/dc/terms/}alternativeTranslated
{http://purl.org/dc/elements/1.1/}creator
{http://purl.org/dc/elements/1.1/}subject
{http://purl.org/dc/terms/}abstract
{http://purl.org/dc/terms/}advisor
{http://purl.org/dc/terms/}referee
{http://purl.org/dc/terms/}dateAccepted
{http://purl.org/dc/elements/1.1/}type
{http://purl.org/dc/terms/}name
{http://purl.org/dc/terms/}dateofbirth
{http://purl.org/dc/elements/1.1/}description
{http://purl.org/dc/terms/}grantor
'''
# věci komplet špatně vyplněné či jinak nehodnotné
dcSkipped = '''
{http://purl.org/dc/elements/1.1/}identifier
{http://purl.org/dc/elements/1.1/}rights
{http://purl.org/dc/elements/1.1/}collection
{http://purl.org/dc/elements/1.1/}studyID
{http://purl.org/dc/elements/1.1/}status
{http://purl.org/dc/elements/1.1/}publisher
'''
# created má občas /
# medium&formát zkontrolovat podle příloh
# level a discipline potřebuje učesat a i s type zkontrolovat
dcTODO = '''
{http://purl.org/dc/terms/}created
{http://purl.org/dc/terms/}medium
{http://purl.org/dc/elements/1.1/}format
{http://purl.org/dc/terms/}level
{http://purl.org/dc/terms/}discipline
'''
def convertDC(oai_id, categorize, metadata1):
    metadata = {}
    for tag, value in metadata1:
        if value != None:
            metadata.setdefault(tag,[]).append(value)
    ret = {}
    
    for tag, value in metadata1:
        if value and '\xa0' in value:
            categorize.categorize_item(oai_id, "Kodování")
    
    if metadata == {}:
        categorize.categorize_item(oai_id, "No metadata")
        return
    
    tag = '{http://purl.org/dc/elements/1.1/}title'
    if not tag in metadata.keys():
        categorize.categorize_item(oai_id, "No title") 
        return
    assert len(metadata[tag]) == 1
    if 'Plán' in metadata[tag][0]:
        categorize.categorize_item(oai_id, "Mapa nikoliv kvalifikační práce") 
        return
    if metadata[tag][0] in ['článek','AVU','Test LDAP', 'Test LDAP Htf', 'Test LDAP TF', 'Testovaci Acess rights', 'nnnnnn', ]:
        categorize.categorize_item(oai_id, "Testovací objekt - smazat.") 
        return
    if 'pdf' in metadata[tag][0]:
        categorize.categorize_item(oai_id, "Přílohy s metadataty.") 
        return
    
    tag = '{http://purl.org/dc/terms/}abstract'
    if tag in metadata.keys() and metadata[tag] == ['abstract']:
        #tohle všechno jsou nesmysly nebo špatně zařazené věci
        categorize.categorize_item(oai_id, "Abstract is 'abstract'") 
        return
    
    tag = "{http://purl.org/dc/elements/1.1/}language" 
    if not tag in metadata.keys():
        categorize.categorize_item(oai_id, "unknown language")
        return
    assert len(metadata[tag]) == 1
  
    # jazkyk v tagu a jazyk titulku letmým pohledem sedí - HURÁ
    #print(metadata[tag][0],metadata['{http://purl.org/dc/elements/1.1/}title'])
    

    tag = '{http://purl.org/dc/elements/1.1/}type'
    tag2 = '{http://purl.org/dc/terms/}name'
    if not tag in metadata.keys():
        if tag2 in metadata.keys():
            if metadata[tag2][0] == 'Mgr.':
                metadata[tag] = 'diplomová práce'
        categorize.categorize_item(oai_id, "unknown type of work")
        return
    assert len(metadata[tag]) == 1
    if metadata[tag][0] in ['bakalářksá práce']:
        metadata[tag][0] = 'bakalářská práce'
    if metadata[tag][0] in ['magisterská práce','diplomové práce','diplomová príce']:
        metadata[tag][0] = 'diplomová práce'
    if metadata[tag][0] in ['doktorská práce','disertační práce']:
        metadata[tag][0] = 'dizertační práce'
    if metadata[tag][0] == 'článek':
        categorize.categorize_item(oai_id, "článek není závěrečná práce")
        return
    if not metadata[tag][0] in ['bakalářská práce','diplomová práce', 'dizertační práce', 'rigorózní práce']:
        categorize.categorize_item(oai_id, "unknown type of work")
        return
    
        #print(metadata)
        #print(metadata[tag])


    tag = '{http://purl.org/dc/terms/}grantor'
    if tag in metadata.keys():
        assert len(metadata[tag]) == 1
        origin = metadata[tag][0]
        r = commonTag.convertOrigin(origin, oai_id, categorize)
    
    for tag in metadata.keys():
        if not tag in (dcParsed + dcTODO +  dcSkipped).split('\n'):
            raise Exception("Unknown tag {}.".format(tag))

