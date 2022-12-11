players_list = {}
while True:
    command = input()
    if command == 'Season end': break
    if '->' in command:
        player, position, skill = command.split(' -> ')
        if player not in players_list.keys():
            players_list[player] = {}
        if position not in players_list[player]:
            players_list[player][position] = 0
        if players_list[player][position] < int(skill):
            players_list[player][position] = int(skill)
    elif ' vs ' in command:
        player1, player2 = command.split(' vs ')
        if (player1 and player2) in players_list:
            for pos1 in players_list[player1]:
                if pos1 in players_list[player2]:
                    total_skills_player1 = sum(players_list[player1].values())
                    total_skills_player2 = sum(players_list[player2].values())
                    if total_skills_player1 > total_skills_player2:
                        players_list.pop(player2)
                    elif total_skills_player1 < total_skills_player2:
                        players_list.pop(player1)
players_by_skills_name = []
for player in players_list.keys():
    players_by_skills_name.append({"name": player, "total_skills": sum(players_list[player].values())})
sorted_result = sorted(players_by_skills_name, key=lambda x: (-x["total_skills"], x["name"]))
for item in sorted_result:
    print(f"{item['name']}: {item['total_skills']} skill")
    for pos, skill in sorted(players_list[item['name']].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {pos} <::> {skill}")



