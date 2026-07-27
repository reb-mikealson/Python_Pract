def analyzeURL(string):
    urlLen = len(string)
    dotCount = 0
    hyphenCount = 0
    digitCount = 0
    if "https://" in string:
        print("The URL is secure.")
    else:
        print("The URL is not secure.")
    for i in string:
        if i == ".":
            dotCount += 1
        elif i == "-":
            hyphenCount += 1
        elif i.isdigit():
            digitCount += 1
    print("Length of the URL:", urlLen)
    print("Number of dots in the URL:", dotCount)
    print("Number of hyphens in the URL:", hyphenCount)
    print("Number of digits in the URL:", digitCount)
string = input("Enter a URL: ")
analyzeURL(string)