import json
import xmltodict
import os

# assign directory
directory = '/Users/shangc/Downloads/hackathon/2352-152X'
i = 0
# iterate over xml files in
# that directory and transfer into json files
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        print(f)
        i = i + 1
        with open(f) as xml_file:
            data_dict = xmltodict.parse(xml_file.read())
            # xml_file.close()

            # generate the object using json.dumps()
            # corresponding to json data

            json_data = json.dumps(data_dict)

            # Write the json data to output
            # json file
            with open(f"{str(i)}.json", "w") as json_file:
                json_file.write(json_data)
                # json_file.close()
