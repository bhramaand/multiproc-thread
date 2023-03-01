rm -rf anek_process.egg-info
rm -rf build
rm -rf dist
python3 release.py $1
python3 setup.py sdist bdist_wheel
# python3 -m twine upload --repository pypi dist/* --verbose