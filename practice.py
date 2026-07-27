def analyzeURL(string):
    urlLen = len(string)
    dotCount = 0
    hyphenCount = 0
    digitCount = 0
    if "https://" in string:
        print("The URL is secure.")
    else:
        print("The URL is not secure.")