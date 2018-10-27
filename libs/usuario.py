def create_user(cid):
    file_name = str(cid) + ".json"
    dict = {"ID": cid, "parrafo_counter": 0}
    with open(file_name, "w") as jsonfile:
        json.dump(dict, jsonfile)

def getparrafo(cid):
    file_name = str(cid) + ".json"
    with open(file_name, "rw") as jsonfile:
        user_dct = json.load(jsonfile)
        return user_dct["parrafo_counter"]

def setparrafo(cid, parrafo):
    file_name = str(cid) + ".json"
    with open(file_name, "rw") as jsonfile:
        user_dct = json.load(jsonfile)
        user_dct["parrafo_counter"] = parrafo

        json.dump(user_dct, jsonfile)
