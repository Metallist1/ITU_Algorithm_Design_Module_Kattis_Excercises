import sys

totalAmount = input()
result = []
    # Team, Preferences
valueDict = []

for i in range(int(totalAmount)):
    word = input().strip().split() #[0] start [1] end
    valueDict.append(word)

sortedFinishTimes = sorted(valueDict, key=lambda x: int(x[1]))

while sortedFinishTimes:
    earlierstTime = sortedFinishTimes[0]
    if result:
        lastValue = result[len(result)-1]
        if int(lastValue[1]) <= int(earlierstTime[0]):
            result.append(earlierstTime)
    else:
        result.append(earlierstTime)
    sortedFinishTimes.pop(0)

print(len(result))
