# TemplateBase API

These are the public methods of the TemplateBase class.

## Attributes

- `snippets`: A dictionary of snippets extracted by reading your previously generated file

## Methods

### `create_file()`

```python
create_file ( self, full_path: str, mod: Module, keep_all_snippets: bool = False ):
```

This method creates a new output file
It also creates all the missing directories and extract snippets from the file if it exists.

Parameters:

	- `full_path`: The full path of the file to create
	- `mod`: The module that is being processed
	- `keep_all_snippets`: If true, all snippets read in previous runs will be kept. If false, only the snippets that are in the current file will be kept.

See also: [extract_snippets()](#extract_snippets)

-----




### `endpoint_mk_function()`

```python
endpoint_mk_function ( self, ep: Endpoint ):
```

This method returns the Endpoint unique function name, composed by the endpoint name and the method.

See also: [valid_function_name()](#valid_function_name)

--------



### `extract_snippets()`
```python
extract_snippets ( self, mod: Module, fname: str )
```
Extracts all the code you have written in the file `fname` and stores it in the `snippets` dictionary.
The code extracted is the one between the `f2c_start` and `f2c_end` comments.

See [Populating the Hexocode](hexocode.md) for more information.

Parameters:

- `mod`: The current Module we are working on
- `fname`: The name of the file to be read and parsed

!!! note

	You usually do not call this method directly, but it is implicitly called with the [create_file()](#create_file) method.

-------

 ### `join_newlines()`

```python
join_newlines ( self, lst: list[str], num_elems: int = 5 ) -> str:
```

This is a helper method that joins a list of strings into a single string, with a newline character between every `num_elems` elements.
This is very useful when you want to create a list of imports, for example.

-------

### `mk_documentation()`

```python
mk_documentation ( self, main_doc: str, params_doc: list[str], ret_name: str, ret_type: str, ret_doc: str, TEMPL: dict[str,str] ) -> str:
```

This method creates the documentation string from the parameters passed.

Parameters:

- `main_doc`: The main documentation string.
- `params_doc`: A list of strings, each of which is a parameter documentation string.
- `ret_name`: The name of the return value.
- `ret_type`: The type of the return value.
- `ret_doc`: The documentation string for the return value.
- `TEMPL`: A dictionary of strings, each of which is a template for a parameter documentation string.

See also: [params_and_doc()](#params_and_doc)

-------

### `mod_name()`

```python
mod_name ( self, mod: Module )
```

Returns the name of the module in `snake_case` format.


-------

### `params_and_doc()`

```python
params_and_doc ( self, fn: Endpoint | Function, TEMPL: dict[str,str], honour_float: bool = True ) -> tuple[list[str],list[str]]:
```

This method returns a tuple with two elements:

- A list of strings, each of which is a parameter declaration string.
- A list of strings, each of which is a parameter documentation string.

Parameters:

- `fn`: The function or endpoint to be documented.
- `TEMPL`: A dictionary of templates.
- `honour_float`: If `True`, the `float` type will be treated as `float`.

See also: [mk_documentation()](#mk_documentation)

-------

### `prepare_field()`

```python
prepare_field ( self, field: Field, template: str, template_obj: str, honour_float: bool = False, use_enums: bool = False ) -> str:
```

This method applies the `template` or `template_obj` to the field, depending on the type of the field, and returns a string with the result.

Parameters:
	- `field`: The field to be used to create the string.
	- `template`: The template to use.
	- `template_obj`: The template to use for objects.
	- `honour_float`: If `True`, the `float` types will be kept, if `False`, they will be converted to `int`.
	- `use_enums`: If `True`, the `template` will use Enums instead of strings.

-------

### `valid_function_name()`
```
valid_function_name ( self, name: str )
```

Returns the passed `name` as a valid function name, stripping all the invalid characters