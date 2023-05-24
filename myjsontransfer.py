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

        if type(data['doc:document']['ja:article']['ja:head']['ce:abstract']) == list:
            abstract = data['doc:document']['ja:article']['ja:head']['ce:abstract'][0]['ce:abstract-sec']['ce:simple-para']['#text']
            print(f"abstract: {abstract}")
        elif type(data['doc:document']['ja:article']['ja:head']['ce:abstract']) == dict:
            abstract = data['doc:document']['ja:article']['ja:head']['ce:abstract']['ce:abstract-sec']['ce:simple-para']['#text']
            print(f"abstract: {abstract}")
        introduction = ""
        for i in data['doc:document']['ja:article']['ja:body']['ce:sections']['ce:section'][0]['ce:para']:
            introduction = introduction + i.get('#text', '')
        print(f"introduction: {introduction}")
        highlights = ""
        try:
            for i in data['doc:document']['ja:article']['ja:head']['ce:abstract'][2]['ce:abstract-sec']['ce:simple-para']['ce:list']['ce:list-item']:
                if type(i['ce:para']) == dict:
                    highlights = highlights + i['ce:para']['#text']
                if type(i['ce:para']) == list:
                    for j in i['ce:para']:
                        highlights = highlights + j['#text']
            print(f"highlights: {highlights}")
        except IndexError:
            for i in data['doc:document']['ja:article']['ja:head']['ce:abstract'][1]['ce:abstract-sec']['ce:simple-para']['ce:list']['ce:list-item']:
                if type(i['ce:para']) == dict:
                    highlights = highlights + i['ce:para']['#text']
                if type(i['ce:para']) == list:
                    for j in i['ce:para']:
                        highlights = highlights + j['#text']
            print(f"highlights: {highlights}")

        dictionary = {
            "prompt": "Here is our : {introduction}\n\n###\n\n".format(introduction=introduction),
            "completion": "Here is our highlights: {highlights} END".format(highlights=highlights)
        }
        with open("sample.json", "a") as outfile:
            json.dump(dictionary, outfile)
            outfile.write("\n")

        mf.close()
