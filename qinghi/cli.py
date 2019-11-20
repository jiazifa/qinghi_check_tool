#! -*- coding: utf-8 -*-

import sys
import importlib
import codecs
from argparse import ArgumentParser
from typing import Optional, Text, Sequence
import qinghi


def import_class(import_string):
    try:
        module, classname = import_string.rsplit(".", 1)
        print(module, classname)
        cls = getattr(importlib.import_module(module), classname)
    except ValueError:
        sys.exit("Please supply module.classname.")
    except ImportError:
        sys.exit("Cannot import module %s" % module)
    except AttributeError:
        sys.exit("Cannot find class {} in module {}".format(classname, module))
    else:
        return cls


def parse(args):
    parser = ArgumentParser(prog='qinghi')

    parser.add_argument('-v', '--version', action='version',
                        version=qinghi.__version__)

    parser.add_argument('-a', '--action', type=import_class,
                        default='qinghi.User', help='action you can choice')
    parser.add_argument('-n', '--name', help='name for login')
    parser.add_argument('-p', '--password', help='password for login')
    return parser.parse_args(args=args)


def main():
    namespace = parse(sys.argv[1:])
    qh = qinghi.Qinghi(widget=namespace.action, extras=vars(namespace))
    print(qh)
