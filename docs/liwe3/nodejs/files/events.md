<a id="events-liwe-event-register"></a>
## `liwe_event_register`


```ts
liwe_event_register = ( modname: string, event: string, handler: LiWEEventHandler )
```


Registers an event handler for a specific event.


@see liwe_event_unregister


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `modname` | any | The name of the module. |
| `event` | any | The name of the event. |
| `handler` | any | The event handler function. |



**Returns**: ``

-----------------

<a id="events-liwe-event-emit"></a>
## `liwe_event_emit`


```ts
liwe_event_emit = async ( req: ILRequest, event: string, data: any )
```


Emits a LiWE event and invokes all registered event handlers.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `req` | any | The ILRequest object. |
| `event` | any | The name of the event to emit. |
| `data` | any | The data associated with the event. |



**Returns**: `A Promise that resolves to an array of LiWEEventResponse objects.`

-----------------

<a id="events-liwe-event-unregister"></a>
## `liwe_event_unregister`


```ts
liwe_event_unregister = ( event: string, handler: LiWEEventHandler )
```


Unregisters an event handler for a specific event.


@see liwe_event_register


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `event` | any | The name of the event to unregister the handler from. |
| `handler` | any | The event handler function to unregister. |



**Returns**: ``

-----------------

<a id="events-liwe-event-list"></a>
## `liwe_event_list`


```ts
liwe_event_list = ()
```


Retrieves the list of LIWE events.





**Returns**: `{string[]} The list of LIWE events.`

-----------------

