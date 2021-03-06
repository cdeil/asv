# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import six

from .. import machine


class Machine(object):
    @classmethod
    def setup_arguments(cls, subparsers):
        parser = subparsers.add_parser(
            "machine", help="Define information about this machine",
            description="""
            Defines information about this machine.  If no arguments
            are provided, an interactive console session will be used
            to ask questions about the machine.
            """)

        defaults = machine.Machine.get_defaults()
        for name, description in machine.Machine.fields:
            parser.add_argument(
                '--' + name, default=defaults[name],
                help=description)

        parser.set_defaults(func=cls.run_from_args)

        return parser

    @classmethod
    def run_from_args(cls, args):
        return cls.run(**vars(args))

    @classmethod
    def run(cls, **kwargs):
        different = {}
        defaults = machine.Machine.get_defaults()
        for key, val in six.iteritems(defaults):
            if kwargs.get(key) != val:
                different[key] = kwargs.get(key)

        machine.Machine.load(
            interactive=(len(different) == 0), **different)
