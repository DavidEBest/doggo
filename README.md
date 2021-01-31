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

If you'd prefer to use docker, `docker-compose build` and `docker-compose up` can launch the application as well.


## Roadmap and Vision

I like prototyping in software. Usually I use straight HTML/CSS or Angular, depending on the complexity of the application.

HTML/CSS can be too fiddly and have too much copy and paste. Angular is, well, Angular. Routing and data services are great and it is incredibly powerful but not as quick to refactor as I'd like. Doggo is my attempt to find a middle ground.

It is mostly HTML/CSS, but with Jinja templating to cut down on the copy and paste. Routing and data services are handled by a yaml file that defines the pages and data available to the application.

Why Doggo? The root idea behind it is the concept of the DoGo map (https://uxpamagazine.org/creating-a-dogo-map/). I have grown to really like the DoGo map as a way to think through the information architecture of a site. I think it makes a serviceable low fidelity clickable prototype.

To that end, the yaml file and default templates in Doggo are extremely rudimentary. They expose the parameters and allow the user to get something up and running with little fuss, without any attempt to trick the user into thinking the application is almost done.

The templates can be easily overridden to allow the user to increase the fidelity of the prototype.

The purpose of this is NOT to create a slick, production framework, but to get developers to prototype roughly and get something that they can use to gather feedback sooner in the process.

### Roadmap

Q1 2021
- [ ] Write a spec for the doggo yaml file
- [ ] Provide some better looking default and selectable templates
- [ ] Figure out a generic way to handle query strings to allow for data selection
- [ ] Create a web page for the project

The Future
- [ ] "Interactive Mode" that allows the user to define new cards & data
- [ ] "Doggo as a Service" - a deployed version of the application that allows users to create their own prototypes and share them (codepen-like functionality)
- [ ] "Whiteboard mode" - Miro or Plectica like interface for teams to define cards and data

Contributions welcome!
