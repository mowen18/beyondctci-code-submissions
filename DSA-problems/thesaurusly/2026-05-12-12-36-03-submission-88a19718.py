# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def thesaurusly(sentence, synonyms):
    words = sentence.split()
    res = []
    cursent = []
    def visit(i):
      if i == len(words):
        res.append(" ".join(cursent))
        return
      if words[i] in synonyms:
        choices = synonyms.get(words[i], [])
      else:
        choices = [words[i]]
      for wrd in choices:
        cursent.append(wrd)
        visit(i + 1)
        cursent.pop()
    visit(0)
    return res



