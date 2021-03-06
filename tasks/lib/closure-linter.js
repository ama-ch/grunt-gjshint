(function(exports) {
  'use strict';

  var grunt = require('grunt');

  /**
   * @param {Object} options
   * @param {Array.<string>} files
   * @return {Array.<string>}
   */
  var buildArguments = function(options, files) {
    var args = options.args || [];
    if (options.flagfile) {
      args.push('--flagfile');
      args.push(options.flagfile);
    }
    return grunt.util._.union(args, files);
  };

  /**
   * @param {Object} task
   * @param {function(Object, Object, number)} callback
   */
  exports.run = function(task, callback) {
    var done = task.async();
    var files = task.filesSrc;
    var args = buildArguments(task.options(), files);

    grunt.verbose.writeln('cmd: ' + task.data.cmd.cyan);
    grunt.verbose.writeln('args: ', args.join(' ').cyan);

    grunt.util.spawn({
      cmd: task.data.cmd,
      args: args
    }, function(err, result, code) {
      callback(err, result, code);
      done();
    });
  };

})(typeof exports === 'object' && exports || this);
