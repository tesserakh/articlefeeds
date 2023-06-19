import os


def create_filename(key, prefix=None, sep="-"):
    if isinstance(key, dict):
        if key.get("publication"):
            naming = key.get("publication")
        else:
            naming = key.get("tag")
    elif isinstance(key, str):
        naming = key
    else:
        print("Key must be dict or str")
        return
    naming = naming.lower().replace(" ", sep)
    if prefix is None:
        return "{}.json".format(naming)
    else:
        return "{}{}{}.json".format(prefix, sep, naming)


def create_storage_path(filename, path="feeds"):
    if path is not None:
        datapath = os.path.join(os.getcwd(), path)
    else:
        datapath = ""
    if not os.path.exists(datapath):
        os.makedirs(datapath)
    return os.path.join(datapath, filename)
