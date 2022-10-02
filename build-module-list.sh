#!/bin/bash

# Open the mkdocs.yml and remove all "Modules" section
sed -i '/- Modules:/,/  - /d' mkdocs.yml

# Append the "Modules" section to the mkdocs.yml
echo "  - Modules:" >> mkdocs.yml
echo "    - Introduction: modules/index.md" >> mkdocs.yml

cd docs/modules

echo "# Modules" > index.md
echo "" >> index.md

echo "This is a list of all public modules in the LiWE Project." >> index.md
echo "" >> index.md


ls *.md | while read c
do
	# skip "index.md"
	if [ "$c" == "index.md" ]; then
		continue
	fi

	echo $c

	# Uppercase first letter
	capitalized=$(echo $c | sed -e 's/\(.\)/\u\1/')

	# Remove ".md"
	capitalized=$(echo $capitalized | sed -e 's/\.md//')

	echo "* [$capitalized]($c)" >> index.md

	# Append the module to the mkdocs.yml
	echo "    - $capitalized: modules/$c" >> ../../mkdocs.yml
done
