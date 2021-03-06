require 'byebug'
require 'Set'
class DynamicProgramming

  def initialize
    @blair_cache = { 1 => 1, 2 => 2 }
    @frog_hop_cache = { 1 => [[1]],
                        2 => [[1, 1], [2]],
                        3 => [[1, 1, 1], [1, 2], [2, 1], [3]] }
    @distance_cache = {}
    @end_pos = []
end

  def nth_odd(n)
    (n * 2) - 1
  end

  # top-down
  # def blair_nums(n)
  #   return @blair_cache[n] if @blair_cache[n]
  #   @blair_cache[n] = blair_nums(n - 2) + blair_nums(n - 1) + nth_odd(n - 1)
  #   @blair_cache[n]
  # end

  # bottom-up
  def blair_nums(n)
    (3..n).each do |k|
      @blair_cache[k] = @blair_cache[k-1] + @blair_cache[k-2] + nth_odd(k-1)
    end
    @blair_cache[n]
  end

  def frog_hops_bottom_up(n)
    frog_cache_builder(n)[n]
  end

  def frog_cache_builder(n)
    cache = { 1 => [[1]],
              2 => [[1, 1], [2]],
              3 => [[1, 1, 1], [1, 2], [2, 1], [3]] }
    (4..n).each do |i|
      cache[i] = cache[i - 3].map { |a| a.dup.push(3) } +
                 cache[i - 2].map { |a| a.dup.push(2) } +
                 cache[i - 1].map { |a| a.dup.push(1) }
    end
    cache
  end

  def frog_hops_top_down(n)
    @frog_hop_cache = { 1 => [[1]],
                        2 => [[1, 1], [2]],
                        3 => [[1, 1, 1], [1, 2], [2, 1], [3]] }
    @frog_hop_cache[n] = frog_hops_top_down_helper(n)
    @frog_hop_cache[n]
  end

  def frog_hops_top_down_helper(n)
    return @frog_hop_cache[n] if @frog_hop_cache[n]
    frog_hops_top_down_helper(n - 1).map { |a| a.dup.push(1) } +
      frog_hops_top_down_helper(n - 2).map { |a| a.dup.push(2) } +
      frog_hops_top_down_helper(n - 3).map { |a| a.dup.push(3) }
  end

  def super_frog_hops(n, k)
    cache = { 1 => [[1]] }
    (2..n).each do |i|
      cache [i] = []
      (1..[k, i - 1].min).each do |j|
        cache[i] += cache[i - j].map { |a| a.dup.push(j) }
      end
      cache[i] << [i] if i <= k
    end
    cache[n]
  end

  def knapsack(weights, values, capacity)
    table = knapsack_table(weights, values, capacity)
    table[weights.length - 1][capacity]
  end

  # Helper method for bottom-up implementation
  def knapsack_table(weights, values, capacity)
    table = Array.new(weights.length) { Array.new(capacity + 1) {0} }
    min_weight = weights.min
    weights.each_with_index do |weight, row|
      (min_weight..capacity).each do |col|
        if weight > col && row > 0
          table[row][col] = table[row - 1][col]
        elsif row > 0
          table[row][col] = [values[row] + table[row - 1][col - weight],
                             table[row - 1][col]].max
        elsif weight <= col
          table[row][col] = values[row]
        end
      end
    end
    table
  end

  def maze_solver(maze, start_pos, end_pos)
    @end_pos = end_pos
    @distance_cache[end_pos] = 0
    @distance_cache[start_pos] = calc_distance(start_pos)
    curr_pos = start_pos
    path = [curr_pos]
    visited = { curr_pos => true }
    until curr_pos == @end_pos
      moves = neighbors(curr_pos).reject { |pos| maze[pos[0]][pos[1]] == 'X' }
      ordered_moves = moves.sort_by { |pos| calc_distance(pos) }
      new_moves = ordered_moves.reject { |pos| visited[pos] }
      best_move = new_moves.empty? ? ordered_moves[0] : new_moves[0]
      if path.include?(best_move)
        @distance_cache[curr_pos] = 1.0 / 0
        path.pop
      else
        path << best_move
        visited[best_move] = true
      end
      curr_pos = best_move
    end
    path
  end

  def calc_distance(pos)
    unless @distance_cache[pos]
      @distance_cache[pos] = Math.sqrt((pos[0] - @end_pos[0])**2 +
                                       (pos[1] - @end_pos[1])**2)
    end
    @distance_cache[pos]
  end

  def neighbors(pos)
    x, y = pos
    neighbors = [[x - 1, y], [x + 1, y],
                 [x, y + 1], [x, y - 1]]
    neighbors.reject { |n_pos| n_pos.any? { |el| el < 0 } }
  end
end
