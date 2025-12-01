import re # re = regular expression, which is a built-in module in Python for working with regular expressions

import re

pattern = r"was" # r indicates a raw string, which tells Python to interpret backslashes literally
text = '''
Cyclone Dumazile was a strong tropical cyclone in the South-West Indian Ocean that affected Madagascar and Réunion in early March 2018. Dumazile originated from a cyclone Dyclone low-pressure area that formed near Agaléga on 27 February. It became a tropical disturbance on 2 March, and was named the next day after attaining tropical storm status. Dumazile reached its peak intensity on 5 March, with 10-minute sustained winds of 165 km/h (105 mph), 1-minute sustained winds of 205 km/h (125 mph), and a central atmospheric pressure of 945 hPa (27.91 inHg). As it tracked southeastwards, Dumazile 

'''

# this method returns a match object if the pattern is found in the text, otherwise it returns None
# match = re.search(pattern, text)
# print(match) 

# this method returns all non-overlapping matches of the pattern in the text as a list of strings
match = re.finditer(pattern, text)
for m in match:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])


'''

Use this link ot learn more about regular expressions in Python: 
https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions

''' 