<a id="image-resize"></a>
## `resize`


```ts
resize = ( src_path: string, dest_path: string, width: number = 0, height: number = 0, options: ResizeOptions = null, cback: LCback = undefined )
```


resize - resizes the given image to the desider width / height maintaining aspect ratio or scaling fixed.
At least width or height MUST be defined.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `src_path` | any | the original image file to be scaled (full path + filename) |
| `dest_path` | any | the destination path where to save the scaled image (full path + filename) |
| `width` | any | the desired image width in px (can be 0 if you want to scale on height) [0] |
| `height` | any | the desired image height in px (can be 0 if you want to scale on width) [0] |
| `options` | any | resize options |
| `cback` | any | Callback to be called on completion |



**Returns**: ``

-----------------

<a id="image-mk-thumb"></a>
## `mk_thumb`


```ts
mk_thumb = async ( src_path: string, dest_path: string, width: number = 0, height: number = 0, options: ResizeOptions = null, cback: LCback = undefined )
```


Creates a thumbnail image from the source image file.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `src_path` | any | The |
| `dest_path` | any | The |
| `width` | any | The |
| `height` | any | The |
| `options` | any | The |
| `cback` | any | The |



**Returns**: ``

-----------------

<a id="image-compress-image"></a>
## `compress_image`


```ts
compress_image = async ( src_path: string, dest_path: string, quality = 80, cback: LCback = undefined )
```


Compresses an image file.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `src_path` | any | The path of the source image file. |
| `dest_path` | any | The path where the compressed image will be saved. |
| `quality` | any | The quality of the compressed image (default: 80). |
| `cback` | any | Optional callback function to be executed after compression. |



**Returns**: `A boolean indicating whether the compression was successful.`

-----------------

