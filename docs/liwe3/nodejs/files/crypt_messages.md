<a id="crypt_messages-cryptpayload"></a>
## `cryptPayload`


```ts
cryptPayload = ( payload: any ): string
```


Encrypts the payload using AES-256-GCM encryption algorithm.


@see decryptPayload
@see cryptMessage


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `payload` | any | The payload to be encrypted. |



**Returns**: `The encrypted payload as a string.`

-----------------

<a id="crypt_messages-decryptpayload"></a>
## `decryptPayload`


```ts
decryptPayload = ( encryptedPayload: string ): any | null
```


Decrypts an encrypted payload.

@see cryptPayload


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `encryptedPayload` | any | The |



**Returns**: `The decrypted payload as an object, or null if decryption fails or the input format is invalid.`

-----------------

<a id="crypt_messages-cryptmessage"></a>
## `cryptMessage`


```ts
cryptMessage = ( payload: any ): CryptedMessage
```


Encrypts a message payload and creates a challenge.

@see cryptPayload
@see decryptMessage


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `payload` | any | The |



**Returns**: `An object containing the encrypted block and the challenge.`

-----------------

<a id="crypt_messages-cryptsend"></a>
## `cryptSend`


```ts
cryptSend = async ( fullURL: string, payload: any ): Promise<any>
```


Sends a cryptographically encrypted message to the specified URL.

@see cryptMessage
@see decryptMessage


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `fullURL` | any | The |
| `payload` | any | The |



**Returns**: `A Promise that resolves to the decrypted response from the server.`

-----------------

<a id="crypt_messages-decryptmessage"></a>
## `decryptMessage`


```ts
decryptMessage = ( cryptedMessage: CryptedMessage ): any | null
```


Decrypts a crypted message.

@see cryptMessage
@see cryptSend
@see cryptPayload
@see decryptPayload


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `cryptedMessage` | any | The crypted message to decrypt. |



**Returns**: `The decrypted payload or null if the challenge mismatched.`

-----------------

