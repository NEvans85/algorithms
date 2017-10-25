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

  end

  def knapsack(weights, values, capacity)

  end

  # Helper method for bottom-up implementation
  def knapsack_table(weights, values, capacity)

  end

  def maze_solver(maze, start_pos, end_pos)
  end
end
