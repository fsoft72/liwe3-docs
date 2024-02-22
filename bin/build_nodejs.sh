#!/bin/bash

NODEJS_SOURCE=/home/fabio/dev/projects/liwe3-playground/server/server/liwe

# Open the mkdocs.yml and remove all "Library" / "Authetication" section and add the "===APPEND===" line right before the "Authentication" section
cat mkdocs.yml | sed '/Library/,/Authentication/{//!d}' > mkdocs.yml.tmp

# Add "===END" line right after the Library / Authentication section
sed -i '/Library/a ===END===' mkdocs.yml

# for all *ts files in $NODEJS_SOURCE  call the `jsdoc2md.py` script and append the output to the `mkdocs.yml` in the `Library` section
for file in $NODEJS_SOURCE/*.ts; do
    # if the file contains 'test' in the path, skip it
    if [[ $file == *"test"* ]]; then
        continue
    fi

    fname=$(basename $file .ts)
    echo "Processing $fname"
    ./bin/jsdoc2md.py $file > docs/liwe3/nodejs/files/$fname.md

    sed -i '/===END===/i \              - '$fname': liwe3/nodejs/files/'$fname'.md' mkdocs.yml
done

sed -i '/===END===/d' mkdocs.yml
