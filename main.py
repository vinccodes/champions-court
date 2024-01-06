import random

players_list = []

###
# Given a list of players .txt file parse the text file into a python list of players
###
def generate_players_list():

    # open the file containing list of players player-list.txt
    with open('player-list.txt', 'r') as f:
        # read the file one line at a time

        skill_level = ['A', 'B', 'C]']

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


def main():
    generate_players_list()
    print(players_list)
    
    check_player_entries(players_list, 5)


if __name__ == "__main__":
    main()


