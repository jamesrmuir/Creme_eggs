import pickle

#Saves the game
testVariableZero = 643466436
testVariableOne = 16443466436
testVariableTwo = 265634334436634
testVariableThree = 345456634
testVariableFour = 4643333333333
testVariableFive = "TImeawasof jiosgrhjisgrhiwer"
testVariableSix = ["32323","31321231","21342442142"]
testVariableSeven = 231234
testVariableEight = 335355

with open("savegame.txt", "wb") as f:
    pickle.dump(testVariableZero, f)
    pickle.dump(testVariableOne, f)
    pickle.dump(testVariableTwo, f)
    pickle.dump(testVariableThree, f)
    pickle.dump(testVariableFour, f)
    pickle.dump(testVariableFive, f)
    pickle.dump(testVariableSix, f)
    pickle.dump(testVariableSeven, f)
    pickle.dump(testVariableEight, f)
    
#Loads the game
with open("savegame.txt", "rb") as f:
    variableZero = pickle.load(f)
    variableOne = pickle.load(f)
    variableTwo = pickle.load(f)
    variableThree = pickle.load(f)
    variableFour = pickle.load(f)
    variableFive = pickle.load(f)
    variableSix = pickle.load(f)
    variableSeven = pickle.load(f)
    variableEight = pickle.load(f)


print(variableZero)
print(variableOne)
print(variableTwo)
print(variableThree)
print(variableFour)
print(variableFive)
print(variableSix)
print(variableSeven)
print(variableEight)




