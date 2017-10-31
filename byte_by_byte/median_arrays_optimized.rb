

def median(arr)
  if arr.length.odd?
    arr[arr.length / 2]
  else
    (arr[arr.length / 2] + arr[(arr.length / 2) - 1]) / 2.0
  end
end

def median_two(arr1, arr2)
  if arr1.length == 2 && arr2.length == 2
    return ([arr1[0],arr2[0]].max + [arr1[1], arr2[1]].min) / 2.0
  end
  median1 = median(arr1)
  median2 = median(arr2)
  case median1 <=> median2
  when 0
    median1
  when -1
    median_two(arr1[(arr1.length / 2) - 1...arr1.length], arr2[0..(arr2.length / 2) + 1])
  when 1
    median_two(arr1[0..(arr1.length / 2) + 1], arr2[(arr2.length / 2) - 1...arr2.length])
  end
end
