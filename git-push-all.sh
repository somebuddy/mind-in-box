#!/bin/bash

echo 'Pushing dev'
git checkout dev
git push bitbucket dev

echo 'Pushing staging'
git checkout staging
git push origin staging
git push bitbucket staging

echo 'Pushing heroku test server'
git checkout heroku_staging
git merge staging
git push heroku heroku_staging:master

echo 'Pushing master'
git checkout master
git push origin master
git push bitbucket master
git push production master

echo 'Return to dev branch'
git checkout dev
