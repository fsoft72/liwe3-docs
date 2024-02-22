<a id="throttler-applysettings"></a>
## `applySettings`


```ts
applySettings = ( _settings: ThrottlerSettings )
```


Changes Throttler's settings





**Returns**: ``

-----------------

<a id="throttler-const-throttler"></a>
## `const Throttler`


```ts
const Throttler = ( request: ILRequest, response: ILResponse, next: any )
```


Throttles incoming requests based on IP address.
If the IP address has reached the request limit, it delays the request before passing it to the next middleware.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `request` | any | The incoming request object. |
| `response` | any | The outgoing response object. |
| `next` | any | The next middleware function. |



**Returns**: ``

-----------------

