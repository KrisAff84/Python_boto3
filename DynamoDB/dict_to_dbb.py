def dict_to_item(raw):
    resp = {}
    for k,v in raw.iteritems():
        if type(v) is str:
            resp[k] = {
                'S': v
            }
        elif type(v) is dict:
            resp[k] = {
                'M': dict_to_item(v)
            }
        elif type(v) is list:
            resp[k] = []
            for i in v:
                resp[k].append(dict_to_item(i))
                    