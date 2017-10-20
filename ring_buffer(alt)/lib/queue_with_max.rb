# Implement a queue with #enqueue and #dequeue, as well as a #max API,
# a method which returns the maximum element still in the queue. This
# is trivial to do by spending O(n) time upon dequeuing.
# Can you do it in O(1) amortized? Maybe use an auxiliary storage structure?

# Use your RingBuffer to achieve optimal shifts! Write any additional
# methods you need.

require_relative 'ring_buffer'

class QueueWithMax
  attr_accessor :store
  attr_reader :max

  def initialize
    @store = RingBuffer.new
    @max = -1.0 / 0.0
  end

  def enqueue(val)
    @max = val if @max < val
    @store.push(val)
  end

  # find_new_max has O(@store.length) however the dequeue function should
  # only run it 1/@store.length of the time on average.
  # I think this makes the amortized complexity O(1).
  # However, in the worst case scenario (numbers queued in descending order)
  # dequeue's complexity is O(n)
  def dequeue
    find_new_max if @store.shift == @max
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
