# prompt: https://www.hackerrank.com/challenges/30-2d-arrays/submissions/code/58189612

# code
arr = Array.new(6)
for arr_i in (0..6-1)
    arr_t = gets.strip
    arr[arr_i] = arr_t.split(' ').map(&:to_i)
end

def calc_hourglass(arr, pos)
    arr[pos[0]][pos[1]] + arr[pos[0]][pos[1] + 1] + arr[pos[0]][pos[1] + 2] + arr[pos[0]+ 1][pos[1] + 1] + arr[pos[0] + 2][pos[1]] + arr[pos[0]+ 2][pos[1] + 1] + arr[pos[0]+ 2][pos[1] + 2]
end

best_hourglass = -1/0.0
(0..3).each do |row|
    (0..3).each do |col|
        test = calc_hourglass(arr, [row, col])
        best_hourglass = [best_hourglass, test].max
    end
end
puts best_hourglass
