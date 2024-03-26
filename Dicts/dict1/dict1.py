


def create_dict_from_lists(keys, values):
    """
    This function returns a dict made from two lists.
    """
    return dict(zip(keys, values))

def merge_two_dicts(d1, d2):
    """
    Merge two Python dictionaries into one
    """
    #pass  # implement me
    merged_dict = {**d1, **d2}
    return merged_dict

def init_dict_with_values(lst, d1):
    """
    Create a dict with default values for each key listed.

    """
    return dict.fromkeys(lst, d1)

def extract_keys_to_dict(datadict, keylist):
    """
    Create a dictionary by extracting the keylist from a given dictionary
    """
    #
    result = dict((k, datadict[k]) for k in keylist
                  if k in datadict)
    return result

def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    del(datadict, keylist)

def check_dict_for_key(datadict, key) -> bool:
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    if key in datadict:
        return True
    else:
        return False

def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    return min(ddd)

def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    return max(ddd, key=ddd.get)
