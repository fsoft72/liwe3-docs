<a id="auth-perm-available"></a>
## `perm_available`


```ts
perm_available = ( user: MiniUserDetails, perms: string[] ): boolean
```


Verifies if the provided `user` has one of the perms specified by the `perms` string array.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `user` | any | The user |
| `perms` | any | A string[] of perms |



**Returns**: ``

-----------------

<a id="auth-perms"></a>
## `perms`


```ts
perms = ( perms: string[] )
```


Middleware function that checks if the user has the required permissions.
If the user does not have the required permissions, it sends a 403 Forbidden response.
If the `check_permissions` configuration option is disabled, it allows the request to proceed.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `perms` | any | An array of permission strings that the user must have. |



**Returns**: `A middleware function that can be used in an Express.js route handler.`

-----------------

<a id="auth-is-logged"></a>
## `is_logged`


```ts
is_logged = ( req: ILRequest, res: ILResponse )
```


Checks if the user is logged in.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `req` | any | The request object. |
| `res` | any | The response object. |



**Returns**: ``

-----------------

