require_relative 'p02_hashing'

class HashSet
  attr_reader :count

  def initialize(num_buckets = 8)
    @store = Array.new(num_buckets) { Array.new }
    @count = 0
  end

  def insert(key)
    unless include?(key)
      hash = key.hash
      self[hash] << key
      @count += 1
      resize! if @count == num_buckets
    end
  end

  def include?(key)
    hash = key.hash
    self[hash].include?(key)
  end

  def remove(key)
    hash = key.hash
    self[hash].delete(key)
  end

  private

  def [](num)
    # optional but useful; return the bucket corresponding to `num`
    @store[num % num_buckets]
  end

  def num_buckets
    @store.length
  end

  def resize!
    elements = @store.flatten
    @store = Array.new(num_buckets * 2) { [] }
    @count = 0
    elements.each { |el| insert(el) }
  end
end
