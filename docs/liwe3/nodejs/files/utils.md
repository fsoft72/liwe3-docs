<a id="utils-recaptcha-check"></a>
## `recaptcha_check`


```ts
recaptcha_check = async ( captcha: string )
```


Checks the validity of a reCAPTCHA response.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `captcha` | any | The |



**Returns**: `A Promise that resolves to the reCAPTCHA verification result.`

-----------------

<a id="utils-md5"></a>
## `md5`


```ts
md5 = ( txt: string, do_check: boolean = true )
```


This function converts ``txt`` into an MD5 string.
If ``do_check`` is true, the original string is checked against a Regular Expression to
verify if it is already an MD5 string, and (in that case) it is just returned without hashing.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `txt` | any | The |
| `do_check` | any | If |



**Returns**: ``

-----------------

<a id="utils-md5file"></a>
## `md5File`


```ts
md5File = ( fname: string ): string
```


Calculates the MD5 hash of a file.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `fname` | any | The path to the file. |



**Returns**: `The MD5 hash of the file.`

-----------------

<a id="utils-sha512"></a>
## `sha512`


```ts
sha512 = ( txt: string, do_check: boolean = true )
```


Calculates the SHA512 hash of a given string.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `txt` | any | The string to be hashed. |
| `do_check` | any | Optional. Specifies whether to check if the input string is already a valid SHA512 hash. Default is true. |



**Returns**: `The SHA512 hash of the input string.`

-----------------

<a id="utils-send-error"></a>
## `send_error`


```ts
send_error = ( res: express.Response, error: any, error_code: number = 400 )
```


This function returns an error to Express




**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `req	The` | any | Express |
| `error` | any | an |
| `error_code` | any | the |



**Returns**: ``

-----------------

<a id="utils-send-ok"></a>
## `send_ok`


```ts
send_ok = ( res: express.Response, payload: any, status_code: number = 200 )
```


This function is used when an Express request succedees




**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `res` | any | the |
| `payload` | any | the |
| `status_code` | any | the |



**Returns**: ``

-----------------

<a id="utils-send-html"></a>
## `send_html`


```ts
send_html = ( res: express.Response, payload: string, status_code: number = 200 )
```


This function returns a simple HTML instead of the standard JSON returned by send_ok()



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `res` | any | the |
| `payload` | any | the |
| `status_code` | any | the |



**Returns**: ``

-----------------

<a id="utils-send-binary"></a>
## `send_binary`


```ts
send_binary = ( res: express.Response, buffer: any, content_type: string, filename: string )
```


Sends a binary response with the specified buffer, content type, and filename.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `res` | any | The express response object. |
| `buffer` | any | The binary buffer to send. |
| `content_type` | any | The content type of the response. |
| `filename` | any | The filename for the attachment. |



**Returns**: ``

-----------------

<a id="utils-rand-int"></a>
## `rand_int`


```ts
rand_int = ( min: number = 0, max: number = 100 ): number
```


Generates a random integer number from `min` to `max`



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `min` | any | Random |
| `max` | any | Random |



**Returns**: `an integer between the specified min / max range`

-----------------

<a id="utils-unique-code"></a>
## `unique_code`


```ts
unique_code = ( simple: boolean = true, prefix: string = null, second_slice: boolean = true ): string
```


Generates an unique string code (up to 37 chars long)



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `simple	If` | any | the |
| `prefix	The` | any | prefix |
| `second_slice	If` | any | a |



**Returns**: `the unique string generated`

-----------------

<a id="utils-unique-code-numbers"></a>
## `unique_code_numbers`


```ts
unique_code_numbers = ( length: number, second_slice: number = 0 ): string
```


Generates a unique code number string based on the current timestamp.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `length` | number | The length of the code number string to generate. |
| `[second_slice=0]` | number | The length of the second slice to append to the code number string. |



**Returns**: `{string} - The unique code number string.`

-----------------

<a id="utils-mkid"></a>
## `mkid`


```ts
mkid = ( prefix: string, ext?: string )
```


@description This function returns an unique id, the id starts with the prefix and can optionally contain an extension


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `prefix` | any | The prefix to add to the string |
| `ext` | any | The extension to add to the string |



**Returns**: ``

-----------------

<a id="utils-random-string"></a>
## `random_string`


```ts
random_string = ( length: number = 4, iterations: number = 20, numeric: boolean = false ): string
```


returns a random string of specified ``length`` using a randomizer of ``iterations``.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `length:` | any |  |
| `iterations:` | any | the |



**Returns**: `the created random string`

-----------------

<a id="utils-fetch-file"></a>
## `fetch_file`


```ts
fetch_file = ( url: string, dest_local_path: string )
```


