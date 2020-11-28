def match_percent(str1=str(),str2=str()):
    """
    match_percent(str1= str, str2= str)\n
    Comares 2 strings and returns the percentage of matching letters.\n
    If the string lenghts are different, whitespace will be added at the end of the short string
    """

    if len(str1)==0:
        str1=" "
    
    if len(str1) > len(str2):
        str2 = str2 + " "*(len(str1)-len(str2))
    elif len(str2) > len(str1):
        str1 = str1 + " "*(len(str2)-len(str1))
    # print(str1+"\nve\n"+str2+"\narasındaki fark hesaplanıyor...")
    per = 0
    for i in range(len(str1)):
        per += int(str1[i] == str2[i])
    
    return (per/len(str1))