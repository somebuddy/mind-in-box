#!/bin/bash

echo 'Pushing dev'
git checkout dev
git push bitbucket dev

echo 'Pushing staging'
git checkout staging
git push origin staging
git push bitbucket staging
git push heroku staging:master

echo 'Pushing master'
git checkout master
git push origin master
git push bitbucket master
