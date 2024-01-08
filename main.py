import random

players_list = []

###
# Given a list of players .txt file parse the text file into a python list of players
###
def generate_players_list():

    # open the file containing list of players player-list.txt
    with open('player-list.txt', 'r') as f:
        # read the file one line at a time

        skill_level = ['A', 'B', 'C']

        for line in f:
            # create a {} representing each player
            player_name = line.split()
            print(player_name)
    
            players_list.append({"name": player_name[0] + " " + player_name[1],
                                "score": [],
                                "skill_level": skill_level[random.randint(0, 2)]})


###
# Check if the player entry list even, less than equal to maximum number of players
# Return true if passes all conditons
# Return false if fails any conditions
###
def check_player_entries(players_list, available_courts):
    # check the length of the players list
    num_players = len(players_list)
    max_players = available_courts * 4
    print(num_players)
    # conditon 2: check if number of players exceeds available court capacity
    if num_players > max_players:
        print("Number of players exceeds available court capacity.")
        return False
    else:
        print("Number of players is within court capacity")
        return True


###
# Sort the players list by skill level
###
def sort_players_list(players_list):

    for i in range(1,len(players_list)):
        key = players_list[i]

        # move players skill level lower than key to the end of list
        j = i - 1
        while j >= 0 and key["skill_level"] < players_list[j]["skill_level"]:
            players_list[j+1] = players_list[j]
            j -= 1
        players_list[j + 1] = key
    print(players_list)
    


###
# Assign players to courts based on skill level
#  Return a list of courts with the assigned players 
###
def assign_courts(players_list, available_courts):
    pass
    courts_assigned = []
    # iterate for every available court
    for i in range(available_courts):
        # add 4 four players in the court
        pass
        # assign all the level A

        # assign all level B

        # assign all level C

###
# Print out the players_list in human readable format
###
def display_player_list(players_list):

    # iterate player list
    for i in range(len(players_list)):
        print(f"Player No.{str(i+1)} Name: {players_list[i]['name']} -- Skill Level: {players_list[i]['skill_level']}\n")


def main():
    generate_players_list()
    print(players_list)
    
    #check_player_entries(players_list, 5)
    sort_players_list(players_list)
    display_player_list(players_list)

if __name__ == "__main__":
    main()


