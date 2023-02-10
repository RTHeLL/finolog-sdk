#!/bin/sh
value=`cat finolog/_version.py  | cut -d '"' -f 2`
echo "$value"
git tag "v$value"
git push origin --tags
python setup.py sdist bdist_wheel
python -m twine upload --skip-existing --repository pypi dist/*