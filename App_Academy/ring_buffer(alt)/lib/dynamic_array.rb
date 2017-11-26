require_relative "static_array"

class DynamicArray
  attr_reader :length

  def initialize
    @length = 0;
    @capacity = 8;
    @store = StaticArray.new(@capacity)
  end

  # O(1)
  def [](index)
    check_index(index)
    @store[index]
  end

  # O(1)
  def []=(index, value)
    check_index(index)
    @store[index] = value
  end

  # O(1)
  def pop
    check_index(0)
    @length -= 1
    @store[@length]
  end

  # O(1) ammortized; O(n) worst case. Variable because of the possible
  # resize.
  def push(val)
    resize! if @length == @capacity
    @store[@length] = val
    @length += 1
  end

  # O(n): has to shift over all the elements.
  def shift
    check_index(0)
    to_shift = @store[0]
    @length -= 1
    @length.times do |i|
      @store[i] = @store[i + 1]
    end
    to_shift
  end

  # O(n): has to shift over all the elements.
  def unshift(val)
    resize! if @length == @capacity
    @length.downto(1) do |i|
      @store[i] = @store[i - 1]
    end
    @store[0] = val
    @length += 1
  end

  protected
  attr_accessor :capacity, :store
  attr_writer :length

  def check_index(index)
    raise "index out of bounds" if index >= @length
  end

  # O(n): has to copy over all the elements to the new store.
  def resize!
    @capacity *= 2
    temp = @store.dup
    @store = StaticArray.new(@capacity)
    @length.times do |i|
      @store[i] = temp[i]
    end
  end
end
