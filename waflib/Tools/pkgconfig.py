#! /usr/bin/env python
# encoding: utf-8
# Tim Mayberry, 2017

from waflib.Configure import conf


@conf
def pkgconfig_check_required_deps(self, deps):
    args = ['--cflags', '--libs']
    if self.env.CC_NAME == 'msvc':
        args += ['--msvc-syntax']
    for pkg, version in deps.items():
        args += ['%s >= %s' % (pkg, version)]
        self.check_cfg(package=pkg, args=args)


@conf
def pkgconfig_check_optional_deps(self, deps):
    args = ['--cflags', '--libs']
    if self.env.CC_NAME == 'msvc':
        args += ['--msvc-syntax']
    for pkg, version in deps.items():
        args += ['%s >= %s' % (pkg, version)]
        self.check_cfg(package=pkg, args=args, mandatory=False)


def configure(self):
    pass