Fetch a file from the given `url` into `dest_local_path`



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `url` | any |  |
| `dest_local_path` | any | The |



**Returns**: ``

-----------------

<a id="utils-jwt-crypt"></a>
## `jwt_crypt`


```ts
jwt_crypt = ( payload: any, secret: string, expires: number ): string
```


Generates a JWT token with the provided payload, secret, and expiration time.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `payload` | any | The data to be included in the token. |
| `secret` | any | The secret key used to sign the token. |
| `expires` | any | The expiration time for the token in seconds. |



**Returns**: `The generated JWT token.`

-----------------

<a id="utils-jwt-decrypt"></a>
## `jwt_decrypt`


```ts
jwt_decrypt = ( tok: string, secret: string ): any
```


Decrypts a JWT token using the provided secret.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `tok` | any | The JWT token to decrypt. |
| `secret` | any | The secret used to decrypt the JWT token. |



**Returns**: `The decrypted payload if the token is valid, otherwise null.`

-----------------

<a id="utils-delete-folder"></a>
## `delete_folder`


```ts
delete_folder = ( path: string ): void
```


Deletes a folder and all its contents recursively.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `path` | any | The path of the folder to delete. |



**Returns**: ``

-----------------

<a id="utils-shell"></a>
## `shell`


```ts
shell = async ( command: string, cback: any )
```


Executes a shell command asynchronously.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `command` | any | The shell command to execute. |
| `cback` | any | Optional callback function to handle the result or error. |



**Returns**: `A promise that resolves with the result of the command or rejects with an error.`

-----------------

<a id="utils-progressive-fetch-file"></a>
## `progressive_fetch_file`


```ts
progressive_fetch_file = ( url: string, update_cback: any, end_cback: any, err_cback: any )
```


Download the file specified by the given ``url`` using progressive events

The function gets 3 cbacks:

- update_cback ( chunk, perc, size, total )

- chunk:  the chunk to write     ( eg. fs.syncWrite ( fd, chunk, 0, chunk.len ) );
- perc:   the percentual of the file downloaded (float)
- size:   the size (in MB) of the file downloaded
- total:  total size in MB

- end_cback ()

This cback is called at the end of the download

- err_cback ( err )

This cback is called when something goes wrong





**Returns**: ``

-----------------

<a id="utils-template-render"></a>
## `template_render`


```ts
template_render = ( template_full_path: string, dct: object ): string
```


Renders a template file with Handlebars syntax




**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `template_full_path` | str | Full path for the file containing the template |
| `dct` | object | An object with all key / values needed |



**Returns**: ``

-----------------

<a id="utils-typed-dict"></a>
## `typed_dict`


```ts
typed_dict = ( dct: any, fields_descr: IFieldDescr[] )
```


Converts a dictionary object into a typed object based on the provided field descriptions.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `dct` | any | The |
| `fields_descr` | any | The |



**Returns**: `The typed object with converted values and error information.`

-----------------

<a id="utils-const-isvaliddate"></a>
## `const isValidDate`


```ts
const isValidDate = ( d: Date ): boolean  !isNaN( d.getTime() );
```


Checks if a given date is valid.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `d` | any | The date to be checked. |



**Returns**: `A boolean indicating whether the date is valid or not.`

-----------------

<a id="utils-date-format"></a>
## `date_format`


```ts
date_format = ( date: any, format = 'yyyy-mm-dd HH:MM:SS' ): string
```


converts a date into a string with the desired format

yyyy - year
mm  - month
dd  - day

HH - hour
MM - minutes
SS - seconds





**Returns**: ``

-----------------

<a id="utils-isvalidemail"></a>
## `isValidEmail`


```ts
isValidEmail = ( email: string ): boolean
```


Checks if the given email is valid.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `email` | any | The email to be validated. |



**Returns**: `True if the email is valid, false otherwise.`

-----------------

<a id="utils-int"></a>
## `int`


```ts
int = ( s: any ): number
```


Converts the input value to an integer.
If the input value is falsy or undefined, returns 0.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `s` | any | The value to convert to an integer. |



**Returns**: `The converted integer value.`

-----------------

<a id="utils-float"></a>
## `float`


```ts
float = ( s: any ): number
```


Converts a value to a floating-point number.
If the value is falsy, returns 0.0.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `s` | any | The value to convert. |



**Returns**: `The converted floating-point number.`

-----------------

<a id="utils-keys-remove"></a>
## `keys_remove`


```ts
keys_remove = ( obj: any, keys: string[] )
```


remove keys specified by `keys` in `obj`
This is a 'change in place' function.
The object is modified in memory





**Returns**: ``

-----------------

<a id="utils-set-attr"></a>
## `set_attr`


