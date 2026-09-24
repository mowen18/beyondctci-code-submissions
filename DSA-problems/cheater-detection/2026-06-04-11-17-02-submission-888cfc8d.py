# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def suspect_students(answers, m, students):
  def same_row(s1, s2):
    return ((s1 - 1) // m) == ((s2-1) // m)

  dic = {}
  deskstud = {}
  for student in students:
    if student[2] == answers:
      continue
    dic[student[1]] = student[2]
    deskstud[student[1]] = student[0]
  
  res = []
  if len(dic) == 0:
    return res
  for stud, desk, ans in students:
    if desk + 1 in dic and dic[desk] == dic[desk + 1] and same_row(desk, desk+1):
      res.append([deskstud[desk], deskstud[desk+1]])
  return res



