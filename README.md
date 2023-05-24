# openai_project

1. Prepare JSONL training data.
   - run `data_generator.py` to transfer xml to json files
   - run `myjsontransfer.py` to combine all the json file into a single one, `sample.json` will be created 
   - run command `openai tools fine_tunes.prepare_data -f ./sample.json` to generate the JSONL file

2. Train a costomzied modle based on the above geretared JSONL file.