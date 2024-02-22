<a id="arango-adb-init"></a>
## `adb_init`


```ts
adb_init = async ( cfg: ILiweConfig ): Promise<Database>
```



// import { ILApplication } from './types';
import { Database } from 'arangojs';
import { ILiweConfig } from '../types';
import { critical, error } from '../console_colors';
import { DocumentCollection } from "arangojs/collection";

import { config_load } from "../liwe";
import { keys_filter } from "../utils";

const cfg: ILiweConfig = config_load( 'data', {}, true, true );

export interface QueryOptions {
If T, the query will return also the count of documents
count?: boolean;
The pagination starting point
skip?: number;
The number of documents to return
rows?: number;
}

export interface DBCollectionIndex {
type: "hash" | "persistent" | "skiplist" | "ttl" | "geo" | "fulltext";
name?: string;
fields: string[];
unique: boolean;
sparse?: boolean;
deduplicate?: boolean;
}

export interface DBCollectionCreateOptions {
Set this to true if you want to drop the collection if it already exists.
drop?: boolean;
}

interface SortOptions {
field: string;
desc?: number;
}

interface CollectionFindAllOptions {
rows?: number;
skip?: number;
sort?: SortOptions[];

If T, the query will return also the count of documents
count?: boolean;
}

const _check_default_analyzers = async ( db: Database ) => {
const analyzers = [ 'norm_it', 'norm_en' ];

await Promise.all( analyzers.map( async ( name ) => {
const analyzer = db.analyzer( name );
if ( !analyzer || !( await analyzer.exists() ) ) {
console.log( `  -- DB: Analyzer ${ name } MISSING` );

const locale = name == 'norm_en' ? 'en.utf-8' : 'it.utf-8';

analyzer.create( { type: 'norm', properties: { locale, accent: false, case: "lower" } } );
}
} ) );
};

// gets a collection by its name, returns null if it does not exist
const _collection_get = ( db: Database, coll_name: string, raise: boolean = true ): DocumentCollection => {
if ( !db ) return null;

const coll: DocumentCollection = db.collection( coll_name );

if ( !coll && raise ) throw ( new Error( `Collection ${ coll_name } does not exist` ) );

return coll;
};



ArangoDB database initialization





**Returns**: ``

-----------------

<a id="arango-adb-db-create"></a>
## `adb_db_create`


```ts
adb_db_create = async ( adb: Database, name: string ): Promise<Database>
```


Creates a database if it does not exist

@throws 		ArangoError



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `adb` | any | ArangoDB |
| `name` | any | Name |



**Returns**: `ArangoDB database`

-----------------

<a id="arango-adb-db-drop"></a>
## `adb_db_drop`


```ts
adb_db_drop = async ( adb: Database, name: string ): Promise<boolean>
```


Drops a database

@throws 		ArangoError


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `adb` | any | ArangoDB |
| `name` | any | Name |



**Returns**: `True if the database was dropped, false otherwise`

-----------------

<a id="arango-adb-collection-create"></a>
## `adb_collection_create`


```ts
adb_collection_create = async ( db: Database, name: string, options: DBCollectionCreateOptions = null ): Promise<any>
```


Creates a collection if it does not exist


@throws 			ArangoError



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `db` | any | ArangoDB |
| `name` | any | Name |
| `options` | any | Options |



**Returns**: `ArangoDB collection`

-----------------

<a id="arango-adb-collection-drop"></a>
## `adb_collection_drop`


```ts
adb_collection_drop = async ( db: Database, name: string ): Promise<boolean>
```


Drops a collection




**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `db` | any | ArangoDB |
| `name` | any | Name |



**Returns**: `True if the collection was dropped, false otherwise`

-----------------

<a id="arango-adb-record-add"></a>
## `adb_record_add`


```ts
adb_record_add = async ( db: Database, coll_name: string, data: any, data_type?: any ): Promise<any>
```


Adds / updates an element in the collection


@note - The update only works if the element has an _id field (the original Arango unique field)


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `db` | any |  |
| `coll_name	Name` | any | of |
| `data` | any |  |
| `data_type	If` | any | present, |



**Returns**: ``

-----------------

<a id="arango-adb-record-replace"></a>
## `adb_record_replace`


```ts
adb_record_replace = async ( db: Database, coll_name: string, data: any, data_type?: any ): Promise<any>
```


Replaces an element in the collection


@note - The update only works if the element has an _id field (the original Arango unique field)


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `db` | any |  |
| `coll_name	Name` | any | of |
| `data` | any |  |
| `data_type	If` | any | present, |



