#! /usr/bin/python3.12

from typing import Self, Literal

class Point:
  """A class representing a point on the two-dimensional x and y axis"""
  # Instance creation
  def __new__(
    klass,
    *args,
    **kwargs
  ) -> Self:
    '''New instance creation'''
    return super().__new__(klass)
  # Instance initialization
  def __init__(
    self,
    *,
    x_coordinate: Literal[int],
    y_coordinate: Literal[int]
  ) -> Literal[None]:
    """New instance initialization"""
    self.x_coordinate = x_coordinate
    self.y_coordinate = y_coordinate
    return None
  # Human readable
  # representation of
  # a Point instance as
  # a string
  def __str__(
    self,
    /
  ) -> Literal[str]:
    """Human readable string representation of a Point instance"""
    return f'({self.x_coordinate}, {self.y_coordinate})'
  # Internal representation
  # of a Point instance as
  # a string
  def __repr__(
    self,
    /
  ) -> Literal[str]:
    '''Internal string representation of a Point instance'''
    return F'Point{self.__str__()}'