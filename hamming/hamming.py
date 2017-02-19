def distance(strand1, strand2):
  hamming = 0

  if len(strand1) != len(strand2):
      raise ValueError('strands are different lenths')

  for ch1, ch2 in zip(strand1,strand2):
      if ch1 != ch2:
          hamming += 1

  return hamming
