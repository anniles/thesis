/* jshint node:true */
'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');
var sourcemaps = require('gulp-sourcemaps');

gulp.task('sass', function () {
  return gulp.src('./kavala/static/sass/**/*.sass')
  	.pipe(sourcemaps.init())
    .pipe(sass().on('error', sass.logError))
    .pipe(autoprefixer({
            browsers: ['last 5 versions'],
            cascade: false
        }))
    .pipe(sourcemaps.write())
    .pipe(gulp.dest('./kavala/static/css'));
});

gulp.task('sass:watch', function () {
  gulp.watch('./kavala/static/sass/**/*.sass', ['sass']);
});

gulp.task('default', ['sass','sass:watch']);
