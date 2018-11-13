# phoebe2-docs

To start, any of the following index pages or the live-version of the docs at [phoebe-project.org/docs](http://phoebe-project.org/docs):

* [Tutorials](tutorials.md)
* [Datasets & Observables](datasets.md)
* [Physics & Individual Parameters](physics.md)
* [Example Scripts](examples.md)
* [API Documentation](api.md)

## Noticed an Error?

If you noticed an error, whether it be a typo, incorrect output, whatever, feel free to open a pull request or file an issue in the issue tracker.  We'll try our best to fix the issue so that everyone else can benefit.

## Updating Documentation

### Index Markdown Pages

All markdown pages (except in the [API](./api) directory) can be edited manually and pushed.  Make sure the page is rendered correctly both here on GitHub and on the website.

### Jupyter Notebooks

Jupyter notebooks can be updated locally, but make sure you have the matching version of PHOEBE installed on your machine and that you run the notebook through entirely before saving and pushing your changes.

### API Docs

Updates to the API docs for archived versions of PHOEBE should be done directly to the markdown files.  For active versions of PHOEBE, the updates should be made to the docstring in the source-code itself in the [phoebe2 repository](http://github.com/phoebe-project/phoebe2) and either copied to the markdown or recompiled.

To recompile the markdown versions of the API docs from the source code, make sure the installed version of PHOEBE matches the branch of the documentation and then call the [make_apidocs.py](./make_apidocs.py) script.  Commit and push all necessary changes.
