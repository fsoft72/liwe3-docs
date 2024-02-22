<a id="mail-send-mail"></a>
## `send_mail`


```ts
send_mail = async ( subject: string, text: string, html: string, to: string, from: string, reply_to: string, cback: LCback = null )
```


sends an email using settings from `cfg.smtp`



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `subect` | any | Email |
| `text` | any |  |
| `html` | any |  |
| `to` | any |  |
| `from` | any | sender |
| `cback` | any | the |



**Returns**: ``

-----------------

<a id="mail-send-mail-template"></a>
## `send_mail_template`


```ts
send_mail_template = ( subject: string, template: string, args: object, to: string, from: string, reply_to: string, cback: LCback )
```


sends an email using the `template` provided




**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `subect` | any | Email |
| `template` | any |  |
| `args` | any |  |
| `to` | any |  |
| `from` | any | sender |
| `cback` | any | the |



**Returns**: ``

-----------------

<a id="mail-send-mail-template-locale"></a>
## `send_mail_template_locale`


```ts
send_mail_template_locale = ( module: string, template_filename: string, language: string, subject: string, args: object, to: string, from: string, reply_to: string, cback: LCback )
```


sends an email using the `template` in the right locale (if available) or using the default locale




**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `module` | any |  |
| `template_filename` | any |  |
| `language` | any |  |
| `subect` | any | Email |
| `args` | any |  |
| `to` | any |  |
| `from` | any | sender |
| `reply_to` | any | where |
| `cback` | any | the |



**Returns**: ``

-----------------

