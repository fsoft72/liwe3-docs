# Module: System



## Index

### Types

 | Name                                                  | Description                      
 | ----------------------------------------------------- | ---------------------------------
 | [SystemDomain](#structure-system-domain)              | The multi-tier domain            
 | [SystemDomainAdmin](#structure-system-domain-admin)   | The multi-tier domain            
 | [SystemDomainPublic](#structure-system-domain-public) | The public info for a Domain     
 | [SystemTheme](#structure-system-theme)                | Handling of system theme settings

### Endpoints

 |            | Path                                                                 | Description                                    
 | ---------- | -------------------------------------------------------------------- | -----------------------------------------------
 | **POST**   | [/system/admin/domain/add](#post-system-admin-domain-add)            | Adds a domain in the system                    
 | **DELETE** | [/system/admin/domain/del](#delete-system-admin-domain-del)          | Deletes a domain from the system               
 | **PATCH**  | [/system/admin/domain/update](#patch-system-admin-domain-update)     | Updates a domain in the system                 
 | **GET**    | [/system/admin/domains/list](#get-system-admin-domains-list)         | List all domains                               
 | **GET**    | [/system/admin/permissions/list](#get-system-admin-permissions-list) | Returns all permissions available on the system
 | **PATCH**  | [/system/admin/reset/id](#patch-system-admin-reset-id)               | Force an id to be changed on the system        
 | **PATCH**  | [/system/admin/theme/set](#patch-system-admin-theme-set)             | Set the system theme                           
 | **GET**    | [/system/domain/current](#get-system-domain-current)                 | Returns the current active domain              
 | **POST**   | [/system/domain/set](#post-system-domain-set)                        | Set the current domain for the user            
 | **GET**    | [/system/domains/list](#get-system-domains-list)                     | List all visible domains                       
 | **POST**   | [/system/email/test](#post-system-email-test)                        | Test email sending                             
 | **GET**    | [/system/theme/get](#get-system-theme-get)                           | Returns the current theme                      

### Functions

 | Name                                                          | Description                                                                                                                                                                                                                        
 | ------------------------------------------------------------- | -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 | [system_db_init](#system_db_init)                             | This function initializes the module database tables.                                                                                                                                                                              
 | [system_domain_get_by_code](#system_domain_get_by_code)       | This function returns a `SystemDomain` structure by its code.                                                                                                                                                                      
 | [system_domain_get_by_id](#system_domain_get_by_id)           | This function returns a `SystemDomain` structure by its id.                                                                                                                                                                        
 | [system_domain_get_by_session](#system_domain_get_by_session) | This function returns a `SystemDomain` structure by its code.                                                                                                                                                                      
 | [system_domain_get_default](#system_domain_get_default)       | This function returns a `SystemDomain` structure by its id.                                                                                                                                                                        
 | [system_permissions_register](#system_permissions_register)   | This function is called by every module during the initialization phase.
The module calls this function to pass its permissions and descriptions to the system.

This data is consumed by `/system/admin/permissions/list` endpoint

	

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


---------------------------------------
<a id="structure-system-domain-admin"></a>
### SystemDomainAdmin
The multi-tier domain


 | idx | Name           | Type    | req   | priv | Description             
 | - | -------------- | ------- | ----- | - | ------------------------
 | u | id             | str     | **Y** |  | the main id field       
 | u | code           | str     | **Y** |  | The domain unique code  
 |   | name           | str     | **Y** |  | The domain name         
 | y | visible        | boolean | **Y** |  | If the domain is visible


---------------------------------------
<a id="structure-system-domain-public"></a>
### SystemDomainPublic
The public info for a Domain


 | idx | Name           | Type | req   | priv | Description      
 | - | -------------- | --- | ----- | - | -----------------
 | u | id             | str | **Y** |  | the main id field
 |   | code           | str | **Y** |  |                  
 |   | name           | str | **Y** |  |                  

# Endpoints

-----------------------------------
<a id="get-system-domains-list"></a>
## **GET**&nbsp;`/system/domains/list`&nbsp;- List all visible domains

List all visible domains


 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions: 
 | name              | description                           
 | ----------------- | --------------------------------------
 | ``system.domain`` | The user can operate on system domains


#### Return: `domains` as [SystemDomain](#structure-system-domain)


-----------------------------------
<a id="post-system-domain-set"></a>
## **POST**&nbsp;`/system/domain/set`&nbsp;- Set the current domain for the user

Set the current domain for the user



 | Name | Type           | req   | Description           
 | ---- | -------------- | ----- | ----------------------
 | code | str            | **Y** | the domain unique code


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: `domain` as [SystemDomain](#structure-system-domain)


-----------------------------------
<a id="post-system-admin-domain-add"></a>
## **POST**&nbsp;`/system/admin/domain/add`&nbsp;- Adds a domain in the system

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


#### Return: `domain` as [SystemDomain](#structure-system-domain)


-----------------------------------
<a id="patch-system-admin-domain-update"></a>
## **PATCH**&nbsp;`/system/admin/domain/update`&nbsp;- Updates a domain in the system

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


#### Return: `domain` as [SystemDomain](#structure-system-domain)


-----------------------------------
<a id="delete-system-admin-domain-del"></a>
## **DELETE**&nbsp;`/system/admin/domain/del`&nbsp;- Deletes a domain from the system

Delete a domain from the system. You can specify both `id` and `code` for deletion



 | Name | Type           | req | Description           
 | ---- | -------------- | - | ----------------------
 | id   | str            |  | the domain id         
 | code | str            |  | the domain unique code


#### Permissions: 
 | name              | description                           
 | ----------------- | --------------------------------------
 | ``system.domain`` | The user can operate on system domains


#### Return: `id_domain` as str


-----------------------------------
<a id="get-system-admin-domains-list"></a>
## **GET**&nbsp;`/system/admin/domains/list`&nbsp;- List all domains

List all domains


 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions: 
 | name              | description                           
 | ----------------- | --------------------------------------
 | ``system.domain`` | The user can operate on system domains


#### Return: `domains` as [SystemDomainAdmin](#structure-system-domain-admin)


-----------------------------------
<a id="patch-system-admin-theme-set"></a>
## **PATCH**&nbsp;`/system/admin/theme/set`&nbsp;- Set the system theme

Changes something in the system theme.



 | Name    | Type           | req | Description     
 | ------- | -------------- | - | ----------------
 | changes | json           |  | the main changes


#### Permissions: 
 | name             | description                      
 | ---------------- | ---------------------------------
 | ``system.theme`` | The user can manage system themes


#### Return: `theme` as [SystemTheme](#structure-system-theme)


-----------------------------------
<a id="get-system-theme-get"></a>
## **GET**&nbsp;`/system/theme/get`&nbsp;- Returns the current theme




 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: `theme` as [SystemTheme](#structure-system-theme)


-----------------------------------
<a id="patch-system-admin-reset-id"></a>
## **PATCH**&nbsp;`/system/admin/reset/id`&nbsp;- Force an id to be changed on the system

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


#### Return: `id` as str


-----------------------------------
<a id="post-system-email-test"></a>
## **POST**&nbsp;`/system/email/test`&nbsp;- Test email sending

This endpoint tests email sending.

You can specify the destination email address to send the message to, but the message itself is defined by the app.


 | Name  | Type           | req   | Description              
 | ----- | -------------- | ----- | -------------------------
 | email | str            | **Y** | Destination email address


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: `result` as boolean


-----------------------------------
<a id="get-system-admin-permissions-list"></a>
## **GET**&nbsp;`/system/admin/permissions/list`&nbsp;- Returns all permissions available on the system

Returns all the permissions available in the System.
The list depends also on the user's permissions:
- If the user has `system.admin`, the endpoint will return **all permissions** available
- if the user doesn't have `system.admin` the endpoint will return **only the permissions the user already has**.

Permissions are returned in an object with: `module name` as key and a string list of permissions available for that module.


 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: `permissions` as json


-----------------------------------
<a id="get-system-domain-current"></a>
## **GET**&nbsp;`/system/domain/current`&nbsp;- Returns the current active domain




 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: `domain` as [SystemDomainPublic](#structure-system-domain-public)

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


-----------------------------------
<a id="system_permissions_register"></a>
## system_permissions_register - Add module's permissions to the system

This function is called by every module during the initialization phase.
The module calls this function to pass its permissions and descriptions to the system.

This data is consumed by `/system/admin/permissions/list` endpoint

 | Name   | Type           | req   | Description           
 | ------ | -------------- | ----- | ----------------------
 | module | str            | **Y** | The module name       
 | perms  | json           | **Y** | The module permissions


#### Return: boolean
