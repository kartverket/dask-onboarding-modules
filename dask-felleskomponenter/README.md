# DASK Felleskomponenter

This is a repo where we make available governance components, common functions and reusable UDFs. DASK felleskomponenter is still in an early stage of the development process.

## Dependencies

You need to install Python3.7 and higher, and to install the dependencies of this project, please execute the following
command

```bash
pip install -r requirements.txt
```

## Bulding and publishing of package

### Steps

- Remove old dist-folder, from last time you published
- Update version in `setup.py`, for instance `0.0.7`->`0.0.8`
- Add change info to CHANGES.txt
- (Run `pip install -r requirements.txt` if you haven't done that earlier)
- Run `python3 -m build` (and wait some minutes...)
- Verity that dist contains a package with the new version in the package name.
- Run `python3 -m twine upload dist/*` to upload to pypi

### To upload to PyPi test

Replace the last command with `python3 -m twine upload --repository testpypi dist/*`

## Run tests

Use the following command
```sh
coverage run -m unittest discover -s src/tests
coverage report -m
```