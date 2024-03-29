# restest
## The command line REST tester

`restest` is a powerful command line tool for testing REST APIs.
Tests are defined in one or more JSON files, and can be run against any REST API.

With `restest` you can control return responses and test values against an expected result / behaviour and also manipulate headers, cookies and call parameters.

Since it is a command line tool, it can be used in a CI/CD pipeline to test your API.

## Main Features

Main features of `restest` are:

- Support session based request
- Powerful path parser to extract keys in nested JSON structures
- Output of a complete `curl` command for each request
- Dump of all headers and fields
- Supports Token authentication
- Support values extracting, storing and reusing during the script
- Data manipulation using Python string formatting rules to create custom strings and values
- Support for multiple test files
- Ability to dump machine status and load it back
- Macros to simplify test definition
- [Postman](https://postman.com){target=_blank} collection export
- Clean debug output

## Installation

Just download the latest version from the [release page](https://github.com/fsoft72/restest/releases){target=_blank} and extract the archive in a folder of your choice.

!!! note
	`restest` requires Python 3.10.

## How to run it

Typically you run `restest` from a command line with some parameters and one or more JSON files with the tests to be performed.

In its simplest form, you can run `restest` with just a single file as argument, like this:

```bash
restest examples/typicode.example.json
```

but `restest` offers many more options, like:

```bash
~/src/restest$ restest --help
positional arguments:
  file                  Files containing the tests

options:
  -h, --help            show this help message and exit
  --base-url BASE_URL   Base URL. This string overrides the 'system' parameter in JSON file
  --curl                Dumps CURL also on console (defaults on log only
  --dry                 If set, no request is done for real
  --dont-stop-on-error  Flag to stop RESTest on error. This flag overrides the 'system' parameter in
                        JSON file
  --env                 If set, global vars will contain also environment variables
  --env-load ENV_LOAD   If set, global vars will be loaded from the specified file
  --env-save ENV_SAVE   If set, global vars will be saved to specified file
  --no-colors           If set, colors in console output are disabled
  --postman POSTMAN     Export activity to a Postman JSON file
  --postman-name POSTMAN_NAME
                        The Postman Collection name
  --postman-base-url POSTMAN_BASE_URL
                        The base url to use in Postman instead of the real host
  --postman-auth-name POSTMAN_AUTH_NAME
                        Name of the authorization header name
  --postman-auth-value POSTMAN_AUTH_VALUE
                        Value to use for authorization header
  --key KEY [KEY ...]   One or more keys to be added to the globals dict use key:value format
  --log LOG             Custom log file overriding the one in 'system'
  --quiet               If set, no output on console
  -v, --version         show program's version number and exit
  --delay DELAY         Delay in milliseconds between requests
  --prefix PREFIX       The API prefix URL
```


## JSON file structure

`restest` uses a JSON file to define the tests to be performed, the main and most important section of the JSON file is the `actions` section, which contains the list of actions to be performed.

Actions can be of two types:

- a **request action**, which is a request to be performed against the API
- an **insternal script** action which is related to `restest` internal behaviour

**Request actions** are the most important part of the JSON file, and they contain the `method` and `url` keys to define the request to be performed.

**Internal script** actions are used to control the behaviour of `restest` and contain the `action` key to define the action to be performed.

Every action **must** contain a `method` or `action` key.

If the `method` key is present, then the action is actually a `http`/`https` request.

If the `action` key is present, then the action is a *script* command.


### The simplest example

This is the smaller JSON file for `restest` you can write
(note: name it `simple-example.test.json`):
```json
{
	"actions": [
		{
			"method": "get",
			"url": "/api/your/url/hello-world"
		}
	]
}
```

In this example, the JSON file is created with just one single action that will do a GET request to the `/api/your/url/hello-world` URI.
As you can see, the URI is incomplete, as it misses the `http`/`https` part. Don't worry: you can specify it in the command line.
Specifying using the command line allows you to run the same tests on different URLs (for example, development and production environments).

Here is the shortest command line to execute the script above:

```bash
restest --base-url http://example.com simple-example.test.json
```


## ACTION description for HTTP requests

### `title`

Every action can have a *title* field. The text included in this field will be shown on console. Useful to tell the user what's going on.

### `method`

Supported `method` modes:

- **GET** the `HTTP GET` method
- **POST** the `HTTP POST` method
- **PUT** the `HTTP PUT` method
- **PATCH** the `HTTP PATCH` method
- **DELETE** the `HTTP DELETE` method

Currently, other `HTTP` methods are not supported, but planned in the future.

### `url`

The partial URL to call. As you have seen before, you can specify the base URL with the `--base-url` command line argument.

### `auth`

This is a `true` / `false` flag which determines if the current call is authenticated. Default is **`false`**

### `content`

Defines the request content-type and mode. Possible values are:
- **json**  the request is a `application/json`  (*default*)
- **form**  the request is a `application/x-www-form-urlencoded`

### `ignore_error`

This is a `true` / `false` flag which determines if `restest` should ignore an error occurring on this request.
Default is **`true`**

### `status_code`

With `status_code` key you can specify the `HTTP Status Code` you expect the call to return.
For example, if you make an unauthorized call to a specific endpoint, it should return a `403 Unauthorized` return code.
If you do *not* specify `status_code` key and your request returns a `403`, then `restest` will return an error, but if you know *for sure* that
your request is going to fail with a `403` return code, then you can specify it with:
```json
"status_code": 403
```
And the `restest` action will succeed.

Default value for `return_code` is **`200`**

### `params`

If the request has parameters, you can specify them with the `params` keyword and passing an array.
Here there is an example:
```json
{
	"method": "post",
	"url": "/api/site/login",
	"params": {
		"email": "john.doe@example.com",
		"password": "mypassword"
	}
}
```

if the request is a `POST` request, parameters will be sent in post data, if it is a `GET` request, parameters will be added to the `url` with the classic `name=value&` format, correctly escaped.

### `headers`

If the request needs custom  headers, you can add them with the `headers` keyword.
Provided headers are not manipulated in any way (so, be carefull with uppercase and lowercase letters).
You can add the usual *variable escape* feature in the `value` field of your headers.

**NOTE 1**: headers can only contain `string` values.

**NOTE 2**: authentication headers are still handled with the `auth` keyword.

**NOTE 3**: if you have the same header key in both `global_headers` and `headers`, the value from `headers` will be used for this call.

```json
{
	"method": "post",
	"url": "/api/site/login",
	"params": {
		...
	},
	"headers": {
		"X-Header1": "header 1",
		"X-Custom": "%(custom_value)s"
	}
}
```


### `files`

If the action is a `post` request, you can specify `files` keyword, passing an array of files to be posted.
Here there is an example:
```json
{
	"method": "post",
	"url": "/api/site/files",
	"files": {
		"file1": "relative/path/to/file.txt",
		"file2": "/absolute/path/to/file.jpg"
	}
}
```

### `no_cookies`

This is a `true` or `false` flag. If set to `true` the cookies will not be sent or read during this single request.


### `max_time`

You can have a test failing when the request exceedes a certain amount of time defined by `max_time`.
`max_time` is set in milliseconds, so if you want to fail after one second, set it to `1000`.

### `fields`

The `fields` section allows you to collect values from the response and to *save* them inside `restest` to future use.
It is a list of field names that can be also "mapped" to a new name in memory while saving. You can specify both *string* (to save the key / value in memory *as is* without name modification) or a *list* with two fields `[ orig_name, new_name ]`.

**NOTE**: Field extraction supports dotted notation for nested objects.

Here there is a code snippet. Suppose the response is a JSON object like this one:

```json
{
	"auth_token": "jajsj3ijssisiej",
	"user": {
		"id": "abc123",
		"username": "johndoe"
	}
}
```

You could save `auth_token` as is and remap `user.id` into `user_id` in this way:

```json
"fields": [
	"auth_token",
	[ "user.id", "user_id" ]
]
```

### `tests`

The `tests` section allows you to run tests against the request response.
It contains an array of tests structured in this way:

- `title` (optional) a title of the running test
- `field` is the name of the field to run the test against. Field can be one of the following:
    - an attribute name of the returned object (eg. `email`)
	- if the field is a list of values (eg, `tags: [ 'hello', 'world' ]`) you can instruct to check against a specific value using the `[]` square notation. For example: `tags[0]` will be `hello` and `tags[1]` will be `world`.
	Square notations also work when the returned object is just an array. In this case, omit the field name (since there isn't any) and just go for `[0]` or `[1]` and so on.
	- the field name can use dotted notation to access an inner field. There is no limit to the nested field notation. Examples: `user.email` or `user.address.location.lat`

- `value` is the expected value
- `mode` is how to test the `field` value against the provided `value`. You can use one of those conditions (if omitted, default is `EQUALS`):
	- `EQUALS` or `=` or `==`:  the `value` must be exactly the same as the value contained in `field`
	- `EMPTY` or `IS_EMPTY` or `IS_NULL` or `NULL`: the `value` must not exists
	- `EXISTS` or `!!`: the `field` is present in the returned object
	- `CONTAINS` or `->`: the `value` must be present *inside* the `field` value
	- `SIZE` or `LEN` or `LENGTH`: the `field` object (eg. array or string) must be of the size defined in `value`
	- `GT` or `>`: the `field` value must be greater than `value`
	- `GTE` or `>=`: the `field` value must be greater than or equal to `value`
	- `LT` or `<`: the `field` value must be lesser than `value`
	- `LTE` or `<=`: the `field` value must be lesser than or equal to `value`
	- `NOT_NULL` or `IS_NOT_NULL`: the `field` value must exist
	- `NOT_EQUAL` or `!=` or `<>`: the `field` value must be different to `value`
	- `SIZE-GT` or `()>`: the `field` value is an array or string with a size greater than `value`
	- `SIZE-GTE` or `()>=`: the `field` value is an array or string with a size greater than or equal to `value`
	- `SIZE-LT` or `()<`: the `field` value is an array or string with a size lesser than `value`
	- `SIZE-LTE` or `()<=`: the `field` value is an array or string with a size lesser than or equal to `value`
	- `OBJ` or `OBJECT`: the `field` value is an object that must match the object specified in `value`

Here there is an example of two tests, the first one is checking if the first element in array has `id` equal to 1.
The second checks if the second user in the array has the username `Antonette`.
```json
"tests": [
	{
		"title": "Checking for id=1 on first user",
		"field": "[0].id",
		"value": 1
	},
	{
		"title": "Checking for right name on second user",
		"field": "[1].username",
		"value": "Antonette"
	}
]
```

# Path declarations

During tests or variable extraction, sometimes it is important to be able to access a nested value in the returning JSON object.

`restest` offers a very powerful path parser, that will help you reaching the node you want inside your structure. Let's see some examples.
First of all, suppose that the JSON returning is similar to this one:

```json
{
	"user": {
		"email": "user@example.com",
		"id": 123,
		"perms": [
			"admin",
			"superuser"
		]
	},
	"preferences": [
		{
			"name": "color",
			"value": "blue"
		},
		{
			"name": "avatar",
			"value": 1204
		},
		{
			"name": "children",
			"value": [
				{
					"name": "child01",
					"value": 1
				},
				{
					"name": "child02",
					"value": 2
				}
			]
		}
	]
}
```

Here there are some path examples:

- `"user.email"`	- returns the value of the field `email` (`user@example.com` in this example)
- `"user.perms.[0]"` - returns the first element of the perms array (`admin` in this example)
- `"preferences.[name=avatar]"` - returns the object that has `avatar` in `name` field inside `preferences`
- `"preferences.[name=children].value[value!=2]"` - returns the first child of object with `name` == `children` that hasn't a `value` of `2`.


# See examples

You can see a fully working example in `examples` directory.
I'll add more examples during time.

[To see the Typicode example, click here](examples/typicode.example.json)
