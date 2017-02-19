#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
  if name is None or name is '':
    return "Hello, World!"
  else:
    return "Hello, {}!".format(name)
