## grunt-gjshint

My sample linting project.  
http://ama-ch.hatenablog.com/entry/2013/04/21/160208

## Features

* Grunt project.
* Linting JavaScript files with JSHint + Google Closure Linter.
* Watch and lint only changed files.
* Notify results with grunt-notify.

## Usage

Before running Closure Linter, install python-gflags if you need.

```bash
$ easy_install python-gflags
```

Linting with JSHint:  
```bash
$ grunt jshint:all
```

Linting with Closure Linter:  
```bash
$ grunt gjslint:all
```

Fixing gjslint errors automatically:
```bash
$ grunt fixjsstyle:all
```

Linting with JSHint + Closure Linter (default task):  
```bash
$ grunt
```

Watch and notify:  
```bash
$ grunt watch
```

## License

* grunt-gjshint - MIT License
* Google Closure Linter - Apache License, Version 2.0  
https://code.google.com/p/closure-linter/source/browse/trunk/LICENSE
