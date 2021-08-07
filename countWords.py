def countWordsFromFile():
    fileName=input("Enter the file name: ")
    file=open(fileName,"r")

    numberOfWords=0

    for line in file:
        words=line.split()
        numberOfWords=numberOfWords+len(words)
    
    print("The number of words in the file are: ")
    print(numberOfWords)

countWordsFromFile()
