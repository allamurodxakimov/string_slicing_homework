def main(s):
    """
    The s string variable is given. return the characters in the even position.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    return s[0:len(s):2]
print(main("apple"))
print(main("codeschooluz"))