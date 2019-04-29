import json

def darTags(tags):
    retorno = []
    jsonC = ''
    with open('data.json', 'r', encoding="utf8") as f:
        jsonC = json.load(f)
    for x in tags:
        for c in jsonC['tags']:
            if(str(x)==str(c['id'])):
                retorno.append(c['name'])
    return retorno

def darPorTag(tag):
    retorno = []
    jsonC = ''
    with open('data.json', 'r', encoding="utf8") as f:
        jsonC = json.load(f)
        for c in jsonC['stores']:
            for x in c['tags']:
                if(str(x)==str(tag)):
                    retorno.append(c)
    return retorno
        
