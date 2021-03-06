# -*- encoding:utf-8 -*-

# These are some common function which may be used in different shape.
# module inc

import math
import os
from string import Template


def get_effective_radius(nums=1, d=0.001):
    """
    get the effective radius of shape according the size of d and the total nums of d.
    """
    effective_radius = d * (3 * nums / math.pi / 4) ** (1. / 3)
    return effective_radius


def tpl_dir():
    """
    get template path of shape.tpl
    """
    real_file = os.path.realpath(__file__)
    real_path = os.path.dirname(real_file)
    tpl_full_path = os.path.join(real_path, 'Template', 'shape.tpl')
    return tpl_full_path


def shape_dir():
    """
    get the path of shape.dat
    """
    return os.path.join(os.path.abspath('.'), 'shape.dat')


def print_line(index=1, center=(0, 0, 0), point=(0, 0, 0)):
    """
    format data that will be writted into shape.dat
    """
    line = "%6d\t%3d\t%3d\t%3d\t%d\t%d\t%d\n" % (
        index, center[0] + point[0], center[1] + point[1], center[2] + point[2], 1, 1, 1)
    return line


def write_shape(point_max=(50, 50, 50), index=1, data=""):
    """
    write shape.dat with given point max and index and data
    """
    replace_string = {'nx': point_max[0], 'ny': point_max[1], 'nz': point_max[2], 'total': index - 1, 'data': data}
    # read template content
    content_tpl = open(tpl_dir(), 'r').read()
    tpl = Template(content_tpl)
    # replace template with real data
    content_shape = tpl.substitute(replace_string)
    open(shape_dir(), 'w').write(content_shape)
    # get effective radius
    effective_radius = get_effective_radius(nums=index)
    print 'Write shape.dat successfully and effective radius is %s...' % effective_radius
