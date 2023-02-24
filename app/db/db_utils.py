def stringify_id(object):
    if '_id' in object:
        object['_id'] = str(object['_id'])
    return object