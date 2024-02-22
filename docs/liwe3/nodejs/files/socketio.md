<a id="socketio-export-interface-iliwesocketmessage"></a>
## `export interface ILiWESocketMessage`


```ts
export interface ILiWESocketMessage
```


The ILiWESocketMessage defines the type of message handled by SocketIORouter
All the messages in LiWE Socket.IO implementation have the same signature
similar to Redux dispatch bundle.





**Returns**: ``

-----------------

<a id="socketio-export-class-socketiorouter"></a>
## `export class SocketIORouter`


```ts
export class SocketIORouter
```


The SocketIORouter class is a singleton class created directly by liwe.startup () and defines the internal LiWE implementation
of Socke.IO lib.






**Returns**: ``

-----------------

<a id="socketio-public-listener-add"></a>
## `public listener_add ( name: string, cback: any )`


```ts
public listener_add ( name: string, cback: any )
```


Adds a listener for the specified event name.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `name` | any | The name of the event to listen for. |
| `cback` | any | The callback function to be executed when the event is triggered. |



**Returns**: ``

-----------------

<a id="socketio-public-listener-del"></a>
## `public listener_del ( name: string )`


```ts
public listener_del ( name: string )
```


Removes a listener by name.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `name` | any | The name of the listener to remove. |



**Returns**: ``

-----------------

<a id="socketio-public-send-direct-raw"></a>
## `public send_direct_raw ( socket_id: string, action: string, payload: any )`


```ts
public send_direct_raw ( socket_id: string, action: string, payload: any )
```


Sends a raw message directly to a specific socket.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `socket_id` | any | The |
| `action` | any | The |
| `payload` | any | The |



**Returns**: ``

-----------------

