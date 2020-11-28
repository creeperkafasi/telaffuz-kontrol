def match_percent(str1=str(),str2=str()):
    """
    match_percent(first string, second string)\n
    Comares 2 strings and returns the percentage of matching letters.\n
    If the string lenghts are different, whitespace will be added at the end of the short string
    """

    if len(str1)==0:
        str1=" "
    if len(str1) > len(str2):
        str2 = str2 + " "*(len(str1)-len(str2))
    elif len(str2) > len(str1):
        str1 = str1 + " "*(len(str2)-len(str1))
    
    per = 0
    for i in range(len(str1)):
        per += int(str1[i] == str2[i])
    
    return (per/len(str1))

def check_match(str1=str(),str2=str()):
    """
    check_match(first string, second string)\n
    Checks the second string to the first one,
    returns a list of mismatched indexes and 
    prints both strings highlighting the errors in the second string with red color.\n
    If the string lenghts are different, whitespace will be added at the end of the short string\n
    """
    import colorama
    colorama.init()

    if len(str1)==0:
        str1=" "
    if len(str1) > len(str2):
        str2 = str2 + " "*(len(str1)-len(str2))
    elif len(str2) > len(str1):
        str1 = str1 + " "*(len(str2)-len(str1))

    wrong_indexes = []
    hlstr2 = ""
    for i in range(len(str1)):
        if str1[i]==str2[i]:
            hlstr2 += str2[i]
        else:
            hlstr2 += colorama.Fore.RED+str2[i]+colorama.Fore.WHITE
            wrong_indexes.append(i)
    print(str1)
    print(hlstr2)
    return wrong_indexes