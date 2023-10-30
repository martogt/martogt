def team_lineup(*players_data):
    player_info = {}

    for player, country in players_data:
        if country in player_info:
            player_info[country].append(player)
        else:
            player_info[country] = [player]

    sorted_data = sorted(player_info.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []
    for country, players in sorted_data:
        result.append(f"{country}:")
        for player in sorted(players):
            result.append(f"-{player}")

    return "\n".join(result)


print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany"),
    ("Bruno Fernandes", "Portugal"),
    ("Bernardo Silva", "Portugal"),
    ("Harry Maguire", "England")))
