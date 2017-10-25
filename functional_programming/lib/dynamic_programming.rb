require 'byebug'
require 'Set'
class DynamicProgramming

  def initialize
    @blair_cache = { 1 => 1, 2 => 2 }
    @frog_hop_cache = { 1 => [[1]],
                        2 => [[1, 1], [2]],
                        3 => [[1, 1, 1], [1, 2], [2, 1], [3]] }
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
    return @frog_hop_cache[n] if @frog_hop_cache[n]
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
      if i <= k
        (1...i).each do |j|
          cache[i] += cache[i - j].map { |a| a.dup.push(j) }
        end
        cache[i] << [i]
      else
        (1..k).each do |j|
          cache[i] += cache[i - j].map { |a| a.dup.push(j) }
        end
      end
    end
    cache[n]
  end

  def knapsack(weights, values, capacity)
    table = knapsack_table(weights, values, capacity)
    debugger
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
  end
end
