# prompt: https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

n,k = gets.strip.split(' ')
n = n.to_i
k = k.to_i
a = gets.strip
a = a.split(' ').map(&:to_i)

k.times do
    a.push(a.shift)
end

puts a.join(" ")
