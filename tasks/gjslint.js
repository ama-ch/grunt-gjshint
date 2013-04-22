/**
 * @param {*} grunt
 */
module.exports = function(grunt) {
  'use strict';

  grunt.registerMultiTask('gjslint', 'Run gjslint.', function() {
    var linter = require('./lib/closure-linter');
    var files = this.filesSrc;

    /**
     * @param {Object} err
     * @param {Object} result
     * @param {number} code
     */
    var callback = function(err, result, code) {
      if (code === 0) {
        grunt.log.ok(files.length + ' file' + (files.length === 1 ? '' : 's') + ' gjslint free.');
      } else {
        grunt.fail.warn(result.stdout);
      }
    };

    linter.run(this, callback);
  });
};
