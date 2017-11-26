require_relative "heap"

class Array
  def heap_sort!
    heapify!
    extract_each!
  end

  def heapify!
    heaped = 1
    while heaped < length
      BinaryMinHeap.heapify_up(self, heaped, heaped + 1) { |a, b| -1 * (a <=> b) }
      heaped += 1
    end
  end

  def extract_each!
    barrier = length - 1
    until barrier.zero?
      self[0], self[barrier] = self[barrier], self[0]
      BinaryMinHeap.heapify_down(self, 0, barrier) { |a, b| -1 * (a <=> b) }
      barrier -= 1
    end
  end
end
