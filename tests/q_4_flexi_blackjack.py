
test = {
  'name': 'Question 4_flexi_blackjack',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'p_flex_total_21'
          >>> assert 'p_flex_total_21' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_flex_total_21'
          >>> # from its initial state (of ...)
          >>> assert p_flex_total_21 != ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          # See simulation code in q_3_simple_blackjack.py
          'code': r"""
          >>> assert 0.081 < p_flex_total_21 < 0.099
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
