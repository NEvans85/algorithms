# prompt: https://www.hackerrank.com/challenges/30-recursion/problem

# code

def factorial(n)
    return 1 if n == 1 || n == 0
    return n * factorial(n - 1)
end

n = gets.strip.to_i
result = factorial(n)
puts result
