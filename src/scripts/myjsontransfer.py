import json
import os

# assign directory
directory = '$PATH'
i = 0
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f) and f.endswith(".json"):
        print(f)
        mf = open(f)
        data = json.load(mf)

        title = ""
        try:
            title = data['doc:document']['ja:article']['ja:head']['ce:title']['#text']
        except:
            continue

        abstract = ""
        try:
            if type(data['doc:document']['ja:article']['ja:head']['ce:abstract']) == list:
                for i in data['doc:document']['ja:article']['ja:head']['ce:abstract']:
                    if i['@class'] == 'author' or i['@class'] == 'editor':
                        abstract = i['ce:abstract-sec']['ce:simple-para']['#text']
                        break
            elif type(data['doc:document']['ja:article']['ja:head']['ce:abstract']) == dict:
                if data['doc:document']['ja:article']['ja:head']['ce:abstract']['@class'] == 'author' or data['doc:document']['ja:article']['ja:head']['ce:abstract']['@class'] == 'editor':
                    abstract = data['doc:document']['ja:article']['ja:head']['ce:abstract']['ce:abstract-sec']['ce:simple-para']['#text']
        except:
            continue

        introduction = ""
        try:
            for i in data['doc:document']['ja:article']['ja:body']['ce:sections']['ce:section'][0]['ce:para']:
                introduction = introduction + i.get('#text', '')
        except:
            continue

        highlights = ""
        try:
            for i in data['doc:document']['ja:article']['ja:head']['ce:abstract']:
                if i['@class'] == 'author-highlights':
                    for highlightsElem in i['ce:abstract-sec']['ce:simple-para']['ce:list']['ce:list-item']:
                        if type(highlightsElem['ce:para']) == dict:
                            highlights = highlights + '- ' + highlightsElem['ce:para']['#text'] + '\n'
                        if type(highlightsElem['ce:para']) == list:
                            for j in highlightsElem['ce:para']:
                                highlights = highlights + '- ' + j['#text'] + '\n'
        except:
            continue

        if title and abstract and highlights and introduction:
            dictionary = {
                "prompt": "Please generate a bullet list of highlights using Title and Abstract. Title={title}\nAbstract={abstract}->".format(title=title,abstract=abstract),
                "completion": " {highlights} ".format(highlights=highlights)
            }
            with open("validation.json", "a") as outfile:
                try:
                    json.dump(dictionary, outfile)
                    outfile.write("\n")
                except:
                    continue

        mf.close()
