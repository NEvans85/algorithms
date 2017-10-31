# arr1 = [1,3,5]
# arr2 = [2,4,6]
# median(arr1, arr2) = 3.5

# brute force. O(n) time and space complexity
def median(arr1, arr2)
  merged = []
  d_arr1 = arr1.dup
  d_arr2 = arr2.dup
  until d_arr1.empty? && d_arr2.empty?
    case d_arr1[0] <=> d_arr2[0]
    when -1
      merged << d_arr1.shift
    when 0
      merged << d_arr1.shift
      merged << d_arr2.shift
    when 1
      merged << d_arr2.shift
    when nil
      d_arr1.empty? ? merged << d_arr2.shift : merged << d_arr1.shift
    end
  end
  median = nil
  if merged.length.odd?
    median = merged[merged.length / 2]
  else
    median = (merged[merged.length / 2] + merged[(merged.length / 2) - 1]) / 2.0
  end
  median
end
