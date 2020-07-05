letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letter:point for letter, point in zip(letters, points)} #assigns each letter to a score and stores it in dictionary

letter_to_points.update({" ":0}) #adds blank tile to dictionary and assigns 0 points to it

#print(letter_to_points)

def score_word(word): #turns string into uppercase, adds up points of word given
  point_total = 0
  for each_letter in word:
    upper_case = each_letter.upper()
    if upper_case in letters:
      value = letter_to_points.get(upper_case)
      point_total += value
    else:
      point_total += 0
  return point_total

#print(score_word("Cirill")) <-- expects 8

brownie_points = score_word("BROWNIE")
#print(brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd":["EARTH","EYES","MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
#that's a dictionary of a player and the list words they make


def update_point_totals(words_and_players): #running dictionary of the players with their points so far
  player_to_points = {}
  for player, words in words_and_players.items():
    player_points = 0
    for word in words:
      player_score = score_word(word)
      player_points += player_score
    player_to_points.update({player:player_points})
  return player_to_points

print(update_point_totals(player_to_words))

words_used = {} 
def play_word(player, word): #makes a running dictionary of a player and the list of words they've already used
  if player not in words_used:
    words_used.update({player:[word]})
  elif word not in words_used[player]:
    list_of_words = words_used[player]
    list_of_words.append(word)
  elif word in words_used[player]:
    print("You already used that!")
  return words_used

#test runs
print(play_word("Ciri", "CRY"))
print(play_word("Ciri", "DEED"))
print(play_word("Flo", "CONE"))
print(play_word("Flo", "CONE"))