```ts
set_attr = ( obj: any, field_name: string, val: any )
```


sets an attribute to `obj` only if `val` is not undefined.





**Returns**: ``

-----------------

<a id="utils-set-attrs"></a>
## `set_attrs`


```ts
set_attrs = ( obj: any, data: any )
```


sets multiple attributes to  `obj` only if `val` is not undefined.





**Returns**: ``

-----------------

<a id="utils-keys-filter"></a>
## `keys_filter`


```ts
keys_filter = ( obj: any, type_def: any )
```


Filters the keys of an object `obj` based on the
specified fields in `type_def`.
If a key is not in `type_def`, it is removed from `obj`.





**Returns**: ``

-----------------

<a id="utils-get-date"></a>
## `get_date`


```ts
get_date = ( d: Date ): string
```


Returns a date in international format 'YYYY-MM-DD'





**Returns**: ``

-----------------

<a id="utils-list-add"></a>
## `list_add`


```ts
list_add = ( lst: string[], el: string )
```


adds a new element (el) to a string list (lst)
only if `el` does not exists in `lst`




**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `lst	the` | any | string |
| `el	element` | any | to |



**Returns**: `the new modified list`

-----------------

<a id="utils-list-del"></a>
## `list_del`


```ts
list_del = ( lst: string[], el: string )
```


removes an element (el) from the list (lst)




**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `lst	the` | any | string |
| `el	element` | any | to |



**Returns**: `the new modified list`

-----------------

<a id="utils-keys-valid"></a>
## `keys_valid`


```ts
keys_valid = ( dct: any )
```


returns a new object with only the keys that are not undefined




**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `dct	the` | any | object |



**Returns**: `a new object with valid keys`

-----------------

<a id="utils-export-function-isobject"></a>
## `export function isObject ( item: any )`


```ts
export function isObject ( item: any )
```


Simple object check.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `item` | any |  |



**Returns**: `{boolean}`

-----------------

<a id="utils-export-function-merge"></a>
## `export function merge ( target: any, ...sources: any[] ): any`


```ts
export function merge ( target: any, ...sources: any[] ): any
```


Deep merge two objects.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `target` | any |  |
| `...sources` | any |  |



**Returns**: ``

-----------------

<a id="utils-list-random-pick"></a>
## `list_random_pick`


```ts
list_random_pick = ( lst: any[] )
```


Picks a random element from the given list.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `lst` | any | The list to pick from. |



**Returns**: `The randomly picked element from the list.`

-----------------

<a id="utils-list-random-pick-n"></a>
## `list_random_pick_n`


```ts
list_random_pick_n = ( lst: any[], n: number )
```


Picks n random elements from the given list.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `lst` | any | The list from which to pick random elements. |
| `n` | any | The number of random elements to pick. |



**Returns**: `An array containing n random elements from the list.`

-----------------

<a id="utils-challenge-create"></a>
## `challenge_create`


```ts
challenge_create = ( params: string[], debug = false )
```


takes a list of strings and returns a valid challenge





**Returns**: ``

-----------------

<a id="utils-challenge-check"></a>
## `challenge_check`


```ts
challenge_check = ( challenge: string, params: string[] ): boolean
```


takes a list of strings and check it agains the provided challenge




**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `challenge	the` | any | challenge |
| `params	the` | any | list |



**Returns**: `true if the challenge is valid`

-----------------

<a id="utils-slugify"></a>
## `slugify`


```ts
slugify = ( str: string )
```


Converts a string into a slug by removing special characters, converting to lowercase, and replacing spaces with dashes.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `str` | any | The string to be slugified. |



**Returns**: `The slugified string.`

-----------------

<a id="utils-decimaltobase96"></a>
## `decimalToBase96`


```ts
decimalToBase96 = ( decimal: number ): string
```


Converts a decimal number to a base-96 string representation.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `decimal` | any | The |



**Returns**: `The base-96 string representation of the decimal number.`

-----------------

<a id="utils-base96todecimal"></a>
## `base96ToDecimal`


```ts
base96ToDecimal = ( base96: string ): number
```


Converts a base96 number to decimal.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `base96` | any | The base96 number to convert. |



**Returns**: `The decimal representation of the base96 number.`

-----------------

<a id="utils-formatcurrency"></a>
## `formatCurrency`


```ts
formatCurrency = ( number: number,  thousandSeparator = '.', decimalSeparator = ',' } = } ): string
```


Formats a number as a currency string.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `number` | any | The number to format. |
| `options` | any | Optional formatting options. |
| `options.thousandSeparator` | any | The character used as a thousand separator. Default is '.'. |
| `options.decimalSeparator` | any | The character used as a decimal separator. Default is ','. |



**Returns**: `The formatted currency string.`

-----------------

