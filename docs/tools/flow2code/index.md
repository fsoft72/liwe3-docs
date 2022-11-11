# Flow2Code

`flow2code` is a tool that allows you to create a code skeleton (**hexocode**) from a [LiWE Flow](./liwe3/tools/flow.md) file.

`flow2code` uses a set of templates to generate the code skeleton. The templates are written in [Python](https://www.python.org/){target=_blank} and are stored in the `templates` folder.

You can create your own templates for your codebase and style and use them with `flow2code`. To know how to create a new template, please, see [Creating a new template](./liwe3/tools/flow2code/creating-a-new-template.md).

## Usage

`flow2code` is a command line tool that can be used in this way:

```bash
flow2code.py <flowfile> -t template_name -o output_folder  [--strict]
```

Where:
```
<flowfile> - the path to the flow file
-t template_name - the name of the template to use
-o output_folder - the folder where to save the generated code
--strict - if set, the tool will fail if a something is not found during the generation
```

The full commands are:

```bash
usage: flow2code.py [-h] [-o OUTPUT] [-t TEMPLATE] [--strict] [-v] flow

Convert a flow file to Code using a template

positional arguments:
  flow                  Flow file to convert

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output directory
  -t TEMPLATE, --template TEMPLATE
                        Template file
  --strict              Strict mode
  -v, --version         show program's version number and exit
```
