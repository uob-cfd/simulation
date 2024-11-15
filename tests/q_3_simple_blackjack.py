
test = {
  'name': 'Question 3_simple_blackjack',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'p_total_21'
          >>> assert 'p_total_21' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_total_21'
          >>> # from its initial state (of ...)
          >>> assert p_total_21 != ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          # n = 10000
          # ranks = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
          # results = np.random.multinomial(3, np.ones(13) / 13, n * n)
          # scores = results @ ranks
          # per_n = (scores == 21).reshape((n, n)).sum(axis=1) / n
          # np.quantile(per_n , [0.001, 0.999])
          'code': r"""
          >>> assert 0.071 < p_total_21 < 0.089
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

"""
# Simulation to get bounds


import numpy as np

# Number of repeats
R = 10000
# Number of iterations
N = 10000

ranks = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
card_deck = np.repeat(ranks, 4)
simple_ps = np.zeros(R)
complex_ps = np.zeros(R)

rank_totals_1 = np.zeros(N)
rank_totals_11 = np.zeros(N)
for r in range(R):
    for i in np.arange(N):
        cards = np.random.choice(card_deck, 3, replace=False)
        rank_totals_1[i] = np.sum(cards)
        cards[cards == 1] = 11
        rank_totals_11[i] = np.sum(cards)
    simple_ps[r] = np.count_nonzero(rank_totals_1 == 21) / N
    rank_totals_1[rank_totals_11 == 21] = 21
    complex_ps[r] = np.count_nonzero(rank_totals_1 == 21) / N
print(np.quantile(simple_ps, [0.001, 0.999]))
print(np.quantile(complex_ps, [0.001, 0.999]))

Result:
[0.0720999 0.0886002]
[0.0815998 0.0989003]
"""
