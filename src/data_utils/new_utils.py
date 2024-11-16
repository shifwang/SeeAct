
from data_utils.format_prompt_utils import get_index_from_option_name

class Node:
    def __init__(self, url="", parent=None, children=[], alternatives=[]):
        self.url = url
        self.parent = parent
        self.children = children
        self.alternatives = alternatives  # alternative actions
    def __repr__(self):
        return f"Node(url={self.url}, parent={self.parent}, children={self.children}, alternatives={self.alternatives})"

def process_new_action(element, action, value, elements, n_total_elements, choices):
    new_action = ""
    if len(element) in [1, 2]:
        element_id = get_index_from_option_name(element)
    else:
        element_id = -1
 
    if (0 <= element_id < n_total_elements and action.strip() in ["CLICK", "SELECT", "TYPE",
                                                                         "PRESS ENTER", "HOVER",
                                                                         "TERMINATE"]):
        target_element = elements[int(choices[element_id][0])]
        target_element_text = choices[element_id][1]
        target_action = action
        target_value = value
        new_action += "[" + target_element[2] + "]" + " "
        new_action += target_element[1] + " -> " + target_action
        if target_action.strip() in ["SELECT", "TYPE"]:
            new_action += ": " + target_value
        got_one_answer = True
    elif action.strip() in ["PRESS ENTER", "TERMINATE"]:
        target_element = action
        target_element_text = target_element
        target_action = action
        target_value = value
        new_action += target_action
        if target_action.strip() in ["SELECT", "TYPE"]:
            new_action += ": " + target_value
        got_one_answer = True
    else:
        got_one_answer = False
        target_element = None
        target_element_text = None
        target_action = None
        target_value = None
        new_action = None
    return got_one_answer, target_element, target_element_text, target_action, target_value, new_action

