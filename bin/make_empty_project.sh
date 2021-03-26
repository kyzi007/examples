#!/bin/bash
# copy, add your own lovely steps and enjoy this
# make_empty_project.sh project-name git@github.com:account/project-name.git

mkdir "${1}" && cd "${1}"

touch README.md
touch .gitignore
touch Makefile
touch requarements.txt

virtualenv venv

git init
git remote add origin "${2}"
git add .
git commit -m "initial commit"
git push --set-upstream origin master
