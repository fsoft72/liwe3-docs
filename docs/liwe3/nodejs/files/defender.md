<a id="defender-get-real-ip"></a>
## `get_real_ip`


```ts
get_real_ip = ( request: ILRequest ): string
```


Retrieves the real IP address from the request object.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `request` | any | The request object containing the headers and socket information. |



**Returns**: `The real IP address as a string.`

-----------------

<a id="defender-blacklist-ip"></a>
## `blacklist_ip`


```ts
blacklist_ip = ( ip_addr: string, duration: number )
```


Add an IP address to blacklist

Parameters:

- ip_addr   - The IP to blacklist
- duration  - Time in millis of the blacklist





**Returns**: ``

-----------------

<a id="defender-blacklist-ip-list"></a>
## `blacklist_ip_list`


```ts
blacklist_ip_list = ()
```


Retrieves a list of blacklisted IP addresses along with their corresponding dates.





**Returns**: `An array of objects containing the IP address and date of each blacklisted IP.`

-----------------

<a id="defender-applysettings"></a>
## `applySettings`


```ts
applySettings = ( _settings: DefenderSettings )
```


Changes Defender's settings





**Returns**: ``

-----------------

<a id="defender-const-defender"></a>
## `const Defender`


```ts
const Defender = ( request: ILRequest, response: ILResponse, next: any )
```


Middleware function that acts as a defender against suspicious requests.
It checks for blacklisted IP addresses and suspicious URL fragments.
If an IP address is blacklisted, it returns a 403 response.
If a suspicious URL fragment is found, it handles the request accordingly.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `request` | any | The incoming request object. |
| `response` | any | The outgoing response object. |
| `next` | any | The next middleware function in the chain. |



**Returns**: ``

-----------------

<a id="defender-add-suspicious-activity"></a>
## `add_suspicious_activity`


```ts
add_suspicious_activity = ( request: ILRequest, response: ILResponse, message: string ): boolean
```


add a new suspicious activity to the log
if it returns `true`, it means that ip reached threshold





**Returns**: ``

-----------------

