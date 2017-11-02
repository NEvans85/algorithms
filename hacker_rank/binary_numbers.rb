# prompt: https://www.hackerrank.com/challenges/30-binary-numbers/problem

# code

n = gets.strip.to_i

b = n.to_s(2)
max_count = 0
one_count = 0
b.each_char do |ch|
  if ch == '1'
    one_count += 1
  else
    max_count = one_count if one_count > max_count
    one_count = 0
  end
end
max_count = one_count if one_count > max_count
puts max_count
