#!/usr/bin/env python
#
# Copyright 2012 The Closure Linter Authors. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Unit tests for the statetracker module."""

# Allow non-Google copyright
# pylint: disable-msg=C6304

__author__ = ('nnaze@google.com (Nathan Naze)')



import unittest as googletest

from closure_linter import statetracker


class _FakeDocFlag(object):

  def __repr__(self):
    return '@%s %s' % (self.flag_type, self.name)


class DocCommentTest(googletest.TestCase):

  @staticmethod
  def _MakeDocFlagFake(flag_type, name=None):
    flag = _FakeDocFlag()
    flag.flag_type = flag_type
    flag.name = name
    return flag

  def testDocFlags(self):
    comment = statetracker.DocComment(None)

    a = self._MakeDocFlagFake('param', 'foo')
    comment.AddFlag(a)

    b = self._MakeDocFlagFake('param', '')
    comment.AddFlag(b)

    c = self._MakeDocFlagFake('param', 'bar')
    comment.AddFlag(c)

    self.assertEquals(
        ['foo', 'bar'],
        comment.ordered_params)

    self.assertEquals(
        [a, b, c],
        comment.GetDocFlags())

  def testInvalidate(self):
    comment = statetracker.DocComment(None)

    self.assertFalse(comment.invalidated)
    self.assertFalse(comment.IsInvalidated())

    comment.Invalidate()

    self.assertTrue(comment.invalidated)
    self.assertTrue(comment.IsInvalidated())

  def testSuppressionOnly(self):
    comment = statetracker.DocComment(None)

    self.assertFalse(comment.SuppressionOnly())
    comment.AddFlag(self._MakeDocFlagFake('suppress'))
    self.assertTrue(comment.SuppressionOnly())
    comment.AddFlag(self._MakeDocFlagFake('foo'))
    self.assertFalse(comment.SuppressionOnly())

  def testRepr(self):
    comment = statetracker.DocComment(None)
    comment.AddFlag(self._MakeDocFlagFake('param', 'foo'))
    comment.AddFlag(self._MakeDocFlagFake('param', 'bar'))

    self.assertEquals(
        '<DocComment: [\'foo\', \'bar\'], [@param foo, @param bar]>',
        repr(comment))


if __name__ == '__main__':
  googletest.main()