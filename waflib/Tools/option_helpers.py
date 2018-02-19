#!/usr/bin/env python
# encoding: utf-8
# Tim Mayberry, 2018

from waflib import Options

def add_enable_option(ctx, name, default, feature_str):
    feature_enable_str = 'Build with ' + feature_str + ' enabled'
    feature_disable_str = 'Build with ' + feature_str + ' disabled'
    ctx.add_option('--enable-' + name, action = 'store_true',
        default = default,
        dest = 'enable_' + name.replace('-','_'),
        help = feature_enable_str)
    ctx.add_option('--disable-' + name, action = 'store_false',
        #default = default,
        dest = 'enable_' + name.replace('-','_'),
        help = feature_disable_str )
