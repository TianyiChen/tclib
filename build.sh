rm -f dist/* && python3 setup.py sdist bdist_wheel &&pip3 install --no-deps --force-reinstall  dist/*.whl
