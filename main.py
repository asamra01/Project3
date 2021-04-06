
class TermNode:
   def __init__(self, CoEfficient, Exponent, next=TermNode):

    self._coefficient = CoEfficient
    self._exponent = Exponent
    self._next = TermNode

   def __eq__(self, other):

   def __ne__(self, other):

       return not (self == other)

class Polynomial:

   def __init__(self, CoEfficient, exponent):

       self._first_node = TermNode(CoEfficient, exponent)

   def __add__(self, other):

