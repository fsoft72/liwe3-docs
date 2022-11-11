#!/bin/bash

upd=$(date "+%Y-%m-%d %H:%M:%S")

sed -i "s/Last update.*/Last update: $upd/" overrides/partials/copyright.html

rm -Rf site
mkdocs build
cd site
tar cfj - * | ssh liwe@liwe.org "cd public_html; tar xvfj -"
cd ..
rm -Rf site
