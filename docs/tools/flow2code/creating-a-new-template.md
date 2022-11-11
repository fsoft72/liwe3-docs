# Creating a new template

`flow2code` uses a set of templates to generate the code skeleton (*hexocode*). The templates are written in [Python](https://www.python.org/){target=_blank} and are stored in the `templates` folder.

Template creation can be an easy task, but also an advanced one. It depends on the complexity of the codebase you want to generate. In this section, we will explain how to create a new template.

## Main concepts

Your template class will inherit from `TemplateBase` class, that offers some useful methods to help you in the creation of your template. The `TemplateBase` class is defined in `template_base.py` file in `lib` folder.

The `TemplateBase` is mainly responsible for reading the LiWE Flow JSON file and converting it into woking Python objects, so you don't have to worry about it. It also offers some useful methods to help you in the creation of your template.

To see all the `TemplateBase` methods, please, see the [TemplateBase API](./liwe3/tools/flow2code/template-base-api.md).

To see all the Flow2Code Types, please, see the [Flow2Code API](./liwe3/tools/flow2code/flow2code-types.md).

## Creating a new template

The most basic Template, should be composed by these files:

- a directory with the name of your template, in `templates` folder
- a `__init__.py` file in the template directory
- a `template.py` file in the template directory

The `template.py` file is the main file for a new template, and the **only** file mandatory for `flow2code` to work.
Inside the `template.py` you should have a class `Template` that inherits from `TemplateBase` and implements the `code` method.
The `code()` method is the entry point of your template. It will be called by the `flow2code` tool.

So, the template structure should be like this:

```bash
templates/
└── my_template
	├── __init__.py
	└── template.py
```

And the most basic `Template` class should be like this:

```python
#/usr/bin/env python3

import os

from lib.template_base import TemplateBase

class Template(TemplateBase):
	def code ( self, mod: Module, flow: any, output: str ):
		super().code( mod, flow, output )

		# start your template logic from here
```

After the call to the `super().code()` method, you can start your template logic. The `mod` parameter is a `Module` object, that contains all the information about the module you want to generate. The `flow` parameter is the LiWE Flow JSON file, that will be converted into Python objects in memory from the `TemplateBase`. The `output` parameter is the base path where the generated code will be stored.