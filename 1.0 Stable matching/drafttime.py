import sys

firstLine = input()
ab = firstLine.split()  # Number of teams. Number of rounds and number of players
a = int(ab[0])  # Number of teams.
b = int(ab[1])  # Number of rounds
c = int(ab[2])  # Number of players
if a > 0 and b > 0 and c > 0:

    matrix = [['-' for _ in range(c)]
              for _ in range(a)]
    team_to_index = {}
    teammate_to_index = {}
    currentTeam = 0
    # Dictionaries to make translating between letters <-> indices easy.
    isFirst = True
    # Team, Preferences
    for _ in range(int(a)):
        word = input().strip().split()
        if isFirst:
            isFirst = False
            for i in range(len(word)):
                if i == 0:
                    team_to_index[word[0]] = currentTeam
                    currentTeam += 1
                else:
                    proposer = word[i]
                    teammate_to_index[proposer] = i - 1
                    team, teammate = team_to_index[word[0]], teammate_to_index[proposer]
                    matrix[int(team)][int(teammate)] = i - 1
        else:
            for i in range(len(word)):
                if i == 0:
                    team_to_index[word[0]] = currentTeam
                    currentTeam += 1
                else:
                    proposer = word[i]
                    team, teammate = team_to_index[word[0]], teammate_to_index[proposer]
                    matrix[int(team)][int(teammate)] = i - 1

    proposer_preference_original = {}
        # Team, Preferences
    try:
        for _ in range(int(c)):
            wqa = input().strip()
            wordas = wqa.split()  # Number of teams. Number of rounds and number of players
            first_half = wordas[:1]
            second_half = wordas[1:]
            name = first_half[0]
            proposer_preference_original[name] = second_half

        proposer_preference = {key: value[:] for key, value in proposer_preference_original.items()}
        no_team_man = list(teammate_to_index.keys())
        man_fiance = dict.fromkeys(teammate_to_index.keys(), None)
        team_current = dict.fromkeys(team_to_index.keys(), None)
        for key in team_current:
            team_current[key] = []
        next_proposals = dict.fromkeys(teammate_to_index.keys(), 0)
        while no_team_man:
            isInserted = False
            man = no_team_man[0]
            his_preferences = proposer_preference[man]
            if not his_preferences:
                no_team_man.remove(man)
            else:
                favTeam = his_preferences.pop(0)
                next_proposals[man] += 1
                teamsList = team_current[favTeam]
                if man_fiance[man] is None:
                    teamIndex, challangerIndex = team_to_index[favTeam], teammate_to_index[man]
                    for i in range(len(teamsList)):
                        currentIndex = teammate_to_index[teamsList[i]]
        
                        if matrix[teamIndex][challangerIndex] < matrix[teamIndex][currentIndex]:
                            teamsList.insert(i, man)
                            if len(teamsList) > b:
                                thrownOutTeammate = team_current[favTeam].pop()
                                no_team_man.append(thrownOutTeammate)
                                man_fiance[thrownOutTeammate] = None
                            man_fiance[man] = favTeam
                            no_team_man.remove(man)
                            isInserted = True
                            break
                    if len(teamsList) != b and isInserted == False:
                        teamsList.append(man)
                        man_fiance[man] = favTeam
                        try:
                            no_team_man.remove(man)
                        except ValueError:
                            pass
                        except:
                            raise NameError("This is an argument")
        sortedList = team_current
        # check if happy draft.
        isHappyDraft = True
        
        if isHappyDraft:
            result = ""
            for key in sortedList:
                arrayListas = sortedList[key]
                s = ' '.join(arrayListas)
                result = key + " " + s
                print(result)
        else:
            print("Hello darkness my old friend!")
    except NameError:
        sys.exit(1)
    except:
        print("result is")
else:
    print("Hello darkness my old friend!")
