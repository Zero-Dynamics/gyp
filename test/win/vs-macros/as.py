#!/usr/bin/env python

# Copyright (c) 2012 Google Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from optparse import OptionParser

parser = OptionParser()
parser.add_option('-a', dest='platform')
parser.add_option('-o', dest='output')
parser.add_option('-p', dest='path')
(options, args) = parser.parse_args()

with open(options.output, 'w') as f:
    print('options', options, file=f)
    print('args', args, file=f)
