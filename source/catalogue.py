levelToTitle = {
    "Bakalářská práce": [ "Bc.", ],
    "Diplomová práce": [ "Mgr.", "MUDr." ],
    "Rigorózní práce": [ "PhDr.", 'ThLic.', 'JUDr.', 'RNDr.', 'PharmDr.', 'MUDr.', "ThDr.", ],
    "Dizertační práce": [ 'ThD.','Th.D.', "PhD.", 'Ph.D.' ],
    "Habilitační práce": [ "Doc.", ],
    }
categoryToTypeTitle = {
    "bakalářské práce": "bakalářská práce",
    "diplomové práce": "diplomová práce",
    "rigorózní práce": "rigorózní práce",
    "dizertační práce": "dizertační práce",
    "habilitační práce": "habilitační práce",
    }
    
convertLang = {
    'cze': 'cs_CZ',
    'slo': 'sk_SK',
    'fre': 'fr_FR',
    'eng': 'en_US',
    'ger': 'de_DE',
    'pol': 'pl_PL',
    'spa': 'es_ES',
    'ita': 'it_IT',
    }

langText = {
    'cs_CZ': 'čeština',    
    'sk_SK': 'slovenština',    
    'fr_FR': 'francouština',    
    'en_US': 'angličtina',    
    'de_DE': 'němčina',    
    'pl_PL': 'polština',    
    'es_ES': 'španělština',    
    'it_IT': 'italština',    
    }


institutToFaculty = {
    'Institut politologických studií': 'Fakulta sociálních věd', 
    'Institut sociologických studií': 'Fakulta sociálních věd',
    'Institut mezinárodních studií': 'Fakulta sociálních věd',
    'Institut ekonomických studií': 'Fakulta sociálních věd',
    }

