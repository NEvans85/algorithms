require_relative "static_array"
require 'byebug'

class RingBuffer
  attr_reader :length

  def initialize
    @length = 0
    @capacity = 8
    @start_idx = 0
    @store = StaticArray.new(@capacity)
  end

  # O(1)
  def [](index)
    check_index(index)
    @store[offset(index)]
  end

  # O(1)
  def []=(index, val)
    check_index(index)
    @store[offset(index)] = val
  end

  # O(1)
  def pop
    check_index(0)
    @length -= 1
    @store[offset(@length)]
  end

  # O(1) ammortized
  def push(val)
    resize! if @length == @capacity
    @store[offset(@length)] = val
    @length += 1
  end

  # O(1)
  def shift
    check_index(0)
    shifted = @store[@start_idx]
    @start_idx += 1
    @start_idx = 0 if @start_idx == @capacity
    @length -= 1
    shifted
  end

  # O(1) ammortized
  def unshift(val)
    resize! if @length == @capacity
    @start_idx = @capacity if @start_idx.zero?
    @start_idx -= 1
    @store[@start_idx] = val
    @length += 1
  end

  protected
  attr_accessor :capacity, :start_idx, :store
  attr_writer :length

  def check_index(index)
    raise 'index out of bounds' if index >= @length
    true
  end

  def offset(index, cap = @capacity)
    (index + @start_idx) % cap
  end

  def resize!
    prev_cap = @capacity
    @capacity *= 2
    temp = @store.dup
    @store = StaticArray.new(@capacity)
    prev_cap.times do |idx|
      @store[offset(idx)] = temp[offset(idx, prev_cap)]
    end
  end
end
