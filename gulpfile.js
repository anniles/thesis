'use strict';
 
var gulp = require('gulp');
var sass = require('gulp-sass');
const autoprefixer = require('gulp-autoprefixer');
var sourcemaps = require('gulp-sourcemaps');

 
gulp.task('sass', function () {
  return gulp.src('./hotel/static/hotel/sass/**/*.sass')
  	.pipe(sourcemaps.init())
    .pipe(sass().on('error', sass.logError))
    .pipe(autoprefixer({
            browsers: ['last 5 versions'],
            cascade: false
        }))
  	.pipe(sourcemaps.write())
    .pipe(gulp.dest('./hotel/static/hotel/css'));
});
 
gulp.task('sass:watch', function () {
  gulp.watch('./hotel/static/hotel/sass/**/*.sass', ['sass']);
});

gulp.task('default', ['sass','sass:watch'])