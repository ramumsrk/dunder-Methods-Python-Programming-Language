#! /usr/bin/python3.12

import logging_configuration

import point.point

import logging

if __name__ == '__main__':

  first_point_instance: point.point.Point = point.point.Point(
    x_coordinate=1,
    y_coordinate=2
  )

  logging.debug(
    f'First point instance: {first_point_instance=}'
  )
  logging.debug(
    F'{first_point_instance.__str__()}'
  )
  logging.debug(
    f'{first_point_instance.__repr__()}'
  )
  logging.debug(
    F'{str(first_point_instance)}'
  )  
  logging.debug(
    f'{repr(first_point_instance)}'
  )