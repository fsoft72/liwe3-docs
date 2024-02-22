<a id="locale-class-locale-implements-ilocale"></a>
## `class Locale implements ILocale`


```ts
class Locale implements ILocale
```


Represents a locale with language modules for translation.





**Returns**: ``

-----------------

<a id="locale-public-set-default-language"></a>
## `public set_default_language ( lang: string ): void`


```ts
public set_default_language ( lang: string ): void
```


Sets the default language for the locale.
If no language is provided, 'en' (English) will be used as the default.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `lang` | any | The language code to set as the default. |



**Returns**: `void`

-----------------

<a id="locale-public-set"></a>
## `public set ( lang: string, key: string, single: string, plural: string, module: string`


```ts
public set ( lang: string, key: string, single: string, plural: string, module: string = 'default' ): void
```


Sets the translation for a given language, key, single and plural values, and module.
If the module is not specified, it defaults to 'default'.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `lang` | any | The |
| `key` | any | The |
| `single` | any | The |
| `plural` | any | The |
| `module` | any | The |



**Returns**: ``

-----------------

<a id="locale-public-set-multi"></a>
## `public set_multi ( lang: string, module: string, items: ILocString[] ): void`


```ts
public set_multi ( lang: string, module: string, items: ILocString[] ): void
```


Sets multiple localization strings for a specific language and module.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `lang` | any | The |
| `module` | any | The |
| `items` | any | An |



**Returns**: ``

-----------------

<a id="locale-public-dump"></a>
## `public dump ()`


```ts
public dump ()
```


Dumps the current state of the object to the console.





**Returns**: ``

-----------------

<a id="locale-public-tojson"></a>
## `public toJSON ()`


```ts
public toJSON ()
```


Converts the languages object to a JSON string representation.





**Returns**: `{string} The JSON string representation of the languages object.`

-----------------

<a id="locale-public-best-language"></a>
## `public best_language ( languages: string`


```ts
public best_language ( languages: string = "" )
```


Finds the best language from the given list of languages.
If no languages are provided, the default language is used.
The best language is determined by matching the languages against the available localization strings.
The first matching language is considered the preferred language.
If no matching language is found, the default language is returned.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `languages` | any | The list of languages to search for the best language. |



**Returns**: `The best language found or the default language if no match is found.`

-----------------

<a id="locale-public-translate"></a>
## `public translate ( lang: string, key: string, val: object, plural: boolean`


```ts
public translate ( lang: string, key: string, val: object, plural: boolean = false, module: string = 'default' ): string
```


Translates a given key into the specified language.


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `lang` | any | The |
| `key` | any | The |
| `val` | any | The |
| `plural` | any | Indicates |
| `module` | any | The |



**Returns**: `The translated string.`

-----------------

<a id="locale-$l"></a>
## `$l`


```ts
$l = ( key: string, val: object, plural: boolean = false, module: string = 'default', lang: string = null )
```


Translates a key using the specified language, module, and values.



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `key` | any | The key to be translated. |
| `val` | any | The values to be substituted in the translation. |
| `plural` | any | Indicates whether the translation is for plural form. |
| `module` | any | The module name for the translation. |
| `lang` | any | The language code for the translation. If not provided, the default language will be used. |



**Returns**: `The translated string.`

-----------------

<a id="locale-locale-load"></a>
## `locale_load`


```ts
locale_load = ( module: string, language: string )
```


load a locale collection into the system



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `module` | any | The module name (eg. 'user', 'system') |
| `language` | any | The language to load (eg. "it", "en", "es" ) |



**Returns**: ``

-----------------

