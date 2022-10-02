# Module: System



## Index

### Types

 | Name                                     | Description
 | ---------------------------------------- | ---------------------------------
 | [SystemDomain](#structure-system-domain) | The multi-tier domain
 | [SystemTheme](#structure-system-theme)   | Handling of system theme settings

### Endpoints

 |            | Path                                                             | Description
 | ---------- | ---------------------------------------------------------------- | ---------------------------------------
 | **POST**   | [/system/admin/domain/add](#post-system-admin-domain-add)        | Adds a domain in the system
 | **DELETE** | [/system/admin/domain/del](#delete-system-admin-domain-del)      | Deletes a domain from the system
 | **PATCH**  | [/system/admin/domain/update](#patch-system-admin-domain-update) | Updates a domain in the system
 | **GET**    | [/system/admin/domains/list](#get-system-admin-domains-list)     | List all domains
 | **PATCH**  | [/system/admin/reset/id](#patch-system-admin-reset-id)           | Force an id to be changed on the system
 | **PATCH**  | [/system/admin/theme/set](#patch-system-admin-theme-set)         | Set the system theme
 | **POST**   | [/system/domain/set](#post-system-domain-set)                    | Set the current domain for the user
 | **GET**    | [/system/domains/list](#get-system-domains-list)                 | List all visible domains
 | **GET**    | [/system/theme/get](#get-system-theme-get)                       | Returns the current theme

### Functions

 | Name                                                          | Description
 | ------------------------------------------------------------- | -------------------------------------------------------------
 | [system_db_init](#system_db_init)                             | This function initializes the module database tables.
 | [system_domain_get_by_code](#system_domain_get_by_code)       | This function returns a `SystemDomain` structure by its code.
 | [system_domain_get_by_id](#system_domain_get_by_id)           | This function returns a `SystemDomain` structure by its id.
 | [system_domain_get_by_session](#system_domain_get_by_session) | This function returns a `SystemDomain` structure by its code.
 | [system_domain_get_default](#system_domain_get_default)       | This function returns a `SystemDomain` structure by its id.



# Types

---------------------------------------
<a id="structure-system-domain"></a>
### SystemDomain
DB Table: `system_domains`

The multi-tier domain

 | idx | Name           | Type    | req   | priv  | Description
 | - | -------------- | ------- | ----- | ----- | ------------------------
 | u | id             | str     | **Y** |       | the main id field
 | u | code           | str     | **Y** |       | The domain unique code
 |   | name           | str     | **Y** |       | The domain name
 | y | visible        | boolean |       | **Y** | If the domain is visible


---------------------------------------
<a id="structure-system-theme"></a>
### SystemTheme
DB Table: `system_themes`

Handling of system theme settings

 | idx | Name           | Type | req   | priv  | Description
 | - | -------------- | ---- | ----- | ----- | -----------------
 | u | id             | str  | **Y** |       | the main id field
 | u | domain         | str  | **Y** | **Y** | The domain code
 |   | data           | json |       |       | The Theme data

# Endpoints

-----------------------------------
<a id="get-system-domains-list"></a>
## **GET** /system/domains/list - List all visible domains

List all visible domains

 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions:
 | name              | description
 | ----------------- | --------------------------------------
 | ``system.domain`` | The user can operate on system domains


#### Return: [SystemDomain](#structure-system-domain) as `domains`


-----------------------------------
<a id="post-system-domain-set"></a>
## **POST** /system/domain/set - Set the current domain for the user

Set the current domain for the user


 | Name | Type           | req   | Description
 | ---- | -------------- | ----- | ----------------------
 | code | str            | **Y** | the domain unique code


#### Permissions:
 | name       | description
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: [SystemDomain](#structure-system-domain) as `domain`


-----------------------------------
<a id="post-system-admin-domain-add"></a>
## **POST** /system/admin/domain/add - Adds a domain in the system

Adds a new domain to the System.

 | Name    | Type           | req   | Description
 | ------- | -------------- | ----- | -----------------------------------------------
 | code    | str            | **Y** | the domain unique code
 | name    | str            | **Y** | the domain name
 | visible | boolean        |       | if the domain is visible or not [default: true]


#### Permissions:
 | name              | description
 | ----------------- | --------------------------------------
 | ``system.domain`` | The user can operate on system domains


#### Return: [SystemDomain](#structure-system-domain) as `domain`


-----------------------------------
<a id="patch-system-admin-domain-update"></a>
## **PATCH** /system/admin/domain/update - Updates a domain in the system

Updates a domain in the system. The `id` field must be provided.


 | Name    | Type           | req   | Description
 | ------- | -------------- | ----- | -------------------------------
 | id      | str            | **Y** | the domain id
 | code    | str            |       | the domain unique code
 | name    | str            |       | the domain name
 | visible | boolean        |       | if the domain is visible or not


#### Permissions:
 | name              | description
 | ----------------- | --------------------------------------
 | ``system.domain`` | The user can operate on system domains


#### Return: [SystemDomain](#structure-system-domain) as `domain`


-----------------------------------
<a id="delete-system-admin-domain-del"></a>
## **DELETE** /system/admin/domain/del - Deletes a domain from the system

Delete a domain from the system. You can specify both `id` and `code` for deletion


 | Name | Type           | req | Description
 | ---- | -------------- | - | ----------------------
 | id   | str            |  | the domain id
 | code | str            |  | the domain unique code


#### Permissions:
 | name              | description
 | ----------------- | --------------------------------------
 | ``system.domain`` | The user can operate on system domains


#### Return: str as `id_domain`


-----------------------------------
<a id="get-system-admin-domains-list"></a>
## **GET** /system/admin/domains/list - List all domains

List all domains

 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions:
 | name              | description
 | ----------------- | --------------------------------------
 | ``system.domain`` | The user can operate on system domains


#### Return: [SystemDomain](#structure-system-domain) as `domains`


-----------------------------------
<a id="patch-system-admin-theme-set"></a>
## **PATCH** /system/admin/theme/set - Set the system theme

Changes something in the system theme.


 | Name    | Type           | req | Description
 | ------- | -------------- | - | ----------------
 | changes | json           |  | the main changes


#### Permissions:
 | name             | description
 | ---------------- | ---------------------------------
 | ``system.theme`` | The user can manage system themes


#### Return: [SystemTheme](#structure-system-theme) as `theme`


-----------------------------------
<a id="get-system-theme-get"></a>
## **GET** /system/theme/get - Returns the current theme



 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions:
 | name       | description
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: [SystemTheme](#structure-system-theme) as `theme`


-----------------------------------
<a id="patch-system-admin-reset-id"></a>
## **PATCH** /system/admin/reset/id - Force an id to be changed on the system

Force an id to be changed on the system.
You have to specify the current `id`, the new `id` and the `collection` name.


 | Name       | Type           | req   | Description
 | ---------- | -------------- | ----- | -------------------
 | id         | str            | **Y** | the current id
 | new_id     | str            | **Y** | the new id
 | collection | str            | **Y** | the collection name


#### Permissions:
 | name             | description
 | ---------------- | ------------------------------------------
 | ``system.admin`` | The super user permission to do everything


#### Return: str as `id`

# Functions

-----------------------------------
<a id="system_domain_get_default"></a>
## system_domain_get_default - Gets the default domain

This function returns a `SystemDomain` structure by its id.

 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Return: [SystemDomain](#structure-system-domain)


-----------------------------------
<a id="system_domain_get_by_id"></a>
## system_domain_get_by_id - Gets a domain by its id

This function returns a `SystemDomain` structure by its id.

 | Name | Type           | req   | Description
 | -- | -------------- | ----- | -------------
 | id | str            | **Y** | The Domain id


#### Return: [SystemDomain](#structure-system-domain)


-----------------------------------
<a id="system_domain_get_by_code"></a>
## system_domain_get_by_code - Gets a domain by its code

This function returns a `SystemDomain` structure by its code.

 | Name | Type           | req   | Description
 | ---- | -------------- | ----- | ---------------
 | code | str            | **Y** | The Domain code


#### Return: [SystemDomain](#structure-system-domain)


-----------------------------------
<a id="system_domain_get_by_session"></a>
## system_domain_get_by_session - Gets a domain by user session

This function returns a `SystemDomain` structure by its code.

 | Name | Type           | req   | Description
 | --- | -------------- | ----- | ---------------------------
 | req | ilrequest      | **Y** | The current session request


#### Return: [SystemDomain](#structure-system-domain)


-----------------------------------
<a id="system_db_init"></a>
## system_db_init - Initializes system module

This function initializes the module database tables.

 | Name | Type           | req   | Description
 | ---- | -------------- | ----- | ----------------
 | liwe | iliwe          | **Y** | LiWE full config


#### Return: boolean
