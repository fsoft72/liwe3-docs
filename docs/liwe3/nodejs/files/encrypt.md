<a id="encrypt-encryptbinary"></a>
## `encryptBinary`


```ts
encryptBinary = ( data: Buffer, secret: string ): Buffer
```


Encrypts binary data using a secret key.


@see decryptBinary


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `data` | any | The binary data to be encrypted. |
| `secret` | any | The secret key used for encryption. |



**Returns**: `The encrypted binary data.`

-----------------

<a id="encrypt-decryptbinary"></a>
## `decryptBinary`


```ts
decryptBinary = ( encryptedData: Buffer, secret: string ): Buffer
```


Decrypts binary data using a secret key.


@see encryptBinary


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `encryptedData` | any | The encrypted binary data to be decrypted. |
| `secret` | any | The secret key used for decryption. |



**Returns**: `The decrypted binary data.`

-----------------

<a id="encrypt-encryptstring"></a>
## `encryptString`


```ts
encryptString = ( data: string, secret: string ): string
```


Encrypts a string using a secret key.

@see decryptString


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `data` | any | The string to be encrypted. |
| `secret` | any | The secret key used for encryption. |



**Returns**: `The encrypted string in hexadecimal format.`

-----------------

<a id="encrypt-decryptstring"></a>
## `decryptString`


```ts
decryptString = ( encryptedData: string, secret: string ): string
```


Decrypts an encrypted string using a secret key.


@see encryptString


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `encryptedData` | any | The encrypted string to be decrypted. |
| `secret` | any | The secret key used for decryption. |



**Returns**: `The decrypted string.`

-----------------

<a id="encrypt-encryptfile"></a>
## `encryptFile`


```ts
encryptFile = async ( input: string, output: string, secret: string ): Promise<void>
```


Encrypts a file using a secret key.


@see decryptFile


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | any | The path to the input file. |
| `output` | any | The path to the output file. |
| `secret` | any | The secret key used for encryption. |



**Returns**: `A Promise that resolves when the encryption is complete.`

-----------------

<a id="encrypt-decryptfile"></a>
## `decryptFile`


```ts
decryptFile = async ( input: string, output: string, secret: string ): Promise<void>
```


Decrypts a file using a secret key.


@see encryptFile


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | any | The path of the input file to be decrypted. |
| `output` | any | The path of the output file where the decrypted content will be written. |
| `secret` | any | The secret key used for decryption. |



**Returns**: `A Promise that resolves when the decryption is complete.`

-----------------

