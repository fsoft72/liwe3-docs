<a id="fs-unlink"></a>
## `unlink`


```ts
unlink = ( path: string ): void
```


Deletes a file if it exists.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `path` | string | The path to the file to delete. |



**Returns**: `{void}`

-----------------

<a id="fs-exists"></a>
## `exists`


```ts
exists = ( path: string ): boolean
```


Checks if a file or directory exists.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `path` | string | The path to the file or directory to check. |



**Returns**: `{boolean} `true` if the file or directory exists, `false` otherwise.`

-----------------

<a id="fs-isfile"></a>
## `isFile`


```ts
isFile = ( path: string ): boolean
```


Checks if a path is a file.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `path` | any | the |



**Returns**: `true if the path is a file`

-----------------

<a id="fs-isdirectory"></a>
## `isDirectory`


```ts
isDirectory = ( path: string ): boolean
```


Checks if a path is a directory.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `path` | any | the |



**Returns**: `true if the path is a directory`

-----------------

<a id="fs-mkdir"></a>
## `mkdir`


```ts
mkdir = ( dirname: string, mode: number = 0o755, recursive: boolean = true )
```


mkdir - creates a new directory



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `dirname` | any | directory name to be created |
| `mode` | any | [0o755] directory mode |
| `recursive` | any | [true] if missing sub dirs should be created. |



**Returns**: ``

-----------------

<a id="fs-rmdir"></a>
## `rmdir`


```ts
rmdir = ( dirname: string )
```


Deletes a directory if it exists.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `dirname` | string | The path to the directory to delete. |



**Returns**: `{void}`

-----------------

<a id="fs-rm"></a>
## `rm`


```ts
rm = ( fname: string )
```


Deletes a file if it exists.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `fname` | string | The path to the file to delete. |



**Returns**: `{void}`

-----------------

<a id="fs-readdir"></a>
## `readdir`


```ts
readdir = ( dirname: string ): string[]
```


Reads the contents of a directory.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `dirname` | string | The path to the directory to read. |



**Returns**: `{string[]} An array of filenames in the directory.`

-----------------

<a id="fs-read"></a>
## `read`


```ts
read = ( fname: string ): string
```


Reads the contents of a file.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `fname` | string | The path to the file to read. |



**Returns**: `{string} The contents of the file as a string.`

-----------------

<a id="fs-abspath"></a>
## `abspath`


```ts
abspath = ( rel_path: string ): string
```


Resolves a relative path to an absolute path.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `rel_path` | string | The relative path to resolve. |



**Returns**: `{string} The absolute path.`

-----------------

<a id="fs-rename"></a>
## `rename`


```ts
rename = ( old_path: string, new_path: string ): void
```


Renames a file or directory.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `old_path` | string | The path to the file or directory to rename. |
| `new_path` | string | The new path for the file or directory. |



**Returns**: `{void}`

-----------------

<a id="fs-move"></a>
## `move`


```ts
move = ( old_path: string, new_path: string ): boolean
```


move ( old_path, new_path ) => void

Moves a file from ``old_path`` to ``new_path``.

This function first tries using `rename` function. If it cannot be used, then the file is copied and removed.


@see rename


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `old_path:` | any |  |
| `new_path:` | any |  |



**Returns**: ``

-----------------

<a id="fs-write"></a>
## `write`


```ts
write = ( full_path: string, data: string | Buffer ): void
```


Writes data to a file.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `full_path` | string | The path to the file to write to. |
| `data` | string | The data to write to the file. |



**Returns**: `{void}`

-----------------

<a id="fs-stat"></a>
## `stat`


```ts
stat = ( full_path: string )
```


Gets information about a file or directory.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `full_path` | string | The path to the file or directory to get information about. |



**Returns**: `{fs.Stats} An object containing information about the file or directory.`

-----------------

<a id="fs-basename"></a>
## `basename`


```ts
basename = ( full_path: string )
```


Gets the base name of a file or directory path.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `full_path` | string | The path to the file or directory. |



**Returns**: `{string} The base name of the file or directory.`

-----------------

<a id="fs-"></a>
## ``


```ts

```


@ignore
creates a temp file in the `full_path` given.
This function is sync.




**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `path` | any | the |
| `name` | any | the |
| `mode` | any | file |



**Returns**: `the full_path of the created file`

-----------------

<a id="fs-symlink"></a>
## `symlink`


```ts
symlink = ( src: string, dest: string ): void
```


Creates a symbolic link.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `src` | string | The path to the source file or directory. |
| `dest` | string | The path to the destination file or directory. |



**Returns**: `{void}`

-----------------

<a id="fs-createwritestream"></a>
## `createWriteStream`


```ts
createWriteStream = ( path: string, options: any )
```


Creates a write stream to the specified path with the given options.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `path` | any | The path to the file. |
| `options` | any | The options for creating the write stream. |



**Returns**: `The created write stream.`

-----------------

<a id="fs-sanitize"></a>
## `sanitize`


```ts
sanitize = ( filename: string )
```


Takes a filename and returns a sanitized version of it.
By default, it replaces all non-alphanumeric characters with underscores and converts to lowercase.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `filename` | string | The filename to sanitize. |



**Returns**: `{string} The sanitized filename.`

-----------------

<a id="fs-filesize"></a>
## `fileSize`


```ts
fileSize = ( path: string ): number
```


Returns the size of a file in bytes.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `path` | any | the |



**Returns**: `the size of the file in bytes`

-----------------

