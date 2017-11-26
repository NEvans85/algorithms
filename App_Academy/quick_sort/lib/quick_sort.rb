require 'byebug'

class QuickSort
  # Quick sort has average case time complexity O(nlogn), but worst
  # case O(n**2).

  # Not in-place. Uses O(n) memory.
  def self.sort1(array)
    left = []
    right = []
    (1...array.length).each do |idx|
      case array[0] <=> array[idx]
      when -1
        right << array[idx]
      when 1, 0
        left << array[idx]
      end
    end
    QuickSort.sort1(left).concat([array[0]]).concat(QuickSort.sort1(right))
  end

  # In-place.
  def self.sort2!(array, start = 0, length = array.length, &prc)
    return array if length <= 1
    prc ||= proc { |a, b| a <=> b }
    barrier = QuickSort.partition(array, start, length, &prc)
    QuickSort.sort2!(array, start, barrier - start, &prc)
    QuickSort.sort2!(array, barrier + 1, length - (barrier + 1), &prc)
  end

  def self.partition(array, start, length, &prc)
    barrier = start
    prc ||= proc { |a, b| a <=> b }
    ((start + 1)...(start + length)).each do |idx|
      if prc.call(array[start], array[idx]) == 1
        barrier += 1
        array[idx], array[barrier] = array[barrier], array[idx]
      end
    end
    array[start], array[barrier] = array[barrier], array[start]
    barrier
  end
end
