# doggo
A python app that turns a yaml [DoGo map](https://uxpamagazine.org/creating-a-dogo-map/) into a clickable prototype.

The `app.yaml` file in the root is the yaml file that defines the structure of the application. You can add new yaml objects to extend it. The schema for each entry is:

```
node_name:
  name: the friendly name of the node
  desc: A description of the node
  inputs:
    - a list of input fields
  do:
    - a list of things the user can do
  go:
    - a list of other node_names that should be linked to this page.
```

The `node_name` is how the node is addressed in the browser. If you have a 'main' node, it is accessible via http://localhost:8000/main.

In the default templates, data in a `node_name` of `common` will be appended to the data in the addressed node.

The `templates` can be overridden. The app searches for a `node_name`.html. If it can't be found, `default.html` will be used.

The templates extend the `base.html`.

## Installation
The application uses [pipenv](https://pipenv.pypa.io/en/latest/). Running `pipenv install` will install the dependencies. 

## Commands

`uvicorn main:app --reload`
Starts the application. Visit localhost:8000 in a browser to load the app.

`pycodestyle` is the included linter, and `pytest` is the included test runner.

