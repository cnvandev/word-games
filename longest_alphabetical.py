def init_dictionary(word_file):
  ''' Builds a dictionary list of words from the word file indicated. '''
  dict_words = set()
  for x in open(word_file):
    dict_words.add(x.lower().strip())
  return dict_words


# Actual code goes here!
if __name__=="__main__":
  # We'll determine the shift by figuring out which decoding of the message gives us the longest list of English dictionary words.
  dict_words = init_dictionary("/usr/share/dict/words")

  alphabetical_words = dict();
  max_length = 0
  for word in dict_words:
  	list_word = sorted(word)
  	if list_word == list(word):
  		# Our word is alphabetical! I could find the max-length word here, but I decided to got a bit deeper and bring up a list of all of the words with that length.
  		if len(word) not in alphabetical_words:
  			alphabetical_words[len(word)] = list()
  		
  		alphabetical_words[len(word)].append(word)
  		max_length = max(max_length, len(word))

  print alphabetical_words[max_length]