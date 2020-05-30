Introduction

This is a repo for an application for a Single Page Application featuring the Laravel PHP framework and the front-end framework Angular. It implements a system to control and supervises one or several farms of microgreens.

********** Installations **********

* Prerequisites and Assumptions

Composer and npm already installed.

* Laravel

cd test-backend

composer install

Copy .env.exampleand rename it to .env

php artisan key:generate

APP_KEY in .env file should be automatically set. If not, update your APP_KEY in .env file with the key generated above.

* Angular

cd test-frontend

npm install