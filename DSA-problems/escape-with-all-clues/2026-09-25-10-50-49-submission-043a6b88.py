# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def escape_with_all_clues(room):
  
  def get_clues_pos():
    clues = []
    for i in range(len(room)):
      for j in range(len(room[0])):
        if room[i][j] == 2:
          clues.append((i,j))
    
    return clues
  
  def valid_moves(pos):
    moves = []
    dirs = [(1,0), (0,1), (-1,0),( 0,-1)]
    for r_dir, c_dir in dirs:
      new_r = pos[0] + r_dir
      new_c = pos[1] + c_dir
      if 0 <= new_r < len(room) and 0 <= new_c < len(room[0]) and room[new_r][new_c] != 1:
        moves.append((new_r, new_c))
    return moves

  

  all_clues = set(get_clues_pos())
  shortest_path = []
  current_path = [(0,0)]
  current_visited = {(0,0)}
  current_clues_remaining = set(get_clues_pos())
  if (0,0) in current_clues_remaining:
    current_clues_remaining.remove((0,0))
  
  def visit():

    nonlocal current_path, current_clues_remaining, current_visited, shortest_path
    if shortest_path and len(current_path) >= len(shortest_path):
      return

    if len(current_clues_remaining) == 0:
      if not shortest_path or len(current_path) < len(shortest_path):
        shortest_path = current_path.copy()
      return
    cur_pos = current_path[-1]
    mvs = valid_moves(cur_pos)
    for new_r, new_c in mvs:
      if (new_r, new_c) in current_visited:
        continue
      
      current_path.append((new_r, new_c))
      current_visited.add((new_r, new_c))
      if (new_r, new_c) in all_clues:
        current_clues_remaining.remove((new_r, new_c))
      
      visit()

      current_path.pop()
      current_visited.remove((new_r, new_c))
      if (new_r, new_c) in all_clues:
        current_clues_remaining.add((new_r, new_c))
      
  visit()

  return [list(p) for p in shortest_path]




      







