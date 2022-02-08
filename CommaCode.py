# Write your code here :-)
def listModifier(listToModify):
    newString = ''
    for i in range(len(listToModify)-1):

        newString += listToModify[i] +', '

        if i == len(listToModify)- 2:
            newString += 'and '
    newString += listToModify[-1]
    return newString
spam = ['One', 'Two', 'Three', 'Four', 'Five']
print(listModifier(spam))
