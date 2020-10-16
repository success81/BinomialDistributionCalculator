def binomial_calculator(p,n,k):
  def factorial(c):
     if c == 0:
        return 1
     else:
        return c * factorial(c-1)
  total_times = factorial(9) / (factorial(5) * (factorial(9-5)))
  outcome_prob = p**k * (1-p)**(n-k)

  total_prob = total_times * outcome_prob

  return (outcome_prob)
