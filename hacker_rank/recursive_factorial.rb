# prompt: https://www.hackerrank.com/challenges/30-recursion/problem

# code

def factorial(n)
  return 1 if [0, 1].include?(n)
  n * factorial(n - 1)
end

n = gets.strip.to_i
result = factorial(n)
puts result
