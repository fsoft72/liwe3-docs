# Module: Tag

The `tag` module is responsible for managing tags system wide.

## Index

### Types

 | Name                  | Description
 | --------------------- | --------------
 | [Tag](#structure-tag) | Tag

### Endpoints

 |            | Path                                                  | Description
 | ---------- | ----------------------------------------------------- | ---------------------------
 | **POST**   | [/tag/admin/add](#post-tag-admin-add)                 | Add or modify a tag
 | **PATCH**  | [/tag/admin/fields](#patch-tag-admin-fields)          | Modifies some fields
 | **POST**   | [/tag/admin/list](#post-tag-admin-list)               | List all tags
 | **POST**   | [/tag/admin/module/add](#post-tag-admin-module-add)   | Adds a new module to a tag
 | **DELETE** | [/tag/admin/module/del](#delete-tag-admin-module-del) | Deletes a module from a tag
 | **PATCH**  | [/tag/admin/update](#patch-tag-admin-update)          | Updates a tag
 | **GET**    | [/tag/list](#get-tag-list)                            | List all available tag

### Functions

 | Name                        | Description
 | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 | [tag_db_init](#tag_db_init) | This function initializes the module database tables.
 | [tag_del_obj](#tag_del_obj) | This function tags an object in the system.

The given `tags` must already exist.

If one or more tag in `tags` do not exist, they will simply be skipped with no warning.
 | [tag_obj](#tag_obj)         | This function tags an object in the system.

The given `tags` must already exist.

If one or more tag in `tags` do not exist, they will simply be skipped with no warning.



# Types

---------------------------------------
<a id="structure-tag"></a>
### Tag
DB Table: `tags`

Tag

 | idx | Name           | Type    | req   | priv  | Description
 | - | -------------- | ------- | ----- | ----- | -----------------------------------------------------------------------------
 | u | id             | str     | **Y** |       | the main id field
 | y | domain         | str     |       | **Y** | The domain name
 | y | name           | str     | **Y** |       | The tag name
 | u | name_domain    | str     | **Y** | **Y** | The unique key tag <-> domain
 | y | count          | num     |       | **Y** | Number of times this tag has been used
 | y | visible        | boolean |       |       | If the tag is visible to the public
 | * | modules        | str[]   |       |       | The module using this tag. This is optional, default is 'system' (everywhere)

# Endpoints

-----------------------------------
<a id="post-tag-admin-add"></a>
## **POST** /tag/admin/add - Add or modify a tag

The call creates or updates a tag in the system

It is possible to pass the same tag with different `module` fields, and the `module` will be added to the existing modules.

This function returns the full `Tag` structure

 | Name    | Type           | req   | Description
 | ------- | -------------- | ----- | ---------------------
 | name    | str            | **Y** | The tag name
 | visible | boolean        |       | If the tag is visible


#### Permissions:
 | name           | description
 | -------------- | ---------------------------------------------------------
 | ``tag.editor`` | Only the one with this permission can change ALL the tags


#### Return: [Tag](#structure-tag) as `tag`


-----------------------------------
<a id="post-tag-admin-list"></a>
## **POST** /tag/admin/list - List all tags

List all tags in the system.

This function returns the full `Tag` structure

 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions:
 | name           | description
 | -------------- | ---------------------------------------------------------
 | ``tag.editor`` | Only the one with this permission can change ALL the tags


#### Return: [Tag](#structure-tag) as `tags`


-----------------------------------
<a id="patch-tag-admin-update"></a>
## **PATCH** /tag/admin/update - Updates a tag

Updates a tag.

This function returns the full `Tag` structure

**NOTE**: at the moment it is not possible to change a tag name.

 | Name    | Type           | req   | Description
 | ------- | -------------- | ----- | ----------------------------
 | id      | str            | **Y** | Address ID
 | name    | str            |       | Tag name
 | visible | boolean        |       | If the tag is visible or not


#### Permissions:
 | name           | description
 | -------------- | ---------------------------------------------------------
 | ``tag.editor`` | Only the one with this permission can change ALL the tags


#### Return: [Tag](#structure-tag) as `tag`


-----------------------------------
<a id="patch-tag-admin-fields"></a>
## **PATCH** /tag/admin/fields - Modifies some fields

The call modifies one or more fields.

This function returns the full `Tag` structure

 | Name | Type           | req   | Description
 | ---- | -------------- | ----- | --------------------------
 | id   | str            | **Y** | The address ID
 | data | json           | **Y** | The field / value to patch


#### Permissions:
 | name           | description
 | -------------- | ---------------------------------------------------------
 | ``tag.editor`` | Only the one with this permission can change ALL the tags


#### Return: [Tag](#structure-tag) as `tag`


-----------------------------------
<a id="post-tag-admin-module-add"></a>
## **POST** /tag/admin/module/add - Adds a new module to a tag

Adds a new module to a tag in the system.

 | Name   | Type           | req   | Description
 | ------ | -------------- | ----- | -----------------
 | id     | str            | **Y** | Tag id for update
 | module | str            | **Y** | The module to add


#### Permissions:
 | name           | description
 | -------------- | ---------------------------------------------------------
 | ``tag.editor`` | Only the one with this permission can change ALL the tags


#### Return: [Tag](#structure-tag) as `tag`


-----------------------------------
<a id="delete-tag-admin-module-del"></a>
## **DELETE** /tag/admin/module/del - Deletes a module from a tag

Deletes a module from a tag.

 | Name   | Type           | req   | Description
 | ------ | -------------- | ----- | -----------------
 | id     | str            | **Y** | Tag id for update
 | module | str            | **Y** | The module to add


#### Permissions:
 | name           | description
 | -------------- | ---------------------------------------------------------
 | ``tag.editor`` | Only the one with this permission can change ALL the tags


#### Return: [Tag](#structure-tag) as `tag`


-----------------------------------
<a id="get-tag-list"></a>
## **GET** /tag/list - List all available tag

The call returns a list of all available tag.

If `module` is specified, only tag belonging to that module will be returned.

This function returns a list of full `Tag` structures

 | Name   | Type           | req | Description
 | ------ | -------------- | - | ------------------------------------
 | module | str            |  | The name of the module to filter for


#### Permissions:
 | name       | description
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: [Tag](#structure-tag) as `tags`

# Functions

-----------------------------------
<a id="tag_del_obj"></a>
## tag_del_obj - Remove one or more tags from the object

This function tags an object in the system.

The given `tags` must already exist.

If one or more tag in `tags` do not exist, they will simply be skipped with no warning.

 | Name   | Type           | req   | Description
 | ------ | -------------- | ----- | --------------------
 | tags   | str[]          | **Y** | A list of tags
 | obj    | str            | **Y** | The object to tag
 | module | str            | **Y** | The module of id_obj


#### Return: any


-----------------------------------
<a id="tag_obj"></a>
## tag_obj - Tags an object

This function tags an object in the system.

The given `tags` must already exist.

If one or more tag in `tags` do not exist, they will simply be skipped with no warning.

 | Name   | Type           | req   | Description
 | ------ | -------------- | ----- | --------------------
 | req    | ilrequest      | **Y** | The current request
 | tags   | str[]          | **Y** | A list of tags
 | obj    | str            | **Y** | The object to tag
 | module | str            | **Y** | The module of id_obj


#### Return: any


-----------------------------------
<a id="tag_db_init"></a>
## tag_db_init - Initializes tag module database

This function initializes the module database tables.

 | Name | Type           | req   | Description
 | ---- | -------------- | ----- | ----------------
 | liwe | iliwe          | **Y** | LiWE full config


#### Return: boolean
