# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def to_be_or_not_to_be(sentence):
    res = []
    words = sentence.split()
    sub = []
    def visit(i):
      if i == len(words):
        res.append(" ".join(sub[:]))
        return
      sub.append(words[i])
      visit(i + 1)
      sub.pop()
      visit(i + 1)
    visit(0)
    return res

      
