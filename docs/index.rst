.. Doggo documentation master file, created by
   sphinx-quickstart on Sun Jan 31 20:40:59 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Doggo's documentation!
=================================
I like prototyping in software. Usually I use straight HTML/CSS or Angular, depending on the complexity of the application.

HTML/CSS can be too fiddly and have too much copy and paste. Angular is, well, Angular. Routing and data services are great and it is incredibly powerful but not as quick to refactor as I'd like. Doggo is my attempt to find a middle ground.

It is mostly HTML/CSS, but with Jinja templating to cut down on the copy and paste. Routing and data services are handled by a yaml file that defines the pages and data available to the application.

Why Doggo? The root idea behind it is the concept of the DoGo map (https://uxpamagazine.org/creating-a-dogo-map/). I have grown to really like the DoGo map as a way to think through the information architecture of a site. I think it makes a serviceable low fidelity clickable prototype.

To that end, the yaml file and default templates in Doggo are extremely rudimentary. They expose the parameters and allow the user to get something up and running with little fuss, without any attempt to trick the user into thinking the application is almost done.

The templates can be easily overridden to allow the user to increase the fidelity of the prototype.

The purpose of this is NOT to create a slick, production framework, but to get developers to prototype roughly and get something that they can use to gather feedback sooner in the process.

Roadmap
-------

Q1 2021
^^^^^^^

* Write a spec for the doggo yaml file
* Provide some better looking default and selectable templates
* Figure out a generic way to handle query strings to allow for data selection
* Create a web page for the project

The Future
* "Interactive Mode" that allows the user to define new cards & data
* "Doggo as a Service" - a deployed version of the application that allows users to create their own prototypes and share them (codepen-like functionality)
* "Whiteboard mode" - Miro or Plectica like interface for teams to define cards and data

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