**Returns**: ``

-----------------

<a id="arango-adb-record-add-all"></a>
## `adb_record_add_all`


```ts
adb_record_add_all = async ( db: Database, coll_name: string, data: any ): Promise<any>
```


Adds / updates a list of elements in the collection



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `coll` | any |  |
| `data` | any |  |
| `data_type	If` | any | present, |



**Returns**: ``

-----------------

<a id="arango-adb-query-all"></a>
## `adb_query_all`


```ts
adb_query_all = async ( db: Database, query: string, params: any = undefined, data_type: any = undefined, options?: QueryOptions ): Promise<any>
```


Query the database using AQL



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `db` | any | the database to query on |
| `query` | any | the AQL query |
| `params` | any | a key/value pairs of params present in the query |
| `data_type` | any | if present, result list will be filtered before returning |
| `options` | any | Query options that change the behaviour of the query |



**Returns**: ``

-----------------

<a id="arango-adb-query-one"></a>
## `adb_query_one`


```ts
adb_query_one = async ( db: Database, query: string, params: any = undefined, data_type: any = undefined ): Promise<any>
```


returns a single element



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `db` | any | the database to query on |
| `query` | any | the AQL query |
| `params` | any | a key/value pairs of params present in the query |
| `data_type` | any | if present, result list will be filtered before returning |



**Returns**: ``

-----------------

<a id="arango-adb-query-count"></a>
## `adb_query_count`


```ts
adb_query_count = async ( db: Database, query: string, params: any = undefined ): Promise<number>
```


In `query` just put 'FOR ... IN ....' and FILTERs  (no RETURN)





**Returns**: ``

-----------------

<a id="arango-adb-collection-init"></a>
## `adb_collection_init`


```ts
adb_collection_init = async ( db: Database, name: string, idx: DBCollectionIndex[] = null, options: DBCollectionCreateOptions = null )
```


Creates a collection in the database setting the indexes




**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `db` | any | ArangoDB |
| `name` | any | Name |
| `idx` | any | Indexes |
| `options` | any | Options |



**Returns**: `The collection`

-----------------

<a id="arango-adb-prepare-filters"></a>
## `adb_prepare_filters`


```ts
adb_prepare_filters = ( prefix: string, data: any, extra_values?: any )
```


Create filters and pagination (if skip and rows are defined)

If rows == -1, then all rows are returned

This accepts two type of key/values

- "just"  a key/value
- a value that is an object with the following keys:
- val:    the value to match against
- mode:   the arango DB comparsion mode
- name:   the field name to match on

NOTE: in 'mode' == 'multi' or 'm'  the inner search filter is used

Returns [filters, values]





**Returns**: ``

-----------------

<a id="arango-adb-count"></a>
## `adb_count`


```ts
adb_count = async ( db: Database, coll_name: string, data: any )
```


Counts the number of documents in a collection



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `db` | any |  |
| `coll_name` | any |  |
| `data` | any |  |



**Returns**: ``

-----------------

<a id="arango-adb-find-all"></a>
## `adb_find_all`


```ts
adb_find_all = async ( db: Database, coll_name: string, data: any = undefined, data_type: any = undefined, options?: CollectionFindAllOptions )    //rows = 0, skip = 0 )
```


returns a list of elements



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `db` | any |  |
| `coll_name` | any |  |
| `data` | any |  |
| `data_type` | any | if present, result list will be filtered before returning |
| `options` | any | A `CollectionFindAllOptions` object |



**Returns**: ``

-----------------

<a id="arango-adb-find-one"></a>
## `adb_find_one`


```ts
adb_find_one = async ( db: Database, coll_name: string, data: any, data_type: any = undefined )
```


returns a single element based on a dict


@note: if no filter is specified, returns a warning and returns null


**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `db` | any |  |
| `coll_name` | any |  |
| `data` | any |  |
| `data_type` | any | if present, result list will be filtered before returning |



**Returns**: ``

-----------------

<a id="arango-adb-del-one"></a>
## `adb_del_one`


```ts
adb_del_one = async ( db: Database, coll_name: string, data: any )
```


removes one element from a collection



**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `db` | any |  |
| `coll_name` | any |  |
| `data` | any |  |



**Returns**: ``

-----------------

<a id="arango-adb-del-all"></a>
## `adb_del_all`


```ts
adb_del_all = async ( db: Database, coll_name: string, data: any )
```


removes all elements from a collection




**Parameters**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `db` | any |  |
| `coll_name` | any |  |
| `data` | any |  |



**Returns**: `a list of removed elements ids`

-----------------

