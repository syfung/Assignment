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
    # The base case
    # Single char with 0, 1, 2, e
    if(len(s) == 1):
        if(s[0] == "0" or s[0] == "1" or s[0] == "2" or s[0] == "e"):
            return True
        else:
            return False

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
            return is_regex(r1) and is_regex(r2)

        # Anything that is longer than 1, but not trailing star or
        # enclosed in parenthesis is not a regex 
        return False


def all_regex_permutations(s):
    """(str) -> set of str

    Return a set of permutations of s that are valid regex
    Will raise InvalidCharError when the string contain non-regex
    charters

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
    


def regex_match(r, s):
    """(RegexTree, str) -> bool

    Return true if the string match the regex contained in the tree
    rooted r

    >>> regex_match(r, "2*")
    True
    >>> regex_mathc(r, "(2.2)")
    False
    >>> regrex_match(r, "ha")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "./regex_functions.py", line 65, in all_regex_permutations
      raise InvalidCharError("Contains invalid regex character")
    regex_functions.InvalidRegexError: Not a Regex
    """

    
def build_regex_tree(regex):
    """(str) -> RegexTree

    Return a RegexTree root node of the regex express as a tree

    >>> build_regex_tree("2*")
    <regex_functions.RegexTree>
    >>> build_regex_tree("ha")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "./regex_functions.py", line 65, in all_regex_permutations
      raise InvalidCharError("Contains invalid regex character")
    regex_functions.InvalidRegexError: Not a Regex
    """
