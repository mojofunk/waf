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

def add_with_option(ctx, name, default, package_str):
    package_with_str = 'Build with ' + package_str + ' included'
    package_without_str = 'Build without ' + package_str + ' included'
    ctx.add_option('--with-' + name, action = 'store_true',
        default = default,
        dest = 'with_' + name.replace('-','_'),
        help = package_with_str)
    ctx.add_option('--without-' + name, action = 'store_false',
        #default = default,
        dest = 'with_' + name.replace('-','_'),
        help = package_without_str )
