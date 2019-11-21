#! -*- coding: utf-8 -*-

import sys
import importlib
import codecs
from argparse import ArgumentParser
from typing import Optional, Text, Sequence
import qinghi
from qinghi.config import Config


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

    parser.add_argument('-m', '--module', type=import_class,
                        default='qinghi.User', help='action you can choice')

    parser.add_argument('-c', '--config', help='where is config file')
    parser.add_argument('-a', '--action', help='Action for module')
    return parser.parse_args(args=args)


def main():
    namespace = parse(sys.argv[1:])
    config = Config(namespace.config)
    qh = qinghi.Qinghi(widget=namespace.module,
                       action=namespace.action, config=config)
    qh.execute()
