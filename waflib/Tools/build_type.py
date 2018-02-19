#!/usr/bin/env python
# encoding: utf-8
# Tim Mayberry, 2017

from waflib.Configure import conf

def options(self):
    self.add_option('--build-type', action = 'store',
    default = "debug",
    choices = ('plain', 'debug', 'debugoptimized', 'optimized'),
    dest = 'build_type',
    help = 'Determines the compiler flags used for the build (plain,debug,debugoptimize,optimize) [default: debug]')

@conf
def set_gcc_compiler_flags(self):
    if "debug" in self.options.build_type:
        self.env.prepend_value('CFLAGS', ['-g'])
        self.env.prepend_value('CXXFLAGS', ['-g'])
    elif "optimized" in self.options.build_type:
        self.env.prepend_value('CFLAGS', ['-O2'])
    # configure warnings
    self.env.prepend_value('CFLAGS', ['-Wall', '-Wextra'])

@conf
def set_msvc_compiler_flags(self):
    if "debug" in self.options.build_type:
        self.env.CFLAGS += ['/DEBUG']
        # disables optimization, to speed compilation and simplify debugging.
        self.env.CFLAGS += ['/Od']

        # TODO This should probably be /MDd ??
        self.env.CFLAGS += ['/MD']
        #self.env.CFLAGS += ['/MDd']

        # produces .obj files containing full symbolic debugging information
        self.env.CFLAGS += ['/Z7']

        # compiler uses locks to write syncronously to PBD files, not
        # recommended, available in msvc >= 12 (2013)
        #self.env.CFLAGS += ['/FS']

        self.env.LINKFLAGS += ['/DEBUG']

    # TODO debugoptimized
    elif "optimized" in self.options.build_type:
        self.env.CFLAGS += ['/O2']
        self.env.CFLAGS += ['/MD']

    # use ISO-standard C++ exception handling
    self.env.CXXFLAGS += ['/EHsc']
    self.env.LINKFLAGS += ['/INCREMENTAL:NO']

    # configure warnings
    self.env.CFLAGS += ['/W4', '/D_CRT_SECURE_NO_WARNINGS']
    # ignore "possible loss of data" warnings
    self.env.CFLAGS += ['/wd4305', '/wd4244', '/wd4245', '/wd4267']
    # ignore "unreferenced formal parameter" warnings
    self.env.CFLAGS += ['/wd4100']
    # TODO add some more warnings from glib


@conf
def set_compiler_flags(self):
    if self.env.CC_NAME == 'msvc':
        set_msvc_compiler_flags(self)
    else:
        set_gcc_compiler_flags(self)


def configure(self):
    if self.options.build_type == 'plain':
        return
    elif "debug" in self.options.build_type:
        self.define('DEBUG', 1)
    else:
        self.define('NDEBUG', 1)

    self.set_compiler_flags()
