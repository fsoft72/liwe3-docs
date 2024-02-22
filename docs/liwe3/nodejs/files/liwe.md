<a id="liwe-fsname"></a>
## `fsname`


```ts
fsname = ( path: string ): string
```


Returns the absolute path of a file or directory.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `path` | string | The path to the file or directory. |



**Returns**: `{string} The absolute path of the file or directory.`

-----------------

<a id="liwe-config-fullpath"></a>
## `config_fullpath`


```ts
config_fullpath = ( fname: string = '' ): string  fsname( `etc/config/$ fname }` );
```


Returns the full path of a configuration file.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `fname` | any | The |



**Returns**: `The full path of the configuration file.`

-----------------

<a id="liwe-template-fullpath"></a>
## `template_fullpath`


```ts
template_fullpath = ( modname: string, fname: string = '' ): string  fsname( `etc/templates/$ modname }/$ fname }` );
```


Returns the full path of a template file.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `modname` | any | The name of the module. |
| `fname` | any | The name of the template file (optional). |



**Returns**: `The full path of the template file.`

-----------------

<a id="liwe-upload-fullpath"></a>
## `upload_fullpath`


```ts
upload_fullpath = ( subpath: string = '' ): string  fsname( `static/public/uploads/$ subpath }` );
```


Returns the full path for uploading files.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `subpath` | any | The subpath to append to the upload directory. |



**Returns**: `The full path for uploading files.`

-----------------

<a id="liwe-public-fullpath"></a>
## `public_fullpath`


```ts
public_fullpath = ( subpath: string = '' ): string  fsname( `static/public/$ subpath }` );
```


Returns the full path for a public file or directory.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `subpath` | any | The subpath within the "static/public" directory. |



**Returns**: `The full path for the public file or directory.`

-----------------

<a id="liwe-temp-fullpath"></a>
## `temp_fullpath`


```ts
temp_fullpath = ( subpath: string = '' ): string  fsname( `static/temp/$ subpath }` );
```


Returns the full path for a temporary file or directory.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `subpath` | any | The subpath within the temporary directory. |



**Returns**: `The full path for the temporary file or directory.`

-----------------

<a id="liwe-server-fullpath"></a>
## `server_fullpath`


```ts
server_fullpath = ( subpath: string = '' ): string  fsname( `dist/server/$ subpath }` );
```


Returns the full path of the server file.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `subpath` | any | The subpath of the server file. |



**Returns**: `The full path of the server file.`

-----------------

<a id="liwe-module-fullpath"></a>
## `module_fullpath`


```ts
module_fullpath = ( subpath: string = '' ): string  fsname( `dist/server/modules/$ subpath }` );
```


Returns the full path of a module.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `subpath` | any | The |



**Returns**: `The full path of the module.`

-----------------

<a id="liwe-relative-fullpath"></a>
## `relative_fullpath`


```ts
relative_fullpath = ( fullpath: string = '' ): string
```


Returns the relative path of a given full path.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `fullpath` | any | The full path to convert to a relative path. |



**Returns**: `The relative path.`

-----------------

<a id="liwe-public-relative-path"></a>
## `public_relative_path`


```ts
public_relative_path = ( full_path: string = '' ): string  full_path.split( "/static/public" ).slice( -1 )[ 0 ];
```


Extracts the relative path from a full path by removing the "/static/public" prefix.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `full_path` | any | The |



**Returns**: `The relative path.`

-----------------

<a id="liwe-config-load"></a>
## `config_load`


```ts
config_load = ( fname: string = '', _default: any = }, show_error: boolean = false, raise_exception: boolean = false, path: string = 'etc/config' ): any
```


Loads a configuration file from the specified path.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `[fname='']` | string | The name of the configuration file to load. |
| `[_default={}]` | * | The default value to return if the configuration file is not found. |
| `[show_error=false]` | boolean | Whether to log an error message to the console if the configuration file is not found. |
| `[raise_exception=false]` | boolean | Whether to throw an exception if the configuration file is not found. |
| `[path='etc/config']` | string | The path to the directory containing the configuration files. |



**Returns**: `{*} The parsed configuration object.`

-----------------

<a id="liwe-module-config-load"></a>
## `module_config_load`


```ts
module_config_load = ( modname: string, _default: any = }, show_error: boolean = false, raise_exception: boolean = false ): any
```


Loads the configuration for a module.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `modname` | any | The name of the module. |
| `_default` | any | The default configuration to use if the module configuration is not found. |
| `show_error` | any | Whether to show an error message if the module configuration is not found. |
| `raise_exception` | any | Whether to raise an exception if the module configuration is not found. |



**Returns**: `The configuration object for the module.`

-----------------

<a id="liwe-make-default-dirs"></a>
## `make_default_dirs`


```ts
make_default_dirs = ( fullpath: string ): void
```


Creates the default directories if they do not exist.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `fullpath` | any | The full path of the directory. |



**Returns**: ``

-----------------

<a id="liwe-callback-load"></a>
## `callback_load`


```ts
callback_load = ( modulename: string, cback_name: string, default_cback: any, report_errors: boolean = true )
```


Loads a callback function from a module.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `modulename` | any | The name of the module. |
| `cback_name` | any | The name of the callback function. |
| `default_cback` | any | The default callback function to use if the specified callback is not found. |
| `report_errors` | any | Indicates whether to report errors or not. Default is true. |



**Returns**: `The loaded callback function or the default callback function if not found.`

-----------------

<a id="liwe-str-valid:"></a>
## `str_valid: ( t: string ): boolean`


```ts
str_valid: ( t: string ): boolean
```


Utility functions for string validation, checking emptiness, and key existence in objects.
Checks if a given value is a valid string.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `t` | any | The value to be checked. |



**Returns**: `True if the value is a non-empty string, false otherwise.`

-----------------

<a id="liwe-is-empty:"></a>
## `is_empty: ( t: any ): boolean`


```ts
is_empty: ( t: any ): boolean
```


Checks if a given value is empty.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `t` | any | The value to be checked. |



**Returns**: `True if the value is an empty object or an empty string, false otherwise.`

-----------------

<a id="liwe-has-key:"></a>
## `has_key: ( t: any, key: string ): boolean`


```ts
has_key: ( t: any, key: string ): boolean
```


Checks if a given object has a specific key.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `t` | any | The object to be checked. |
| `key` | any | The key to be checked. |



**Returns**: `True if the object has the specified key, false otherwise.`

-----------------

