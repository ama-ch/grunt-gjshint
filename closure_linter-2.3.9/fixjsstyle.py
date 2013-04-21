#!/usr/bin/env python
# -*- coding: utf-8 -*-

from closure_linter import fixjsstyle
import errorrules

if __name__ == '__main__':
  errorrules.InjectErrorReporter()
  fixjsstyle.main()
