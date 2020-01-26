def get_several_values_at_ones():
    """
    Get several values from a dictionary by several keys at once

    uuid: '75a01a55-b582-4596-8aa1-0c298609e8f2'
    """

    some_dict = {"Russia": "Moscow",
                 "France": "Paris",
                 "Germany": "Berlin"}

    return [some_dict.get(key) for key in ("Russia", "France", "Germany", "USA")]

# get_several_values_at_ones()