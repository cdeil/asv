# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import sys

import six

from . import commands
from .console import console


def main():
    console.enable()

    parser, command_parsers = commands.make_argparser()

    args = parser.parse_args()
    try:
        args.func(args)
    except RuntimeError as e:
        console.error(six.text_type(e))
        sys.exit(1)
    except AttributeError:  # In Python 3.3 func is not set up if no command
        parser.print_usage()
        sys.exit(1)

    console._newline()
