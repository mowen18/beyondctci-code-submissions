# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def hangman_candidates_count(valid_words, pattern, incorrect_guesses):
  bad_letters = set(incorrect_guesses)
  num_valid = 0

  for word in valid_words:

    if len(word) != len(pattern):
      continue
    
    match_word = True
    for i in range(len(pattern)):
      if pattern[i] != '_':
        if word[i] != pattern[i]: 
          match_word = False
          break
      elif word[i] in bad_letters: 
        match_word = False
        break
    if match_word == True:
      num_valid += 1
  return num_valid
