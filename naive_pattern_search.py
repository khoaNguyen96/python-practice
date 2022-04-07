def pattern_search(text, pattern,replacement, case_sensitive=True):
  fixed_text = ""
  num_skips = 0
  for index in range(len(text)):
    match_count = 0
    for char in range(len(pattern)): 
    # Checking the text has to be exact same as the pattern
      if case_sensitive and pattern[char] == text[index + char]:
        match_count += 1
        # Count how many times need to skipped the loop
        num_skips += 1
    # To check on cases that uppercase and lowercase charector can be identify as the same
      elif not case_sensitive and pattern[char].lower() == text[index + char].lower(): 
        match_count += 1
        num_skips += 11
      else:
        break
   
    # Find the pattern 
    if match_count == len(pattern):
      print(pattern, "found at index", index)
    # Change the pattern with the replacement
      fixed_text += replacement
    # Skipping the loop as many charactor as the pattern has
    if num_skips > 0:
      num_skips -= 1
      continue
    # Ortherwise adding the original text to the fixed text
    else:
      fixed_text += text[index]
  return fixed_text
