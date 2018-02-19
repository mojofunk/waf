#! /usr/bin/env python
# encoding: utf-8
# Tim Mayberry, 2017

from waflib.Tools.option_helpers import add_enable_option

def options(opt):
    add_enable_option(opt, "shared", True, 'shared libraries')
    add_enable_option(opt, "static", False, 'static libraries')


def configure(conf):
    conf.env.ENABLE_SHARED = conf.options.enable_shared
    conf.env.ENABLE_STATIC = conf.options.enable_static