faculty = {
    'Filozofická fakulta': [
        'Katedra andragogiky',
        'Katedra pomocných věd historických a archivního studia',
        'Ústav etnologie',
        'Ústav románských studií',
        'Katedra historie',
        'Katedra obecné a pedagogické psychologie',
        'Knihovna andragogiky a kulturologie',
        'Katedra sociální práce a vzdělávání dospělých',
        'Katedra andragogiky a sociální práce',
        'Katedra anglistiky, germanistiky a nordistiky',
        'Katedra andragogiky a personálního řízení',
        'Katedra české literatury a literární vědy',
        'Katedra marxisticko-leninské filosofie',
        'Katedra marxisticko-leninské filozofie',
        'Katedra marxisticko-leninskej filozofie',
        'Katedra marxisticko-leninské sociologie',
        'Katedra pedagogiky',
        'Katedra psychofyziologie a klinické psychologie',
        'Katedra psychologie',
        'Katedra sociologie',
        'Katedra sociologie a filozofie',
        'Katedra sociologie a filosofie',
        'Katedra sociální práce',
        'Katedra tělesné výchovy a sportu',
        'Katedra ekonomie',
        'Katedra teorie kultury',
        'Katedra žurnalistiky',
        'Katedra věd o zemích Asie a Afriky',
        'Katedra výchovy a vzdělávání dospělých',
        'Ústav filozofie a religionistiky',
        'Ústav informačních studií a knihovnictví',
        'Katedra psychologie práce a řízení',
        'Katedra klinické psychologie',
        'Katedra hospodářských a sociálních dějin',
        'Katedra psychologie (1951-1975)',
        'Katedra sociologie (1966-1971)',
        'Katedra sociální psychologie',
        ],
    'Filozoficko-historická fakulta': [ 'Psychologický seminář', ],
    'Fakulta sociálních věd a publicistiky': [ 'Katedra osvěty a výchovy dospělých', ],
    'Fakulta sociálních věd': [
        'Institut politologických studií',
        'Institut sociologických studií',
        'Institut sociologických studií. Katedra sociologie',
        'Institut mezinárodních studií',
        'Institut mezinárodních studií. Katedra západoevropských studií',
        'Institut ekonomických studií',
        'Institut komunikačních studií a žurnalistiky',
        'Institut komunikačních studií a žurnalistiky. Katedra žurnalistiky',
        'Institut komunikačních studií a žurnalistiky. Katedra mediálních studií',
        'Katedra mediálních studií',
        'Katedra veřejné a sociální politiky',
        'Katedra západoevropských studií',
        'Katedra politologie',
        'Katedra amerických studií',
        'Katedra německých a rakouských studií',
        'Katedra mezinárodních vztahů',
        'Katedra sociologie', 
        'Katedra sociologie (1966-1971)',
        ],
    'Pedagogická fakulta': [ 
        'Katedra speciální pedagogiky', 
        'Katedra výtvarné výchovy', 
        'Katedra pedagogické a školní psychologie',
        'Katedra pedagogické psychologie',
        'Katedra psychologie',
        'Katedra obecné a pedagogické psychologie',
        'Katedra informačních technologií a technické výchovy',
        ],
    'Právnická fakulta': [ 
        'Katedra trestního práva',
        'Katedra obchodního práva',
        'Katedra občanského práva',
        'Katedra pracovního práva a práva sociálního zabezpečení',
        'Katedra teorie práva a právních učení',
        'Ústav práva autorského, práv průmyslových a práva soutěžního',
        'Katedra mezinárodního práva',
        'Katedra finančního práva a financí',
        ],
    'Fakulta humanitních studií': [
        'Katedra elektronické kultury a sémiotiky',
        'Katedra obecné antropologie',
        'Katedra řízení a supervize v sociálních a zdravotnických organizacích', ],
    'Evangelická telogická fakulta': [],
    'Husova evangelická bohoslovecká fakulta': [], 
    'Husova československá evangelická fakulta': [],
    'Husova československá bohoslovecká fakulta': [],
    'Husova československá evangelická fakulta bohoslovecká': [],
    'Husova československá evangelická bohoslovecká fakulta': [],
    'Husitská teologická fakulta': [
        'Katedra filosofie',
        'Katedra církevních dějin',
        'Katedra psychosociálních věd a speciální etiky',
        'Katedra pedagogiky a psychologie',
        'Katedra psychosociálních věd',
        'Katedra religionistiky',
        'Katedra učitelství',
        'Ústav východního křesťanství',
        'Ústav židovských studií',
        ],
    'Komenského evangelická bohoslovecká fakulta': [
        'Katedra biblických věd',
        'Katedra církevních dějin',
        'Katedra biblická',
        ],
    'Komenského bohoslovecká fakulta v Praze': [],
    'Komenského bohoslovecká evangelická fakulta': [],
    'Evangelická teologická fakulta': [ 
            'Katedra filosofie', 'Katedra sociální teologie', 'Katedra Starého zákona', 
            'Katedra systematické teologie', 'Katedra teologické etiky', 'Katedra sociální pedagogiky',
            'Teologie křesťanských tradic',
            'Katedra pastorační a sociální práce',
            'Katedra sociálně pedagogická',
            'Katedra praktické teologie',
            'Katedra Nového zákona',
            'Katedra religionistiky',],
    'Matematicko-fyzikální fakulta': [
        'Katedra softwarového inženýrství',
        'Katedra teoretické informatiky a matematické logiky',
        'Kabinet software a výuky informatiky',
        'Ústav formální a aplikované lingvistiky',
        'Katedra geofyziky',
        ],
    '1. lékařská fakulta': ['Ústav patologické fyziologie'],
    '2. lékařská fakulta': [],
    '3. lékařská fakulta': ['Klinika otorinolaryngologická'],
    'Lékařská fakulta, 3.': [],
    'Lékařská fakulta, 2.': [],
    'Lékařská fakulta, 1': ['Ústav patologické fyziologie',],
    }

def getFaculty(department):
    for f in faculty.keys():
        if department in faculty[f]:
            return f

facultyToCollection = {
    '1. lékařská fakulta': 38,
    'Lékařská fakulta, 1': 38, 
    '2. lékařská fakulta': 39, 
    'Lékařská fakulta, 2.': 39,
    '3. lékařská fakulta': 40,
    'Lékařská fakulta, 3.': 40,
    'Evangelická teologická fakulta': 41,
    'Evangelická telogická fakulta': 41, 
    'Komenského evangelická bohoslovecká fakulta': 41, 
    'Komenského bohoslovecká fakulta v Praze': 41,
    'Komenského bohoslovecká evangelická fakulta': 41, 
    'Fakulta humanitních studií': 42,
    'Fakulta sociálních věd': 43,  
    'Fakulta sociálních věd a publicistiky': 43,
    'Filozofická fakulta': 46, 
    'Filozoficko-historická fakulta': 46,
    'Husova evangelická bohoslovecká fakulta': 47, 
    'Husova československá evangelická fakulta': 47,
    'Husova československá bohoslovecká fakulta': 47,
    'Husova československá evangelická fakulta bohoslovecká': 47,
    'Husova československá evangelická bohoslovecká fakulta': 47,
    'Husitská teologická fakulta': 47,
    'Matematicko-fyzikální fakulta': 51, 
    'Pedagogická fakulta': 52, 
    'Právnická fakulta': 54, 
    }
