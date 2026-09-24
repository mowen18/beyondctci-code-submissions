# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def ikea_shopping(budget, prices, ratings):
  best_rating_sum = 0
  best_items = []
  n = len(prices)
  items = []
  def visit(i, cur_cost, cur_rating_sum):
    nonlocal best_items, best_rating_sum
    if i == n:
      if cur_rating_sum > best_rating_sum:
        best_rating_sum = cur_rating_sum
        best_items = items.copy()
      return
    
    visit(i + 1, cur_cost, cur_rating_sum)
    if cur_cost + prices[i] <= budget:
      items.append(i)
      visit(i + 1, cur_cost + prices[i], cur_rating_sum + ratings[i])
      items.pop()
  visit(0, 0, 0)
  return best_items

