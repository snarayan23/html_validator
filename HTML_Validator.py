#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html
    validation by checking whether every opening tag has a
    corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    # HINT:
    # use the _extract_tags function below to generate a
    # list of html tags without any extra text;
    # then process these html tags using the balanced
    # parentheses algorithm from the class/book
    # the main difference between your code and the
    # code from class will be that you will have to keep
    # track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags
    stack = []
    if html == '':
        return True
    tags = _extract_tags(html)
    if tags == []:
        return False
    for tag in tags:
        if '/' not in tag:
            stack.append(tag)
        else:
            if len(stack) == 0:
                return False
            if ('/' in tag and stack[-1][1:-1] == tag[2:-1]):
                stack.pop()
            else:
                return False
    return len(stack) == 0


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are
    not meant to be used directly by the user are
    prefixed with an underscore.
    This function returns a list of all the html tags
    contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tag_index = [x for x in range(len(html)) if html[x] in '<>']
    tags = []
    if len(tag_index) % 2 != 0 or len(tag_index) == 0:
        return tags
    for i in range(0, len(tag_index), 2):
        tags.append(html[tag_index[i]: tag_index[i + 1] + 1])
    return tags
