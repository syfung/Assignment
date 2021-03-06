"""
# Copyright Nick Cheng, Brian Harrington, Danny Heap, 2013, 2014, 2015,
# Joshua Fung, 2015.
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSC148, Winter 2015
#                       
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

# Do not change this import statement, or add any of your own!
from regextree import RegexTree, StarTree, DotTree, BarTree, Leaf

# Do not change anything above this comment except for the copyright
# statement

# Student code below this comment.
"""
# This module include four module-level function, designed to work
# with the RegexTree class for the regextree module.
#
# Include:is_regex(str), all_regex_permutations(str),
# regex_mathc(RegexTree, str), and build_regex_tree(str).
"""

class InvalidCharError(Exception):
    """Raise when nontain non regex char"""


class InvalidRegexError(Exception):
    """Raise when the expected regex is not a regex"""
    
    
def is_regex(s):
    """(str) -> bool

    Return True if the input string is a valid regular expression,
    False otherwise.

    >>> is_regex('(2|e)')
    True
    >>> is_regex('2.e')
    False
    """
    if(len(s) < 1):
        return False
        
    # The base case
    # Single char with 0, 1, 2, e
    if(len(s) == 1):
        if(s[0] == '0' or s[0] == '1' or s[0] == '2' or s[0] == 'e'):
            return True

    # Anything more than one char
    else:
        # If it is followed by a star it is always a valid regex with
        # out that star
        if(s[-1] == "*"):
            return is_regex(s[:-1])

        # If is is enclosed in a parenthesis, it should at least have
        # one . or | seperate. Extra . or | will cause the spliting
        # have . or | in r1 or r2. If they are encolsed in extra
        # parenthese they are consided in different level, will be
        # ingored 
        if(s[0] == "(" and s[-1] == ")"):
            # Base level
            per_level = 0
            split_index = 0
            
            # Looping all char, can be done with recursion but really
            # doesn't change anything 
            for i,c in enumerate(s[1:-1]):

                # Different level
                if(c[0] == "("):
                    per_level += 1
                elif(c[0] == ")"):
                    per_level -= 1

                # Split point
                if(per_level == 0 and (c[0] == "." or c[0] == "|")):
                    split_index = i
                    # There is no need to continue
                    break

            # Split into r1 and r2
            r1 = s[1:split_index + 1]
            r2 = s[split_index + 2:-1]

            # Has to be both true to be true
            return (is_regex(r1) and is_regex(r2))
        
    # Anything that is longer than 1, but not trailing star or
    # enclosed in parenthesis is not a regex 
    return False


def all_regex_permutations(s, index=0, is_first=True):
    """(str) -> set of str

    Return a set of permutations of s that are valid regex

    Will raise InvalidCharError when the string contain non-regex
    charters, I have chossen to raise an error when the given string
    contain a invalid charter is this provide more info to the user
    than not telling them why there is no possible form regex. Because
    this suggess they don't know what a regex is. Also I keep on pass
    non-regex char to it and have no idea why it return empty.

    At the same time, when the provided string only contain valid
    charter but impossible to form a regex (like "((((") the function
    will return a empty set, rather than rasing an error. Since user
    might want to use the function to check if the string form a
    regex.

    I can think of two approch to write this function, one is to
    generate all possible permutation then add the regex one to the
    set

    Or only generate basic regex string then build on that

    >>> all_regex_permutations('()2|e')
    {'(2|e)', '(e|2)'}
    >>> all_regex_permutations("(())02e||")
    {'(e|(2|0))', '((2|0)|e)', '((e|2)|0)', '((0|2)|e)', '(2|(0|e))',
    '(0|(e|2))', '((0|e)|2)', '(0|(2|e))', '((2|e)|0)', '(e|(0|2))',
    '((e|0)|2)', '(2|(e|0))'} 
    >>> all_regex_permutations("3df")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "./regex_functions.py", line 65, in all_regex_permutations
      raise InvalidCharError("Contains invalid regex character")
    regex_functions.InvalidCharError: Contains invalid regex character
    """
    # Lets do the easy version for now (super slow...)

    # Checking for invalid char, this is not the best way to do it,
    # since it is looping the string a extra time
    # but for now it will do.
    if(is_first):
        for c in s:
            # Check if the char at index is a valid char, doing it
            # this way is not ideal since it is checking repeatingly
            if(not(c[0] == "0" or c[0] == "1" or c[0] == "2" or
                   c[0] == "e" or c[0] == "*" or c[0] == "." or
                   c[0] == "|" or c[0] == '(' or c[0] == ")")):
                raise InvalidCharError("Contain invalid char")
            
    # Init the empty set
    regex = set()

    # Using the is_regex to check if it is a regex
    if(is_regex(s)):
        # If yes add it to the set
        regex.add(s)

    # Convert string s to a list of char
    c = list(s)

    # Loop through all the index, when index == len(c) it will pass
    # the loop
    for i in range(index, len(c)):

        # Swapping position
        temp = c[index]
        c[index] = c[i]
        c[i] = temp

        # Call recursively to swap all char
        regex.update(all_regex_permutations(''.join(c), index + 1,
                                            False))
                
    return regex


def regex_match(root, match_string):
    """(RegexTree, str) -> bool

    Return true if the string match the regex contained in the tree
    rooted r.
    
    We assume that the tree rooted in r respect the tree hierarchy,
    like like internal nodes. Shouh as StarTree, DotTree, BarTree and
    Leaf.

    It is hard to decide should the function raise a exception if the
    string contain a invalid char, since trying to match a string
    sugess the user don't know how a regex work. But at the same time
    users might use it in function that might generate string that
    have invalid char, but only want the function return false rater
    than rasing an exception.

    The decision is it will not raise an exception

    >>> regex_match(r, "22222")
    True
    >>> regex_mathc(r, "0222")
    False
    >>> regrex_match(r, "ha")
    False
    """
    if(type(root) is Leaf):
        if(len(match_string) == 0 and root.get_symbol() == "e"):
            return True
        
        elif(len(match_string) == 1 and match_string[0] == root.get_symbol()):
            return True
        else:
            return False

    elif(type(root) is StarTree):
        if(match_string == ""):
            return True
        
        else:
            num_char = len(match_string)
            for i in range(1, num_char + 1):
                if(num_char % i == 0):
                    unit_string = match_string[0:i]
                    num_unit = num_char // i
                    # When the unit len == string len it will always
                    # equal, passing the original match_string into
                    # the regex_match with the child()
                    if((unit_string * num_unit) == match_string):
                        return regex_match(root.get_child(), unit_string)
                    else:
                        pass
        
    elif(type(root) is DotTree):
        root_1 = root.get_left_child()
        root_2 = root.get_right_child()

        # I can't think of a better way to do it, let just spliting
        # all possible until it find a working combination or try
        # everything
        for i in range(0, len(match_string) + 1):
            string_1 = match_string[:i]
            string_2 = match_string[i:]
            print(string_1, string_2)
            if(regex_match(root_1, string_1) and
               regex_match(root_2, string_2)):
                return True

        return False
        
    elif(type(root) is BarTree):
        root_1 = root.get_left_child()
        root_2 = root.get_right_child()

        return (regex_match(root_1, match_string) or
                regex_match(root_2, match_string))

    else:
        return False
            
    
def build_regex_tree(regex):
    """(str) -> RegexTree

    Return a RegexTree root node of the regex express as a tree

    >>> build_regex_tree("2*")
    <regex_functions.RegexTree>
    >>> build_regex_tree("ha")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "./regex_functions.py", line 65, in all_regex_permutations
      raise InvalidRegexError("Not a Regex")
    regex_functions.InvalidRegexError: Not a Regex
    """
    # It make sences to do this with recursion, since each sub-r is a
    # tree
    if(len(regex) < 1):
        raise InvalidRegexError("Not a Regex")
    
    if(len(regex) == 1):
        if(regex[0] == "0" or regex[0] == "1" or regex[0] == "2" or
           regex[0] == "e"):
            return Leaf(regex[0])
        else:
            raise InvalidRegexError("Not a Regex")
        
    if(regex[-1] == '*'):
        return StarTree(build_regex_tree(regex[:-1]))

    # If is is enclosed in a parenthesis, it should at least have
    # one . or | seperate. Extra . or | will cause the spliting
    # have . or | in r1 or r2. If they are encolsed in extra
    # parenthese they are consided in different level, will be
    # ingored 
    if(regex[0] == "(" and regex [-1] == ")"):
        # Base level
        per_level = 0
        split_index = 0
            
        # Looping all char, can be done with recursion but really
        # doesn't change anything 
        for i,c in enumerate(regex[1:-1]):

            # Different level
            if(c[0] == "("):
                per_level += 1
            elif(c[0] == ")"):
                per_level -= 1

            # Split point
            if(per_level == 0 and (c[0] == "." or c[0] == "|")):
                split_index = i
                split_symbol = c[0]
                # There is no need to continue
                break

        # Split into r1 and r2
        r1 = regex[1:split_index + 1]
        r2 = regex[split_index + 2:-1]

        # Has to be both true to be true
        if(split_symbol[0] == '.'):
            return DotTree(build_regex_tree(r1), build_regex_tree(r2))
        elif(split_symbol[0] == '|'):
            return BarTree(build_regex_tree(r1), build_regex_tree(r2))

    raise InvalidRegexError("Not a Regex")
