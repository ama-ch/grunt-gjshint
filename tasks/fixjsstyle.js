/**
 * @param {*} grunt
 */
module.exports = function(grunt) {
  'use strict';

  grunt.registerMultiTask('fixjsstyle', 'Run fixjsstyle.', function() {
    var linter = require('./lib/closure-linter');

    /**
     * @param {Object} err
     * @param {Object} result
     * @param {number} code
     */
    var callback = function(err, result, code) {
      if (code === 0) {
        grunt.log.ok(result.stdout || 'No file to fix.');
      } else {
        grunt.fail.warn(result.stdout);
      }
    };

    linter.run(this, callback);
  });
};
