# Implement a queue with #enqueue and #dequeue, as well as a #max API,
# a method which returns the maximum element still in the queue. This
# is trivial to do by spending O(n) time upon dequeuing.
# Can you do it in O(1) amortized? Maybe use an auxiliary storage structure?

# Use your RingBuffer to achieve optimal shifts! Write any additional
# methods you need.

require_relative 'ring_buffer'

class QueueWithMax
  attr_accessor :store

  def initialize
    @store = RingBuffer.new
    @max_store = RingBuffer.new
  end

  def enqueue(val)
    @store.push(val)
    max_count = @max_store.length
    max_count.times do |i|
      @max_store.pop if @max_store[max_count - 1 - i] < val
    end
    @max_store.push(val)
  end

  def dequeue
    @max_store.shift if @store.shift == @max_store[0]
  end

  def max
    @max_store[0]
  end

  def length
    @store.length
  end

  protected

  def find_new_max
    @max = -1.0 / 0.0
    @store.length.times do |idx|
      @max = @store[idx] if @store[idx] > @max
    end
  end

end
