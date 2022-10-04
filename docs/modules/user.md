# Module: User

The `user` module is responsible of all the functions of the user handling.


## Index

### Types

 | Name                                                  | Description                                  
 | ----------------------------------------------------- | ---------------------------------------------
 | [User](#structure-user)                               | The main user table                          
 | [UserActivationCode](#structure-user-activation-code) | Activation code returned during registratrion
 | [UserFaceRec](#structure-user-face-rec)               | The Face Recognition info                    
 | [UserPerms](#structure-user-perms)                    | User permissions for a given module          
 | [UserRegistration](#structure-user-registration)      | Returned during registration process         
 | [UserSessionData](#structure-user-session-data)       | The user session info                        

### Endpoints

 |            | Path                                                               | Description                                      
 | ---------- | ------------------------------------------------------------------ | -------------------------------------------------
 | **POST**   | [/user/admin/add](#post-user-admin-add)                            | Creates a new user in the system                 
 | **DELETE** | [/user/admin/del](#delete-user-admin-del)                          | Deletes a user from the system                   
 | **PATCH**  | [/user/admin/fields](#patch-user-admin-fields)                     | Modifies single fields                           
 | **GET**    | [/user/admin/get](#get-user-admin-get)                             | Returns a user after a search                    
 | **GET**    | [/user/admin/list](#get-user-admin-list)                           | List users to the system                         
 | **PATCH**  | [/user/admin/update](#patch-user-admin-update)                     | Updates a specified user                         
 | **POST**   | [/user/avatar](#post-user-avatar)                                  | Uploads user avatar                              
 | **PATCH**  | [/user/change/password](#patch-user-change-password)               | Changes the user password                        
 | **POST**   | [/user/facerec/add](#post-user-facerec-add)                        | Uploads user face                                
 | **POST**   | [/user/info_add](#post-user-info_add)                              | Adds more data to the user in the extra field    
 | **DELETE** | [/user/info_del](#delete-user-info_del)                            | Deletes a key from extra field                   
 | **POST**   | [/user/login](#post-user-login)                                    | Standard user login                              
 | **POST**   | [/user/login/metamask](#post-user-login-metamask)                  | User login by a remote service                   
 | **POST**   | [/user/login/remote](#post-user-login-remote)                      | User login by a remote service                   
 | **GET**    | [/user/logout](#get-user-logout)                                   | Logs out the current user                        
 | **GET**    | [/user/me](#get-user-me)                                           | Returns all the data of the currently logged user
 | **POST**   | [/user/password-forgot](#post-user-password-forgot)                | Start the 'Forgot password?' process             
 | **POST**   | [/user/password-reset](#post-user-password-reset)                  | Reset the password                               
 | **POST**   | [/user/perms_set](#post-user-perms_set)                            | Sets the user permissions                        
 | **PATCH**  | [/user/profile](#patch-user-profile)                               | Changes data to the user profile                 
 | **POST**   | [/user/register](#post-user-register)                              | Start the registration process                   
 | **GET**    | [/user/register/activate/:code](#get-user-register-activate-:code) | Activate the user                                
 | **GET**    | [/user/remove/me](#get-user-remove-me)                             | Removes the current user from system             
 | **PATCH**  | [/user/set/billing](#patch-user-set-billing)                       | Creates / update user billing info               
 | **PATCH**  | [/user/set/bio](#patch-user-set-bio)                               | Creates / update users bio                       
 | **POST**   | [/user/tag](#post-user-tag)                                        | Tag an user                                      
 | **GET**    | [/user/test/create](#get-user-test-create)                         | Creates a demo user                              
 | **POST**   | [/user/token](#post-user-token)                                    | User authentication with OAuth2                  
 | **PATCH**  | [/user/update](#patch-user-update)                                 | Updates the user data                            

### Functions

 | Name                                        | Description                                                                                                                                                                                                           
 | ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 | [user_db_init](#user_db_init)               | This function initializes the module database tables.
                                                                                                                                                                
 | [user_facerec_get](#user_facerec_get)       | Gets all Face Recs binded to a user                                                                                                                                                                                   
 | [user_session_create](#user_session_create) | This function creates a new entry in the sessions collection.

If a session for the given user already exists, it will be deleted.

**NOTE** There cannot be more than one session for a given user / email at a time.
 | [user_session_del](#user_session_del)       | Removes a session from the system.                                                                                                                                                                                    
 | [user_session_get](#user_session_get)       | This function retrieves the session from the sessions collection, using the JWT token provided.

If the session is expired or does not exists, an empty object is returned.                                           

	

# Types

---------------------------------------
<a id="structure-user-registration"></a>
### UserRegistration
Returned during registration process


 | idx | Name           | Type | req   | priv | Description      
 | - | -------------- | --- | ----- | - | -----------------
 |  | email          | str | **Y** |  | The user email   
 |  | password       | str | **Y** |  | The user password
 |  | name           | str |       |  | User first name  
 |  | lastname       | str |       |  | User lastname    


---------------------------------------
<a id="structure-user-activation-code"></a>
### UserActivationCode
Activation code returned during registratrion


 | idx | Name           | Type | req | priv | Description                      
 | - | -------------- | --- | - | - | ---------------------------------
 |  | code           | str |  |  | Temporary code to complete action


---------------------------------------
<a id="structure-user-face-rec"></a>
### UserFaceRec
DB Table: `user_facerecs` 

The Face Recognition info


 | idx | Name           | Type | req   | priv  | Description         
 | - | -------------- | --- | ----- | ----- | --------------------
 | u | id             | str | **Y** |       | the main id field   
 | y | domain         | str |       | **Y** | The domain code     
 | y | id_user        | str |       |       | The user id         
 | u | id_upload      | str |       |       | The upload image id 
 |   | filename       | str |       |       | The upload file name
 |   | path           | str |       |       | The upload path     


---------------------------------------
<a id="structure-user"></a>
### User
DB Table: `users` 

The main user table


 | idx | Name           | Type                                      | req   | priv  | Description                                                   
 | - | -------------- | ----------------------------------------- | ----- | ----- | --------------------------------------------------------------
 | u | id             | str                                       | **Y** |       | the main id field                                             
 | y | domain         | str                                       | **Y** | **Y** | The domain code                                               
 | u | email          | str                                       | **Y** |       | The user email                                                
 |   | name           | str                                       |       |       | User name                                                     
 |   | lastname       | str                                       |       |       | User lastname                                                 
 |   | perms          | json                                      |       |       | User permissions                                              
 | y | enabled        | boolean                                   |       |       | If the user can log in or not                                 
 |   | level          | num                                       |       |       | User level                                                    
 |   | password       | str                                       |       | **Y** | User login password                                           
 |   | code           | str                                       |       | **Y** | User unique code (used for registration and password recovery)
 |   | extra          | json                                      |       |       | Extra items for user details (jsoninzed)                      
 |   | language       | str                                       |       |       | Preferred language                                            
 |   | avatar         | str                                       |       |       | The user Avatar URL                                           
 | * | tags           | str[]                                     |       |       | tags for the type                                             
 | y | id_upload      | str                                       |       | **Y** | The id of the Upload object (for the avatar)                  
 | y | deleted        | date                                      |       | **Y** | The date when the user has been deleted                       
 |   | addresses      | [Address](#structure-address)[]           |       |       | Addresses binded to the user                                  
 |   | facebook       | str                                       |       |       | Facebook account                                              
 |   | twitter        | str                                       |       |       | Twitter account                                               
 |   | linkedin       | str                                       |       |       | Linkedin account                                              
 |   | instagram      | str                                       |       |       | Instagram account                                             
 |   | website        | str                                       |       |       | Website URL                                                   
 |   | tagline        | str                                       |       |       | User tagline                                                  
 |   | bio            | str                                       |       |       | User bio                                                      
 |   | faces          | [UserFaceRec](#structure-user-face-rec)[] |       |       | All users Face Rec info                                       
 |   | wallet         | str                                       |       |       | The wallet ID                                                 


---------------------------------------
<a id="structure-user-session-data"></a>
### UserSessionData
The user session info


 | idx | Name           | Type | req   | priv | Description                        
 | - | -------------- | ---- | ----- | - | -----------------------------------
 | u | id             | str  | **Y** |  | the main id field                  
 |   | access_token   | str  |       |  | The JWT access token               
 |   | name           | str  |       |  | The user name                      
 |   | lastname       | str  |       |  | The user lastname                  
 |   | avatar         | str  |       |  | The user avatar URL                
 |   | token_type     | str  |       |  | The token type (defaults to Bearer)
 |   | perms          | json |       |  | Array of user perms                
 |   | email          | str  |       |  | The user email                     


---------------------------------------
<a id="structure-user-perms"></a>
### UserPerms
User permissions for a given module


 | idx | Name           | Type  | req | priv | Description                                 
 | - | -------------- | ----- | - | - | --------------------------------------------
 |  | module_name    | str   |  |  | The module name of the permissions          
 |  | permissions    | str[] |  |  | The list of permissions for the given module

# Endpoints

-----------------------------------
<a id="post-user-admin-add"></a>
## **POST** /user/admin/add - Creates a new user in the system

This endpoint creates a valid user in the system, bypassing registration and verification phases.



 | Name     | Type           | req   | Description                            
 | -------- | -------------- | ----- | ---------------------------------------
 | email    | str            | **Y** | The user email                         
 | password | str            | **Y** | The user password                      
 | name     | str            |       | The user first name                    
 | lastname | str            |       | The user lastname                      
 | perms    | str[]          |       | User permissions                       
 | enabled  | boolean        |       | Flag T/F to know if the user is enabled
 | language | str            |       | The user language                      


#### Permissions: 
 | name            | description                       
 | --------------- | ----------------------------------
 | ``user.create`` | Permission to create / modify user


#### Return: [User](#structure-user) as `user`


-----------------------------------
<a id="patch-user-admin-update"></a>
## **PATCH** /user/admin/update - Updates a specified user




 | Name     | Type           | req   | Description                  
 | -------- | -------------- | ----- | -----------------------------
 | id       | str            | **Y** | The user id to be changed    
 | email    | str            |       | the new user email           
 | password | str            |       | the user password            
 | name     | str            |       | the user first name          
 | lastname | str            |       | the user lastname            
 | enabled  | boolean        |       | If the user is enabled or not
 | level    | num            |       | The user level               
 | language | str            |       | The user language            


#### Permissions: 
 | name            | description                       
 | --------------- | ----------------------------------
 | ``user.create`` | Permission to create / modify user


#### Return: [User](#structure-user) as `user`


-----------------------------------
<a id="delete-user-admin-del"></a>
## **DELETE** /user/admin/del - Deletes a user from the system

Deletes a user from the system


 | Name    | Type           | req   | Description              
 | ------- | -------------- | ----- | -------------------------
 | id_user | str            | **Y** | The user ID to be deleted


#### Permissions: 
 | name            | description                       
 | --------------- | ----------------------------------
 | ``user.create`` | Permission to create / modify user


#### Return: str as `id_user`


-----------------------------------
<a id="patch-user-admin-fields"></a>
## **PATCH** /user/admin/fields - Modifies single fields

The call modifies a single field.
This function returns the full `User` structure


 | Name | Type           | req   | Description               
 | ---- | -------------- | ----- | --------------------------
 | id   | str            | **Y** | the user id               
 | data | json           | **Y** | The field / value to patch


#### Permissions: 
 | name            | description                       
 | --------------- | ----------------------------------
 | ``user.create`` | Permission to create / modify user


#### Return: [User](#structure-user) as `user`


-----------------------------------
<a id="post-user-register"></a>
## **POST** /user/register - Start the registration process

Start the registration process of the user.
The call creates an entry inside the database (if no error is encountered)

If in **debug mode** this functyion returns  the `UserActivationCode`




 | Name      | Type           | req   | Description             
 | --------- | -------------- | ----- | ------------------------
 | email     | str            | **Y** | the new user email      
 | password  | str            | **Y** | the user password       
 | recaptcha | str            | **Y** | The recaptcha check code
 | name      | str            |       | the user first name     
 | lastname  | str            |       | the user lastname       


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: [UserActivationCode](#structure-user-activation-code) as `uac`


-----------------------------------
<a id="patch-user-update"></a>
## **PATCH** /user/update - Updates the user data

Updates user data.

Only the user can update him/her self.


 | Name     | Type           | req | Description       
 | -------- | -------------- | - | ------------------
 | email    | str            |  | the new user email
 | password | str            |  | the user password 
 | name     | str            |  | the user name     
 | lastname | str            |  | the user lastname 


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: [User](#structure-user) as `user`


-----------------------------------
<a id="post-user-avatar"></a>
## **POST** /user/avatar - Uploads user avatar

Uploads a user avatar.
Only the user can update him/her self.


 | Name   | Type           | req   | Description         
 | ------ | -------------- | ----- | --------------------
 | avatar | file           | **Y** | The user avatar file


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: [User](#structure-user) as `user`


-----------------------------------
<a id="post-user-facerec-add"></a>
## **POST** /user/facerec/add - Uploads user face

Uploads a user face for face recognition.

Only the user can update him/her self.


 | Name | Type           | req   | Description        
 | ---- | -------------- | ----- | -------------------
 | face | file           | **Y** | the user face photo


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: [UserFaceRec](#structure-user-face-rec) as `facerec`


-----------------------------------
<a id="post-user-password-forgot"></a>
## **POST** /user/password-forgot - Start the 'Forgot password?' process

Start the 'Password forgotten' process for the user.

The call creates a temporary token for the user.

In **debug mode**  returns to the user the activation code as  ``str`` inside ``uac``.


 | Name      | Type           | req   | Description                    
 | --------- | -------------- | ----- | -------------------------------
 | email     | str            | **Y** | the user email                 
 | recaptcha | str            | **Y** | the recaptcha verification code


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: str as `uac`


-----------------------------------
<a id="post-user-password-reset"></a>
## **POST** /user/password-reset - Reset the password

Resets the user password.



 | Name     | Type           | req   | Description        
 | -------- | -------------- | ----- | -------------------
 | email    | str            | **Y** | the user email     
 | code     | str            | **Y** | the activation code
 | password | str            | **Y** | the new password   


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: boolean as `ok`


-----------------------------------
<a id="get-user-register-activate-:code"></a>
## **GET** /user/register/activate/:code - Activate the user

This is the activation request.


 | Name | Type           | req   | Description                                           
 | ---- | -------------- | ----- | ------------------------------------------------------
 | code | str            | **Y** | the activation code returned by the /api/register call


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: [User](#structure-user) as `user`


-----------------------------------
<a id="post-user-tag"></a>
## **POST** /user/tag - Tag an user

This endpoint allows you to add tags to a user.



 | Name    | Type           | req   | Description                            
 | ------- | -------------- | ----- | ---------------------------------------
 | id_user | str            | **Y** | the user id                            
 | tags    | str[]          | **Y** |  A list of tags to be added to the user


#### Permissions: 
 | name            | description                       
 | --------------- | ----------------------------------
 | ``user.tag``    | Permission to modify user's tag   
 | ``user.create`` | Permission to create / modify user


#### Return: [User](#structure-user) as `user`


-----------------------------------
<a id="post-user-token"></a>
## **POST** /user/token - User authentication with OAuth2

This endpoint implements the user authentication with the ``OAuth2`` protocol.

If the user is known, a JWT token with the running session is returned to the system.



 | Name     | Type           | req   | Description                   
 | -------- | -------------- | ----- | ------------------------------
 | username | str            | **Y** | it must contain the user email
 | password | str            | **Y** | the user password             


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: [UserSessionData](#structure-user-session-data) as `__plain__`


-----------------------------------
<a id="post-user-login"></a>
## **POST** /user/login - Standard user login

This endpoint implements the user authentication with ``login`` and ``password``.

If the user is known, a JWT token with the running session is returned to the system.


 | Name      | Type           | req   | Description             
 | --------- | -------------- | ----- | ------------------------
 | email     | str            | **Y** | The user email          
 | password  | str            | **Y** | the user password       
 | recaptcha | str            | **Y** | The recaptcha check code


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: [UserSessionData](#structure-user-session-data) as `__plain__`


-----------------------------------
<a id="post-user-login-remote"></a>
## **POST** /user/login/remote - User login by a remote service

This endpoint logs in a user authenticated by a remote service.

Since this is a public call, the `challenge` parameter is used to verify that the call is from the correct service.

The `challenge` parameter is a `MD5` hash created composing (`email` + `name` + `remote_secret_key` as set in the `data.json` config file under `security / remote`).

The `avatar` parameter is optional and it can contain an absolute URL to an image avatar of the user.


 | Name      | Type           | req   | Description    
 | --------- | -------------- | ----- | ---------------
 | email     | str            | **Y** | The user email 
 | name      | str            | **Y** | The user name  
 | challenge | str            | **Y** | The challenge  
 | avatar    | str            |       | The user avatar


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: [UserSessionData](#structure-user-session-data) as `__plain__`


-----------------------------------
<a id="get-user-admin-list"></a>
## **GET** /user/admin/list - List users to the system

Returns all user registered to the system.

If `domain` is specified, the list is filtered by domain.

If the user does not have the `system.admin` permission, only the users by his `domain` will be shown.

If `tag` is specified, the list is filtered by tag.


 | Name | Type           | req | Description          
 | --- | -------------- | - | ---------------------
 | tag | str            |  |  The tag to filter by


#### Permissions: 
 | name            | description                       
 | --------------- | ----------------------------------
 | ``user.create`` | Permission to create / modify user


#### Return: [User](#structure-user) as `users`


-----------------------------------
<a id="get-user-logout"></a>
## **GET** /user/logout - Logs out the current user

This endpoint logs out the current user



 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: boolean as `ok`


-----------------------------------
<a id="get-user-me"></a>
## **GET** /user/me - Returns all the data of the currently logged user

This endpoints returns all data related to the currently logged in user.



 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: [User](#structure-user) as `user`


-----------------------------------
<a id="post-user-perms_set"></a>
## **POST** /user/perms_set - Sets the user permissions

This endpoint set the full user permissions.

The function will allow changing the permsissions only if the request comes from a logged user with the `user.perms` permission set.

If the  `system: [ 'admin' ]` permission is set to the user, it becomes a super user and can do **all** operations on the system.


 | Name    | Type                               | req   | Description                    
 | ------- | ---------------------------------- | ----- | -------------------------------
 | id_user | str                                | **Y** | The user id                    
 | perms   | [UserPerms](#structure-user-perms) | **Y** | A JSON of `UserPerms` structure


#### Permissions: 
 | name           | description                      
 | -------------- | ---------------------------------
 | ``user.perms`` | Permission to change user's perms


#### Return: boolean as `ok`


-----------------------------------
<a id="post-user-info_add"></a>
## **POST** /user/info_add - Adds more data to the user in the extra field

This endpoint adds extra information inside the `extra` field, under the `key` specified.

If `key` was already present in the `extra` field, everything in `key` will be overwritten.

New `key`s will be added to `extra`.

If `key` is omitted (passing `''`)  the data is added to the `extra` root.


 | Name | Type           | req   | Description             
 | ---- | -------------- | ----- | ------------------------
 | key  | str            | **Y** | the  main key           
 | data | json           | **Y** | the new data to be added


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: boolean as `ok`


-----------------------------------
<a id="delete-user-info_del"></a>
## **DELETE** /user/info_del - Deletes a key from extra field

This endpoint deletes the specified `key` from the `extra` field.



 | Name | Type           | req   | Description            
 | --- | -------------- | ----- | -----------------------
 | key | str            | **Y** | The `key` to be deleted


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: boolean as `ok`


-----------------------------------
<a id="patch-user-profile"></a>
## **PATCH** /user/profile - Changes data to the user profile

This is the first tab 'Profile' of the UserProfile interface.

You can change data only to the current loggedin user.


 | Name         | Type           | req | Description                 
 | ------------ | -------------- | - | ----------------------------
 | name         | str            |  | The user name               
 | lastname     | str            |  | The user lastname           
 | phone        | str            |  | User phone                  
 | email        | str            |  | user email                  
 | addr_street  | str            |  | Address street              
 | addr_nr      | str            |  | Address street number       
 | addr_zip     | str            |  | Address zip code            
 | addr_city    | str            |  | Address city                
 | addr_state   | str            |  | Address state (or probvince)
 | addr_country | str            |  | Address country             
 | facebook     | str            |  | Facebook user name          
 | twitter      | str            |  | Twitter user name           
 | linkedin     | str            |  | Linkedin user name          
 | instagram    | str            |  | Instagram user name         
 | website      | str            |  | User personal web site      


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: [User](#structure-user) as `user`


-----------------------------------
<a id="get-user-test-create"></a>
## **GET** /user/test/create - Creates a demo user

This endpoint creates a demo user



 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions: 
 | name            | description                       
 | --------------- | ----------------------------------
 | ``user.create`` | Permission to create / modify user


#### Return: [User](#structure-user) as `user`


-----------------------------------
<a id="patch-user-change-password"></a>
## **PATCH** /user/change/password - Changes the user password

This is the change password functionality for UserProfile tab.

You can change data only to the current loggedin user.


 | Name         | Type           | req   | Description                   
 | ------------ | -------------- | ----- | ------------------------------
 | old_password | str            | **Y** | the old password              
 | new_password | str            | **Y** | the new password              
 | recaptcha    | str            | **Y** | the recaptcha verfication code


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: boolean as `ok`


-----------------------------------
<a id="patch-user-set-bio"></a>
## **PATCH** /user/set/bio - Creates / update users bio

Use this endpoint to update user `bio` or `tagline` (or both).

The currently logged in user can only change his/her own data.


 | Name    | Type           | req | Description 
 | ------- | -------------- | - | ------------
 | tagline | str            |  | User tagline
 | bio     | str            |  | User bio    


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: [User](#structure-user) as `user`


-----------------------------------
<a id="patch-user-set-billing"></a>
## **PATCH** /user/set/billing - Creates / update user billing info

Creates / updates the user billing info.

You can change data only to the current loggedin user.


 | Name         | Type           | req | Description              
 | ------------ | -------------- | - | -------------------------
 | address      | str            |  | The street address       
 | nr           | str            |  | The street address number
 | name         | str            |  | Address name             
 | city         | str            |  | Address city             
 | zip          | str            |  | Address postal code      
 | state        | str            |  | Address state            
 | country      | str            |  | Address country          
 | company_name | str            |  | Company name             
 | fiscal_code  | str            |  | Fiscal code              
 | vat_number   | str            |  | VAT number               
 | sdi          | str            |  | SDI code                 
 | pec          | str            |  | PEC email                


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: [User](#structure-user) as `user`


-----------------------------------
<a id="post-user-login-metamask"></a>
## **POST** /user/login/metamask - User login by a remote service

This endpoint logs in a user authenticated by a remote service.

Since this is a public call, the `challenge` parameter is used to verify that the call is from the correct service.

The `challenge` parameter is a `MD5` hash created composing (`address` + `remote_secret_key` as set in the `data.json` config file under `security / remote`).


 | Name      | Type           | req   | Description       
 | --------- | -------------- | ----- | ------------------
 | address   | str            | **Y** | The wallet address
 | challenge | str            | **Y** | The challenge     


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: [UserSessionData](#structure-user-session-data) as `__plain__`


-----------------------------------
<a id="get-user-admin-get"></a>
## **GET** /user/admin/get - Returns a user after a search

This method can return a user after searching all users by some params.

Params are all optional, but at least one must be given, or the current user will be returned.

If the search returns more than one single user, only the first will be returned.


 | Name     | Type           | req | Description      
 | -------- | -------------- | - | -----------------
 | id       | str            |  | The user id      
 | email    | str            |  | The user email   
 | name     | str            |  | The user name    
 | lastname | str            |  | The user lastname


#### Permissions: 
 | name            | description                       
 | --------------- | ----------------------------------
 | ``user.create`` | Permission to create / modify user


#### Return: [User](#structure-user) as `user`


-----------------------------------
<a id="get-user-remove-me"></a>
## **GET** /user/remove/me - Removes the current user from system

This method removes the current user from the system


 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: boolean as `ok`

# Functions

-----------------------------------
<a id="user_db_init"></a>
## user_db_init - Initializes user module database

This function initializes the module database tables.


 | Name | Type           | req   | Description       
 | ---- | -------------- | ----- | ------------------
 | liwe | iliwe          | **Y** | LiWE full instance


#### Return: boolean


-----------------------------------
<a id="user_facerec_get"></a>
## user_facerec_get - Gets all Face Rec binded to a user

Gets all Face Recs binded to a user

 | Name    | Type           | req   | Description  
 | ------- | -------------- | ----- | -------------
 | req     | ilrequest      | **Y** | The ILRequest
 | id_user | str            | **Y** | ID user      


#### Return: [UserFaceRec](#structure-user-face-rec)


-----------------------------------
<a id="user_session_del"></a>
## user_session_del - Deletes a session of one user

Removes a session from the system.

 | Name | Type           | req   | Description    
 | --- | -------------- | ----- | ---------------
 | req | iliwe          | **Y** | The ILRequest  
 | key | str            | **Y** | The Session key


#### Return: boolean


-----------------------------------
<a id="user_session_get"></a>
## user_session_get - Returns a user session by the given Token

This function retrieves the session from the sessions collection, using the JWT token provided.

If the session is expired or does not exists, an empty object is returned.

 | Name | Type           | req   | Description                 
 | --- | -------------- | ----- | ----------------------------
 | req | ilrequest      | **Y** | The ILRequest               
 | tok | str            | **Y** | The JSON Web Token to decode


#### Return: any


-----------------------------------
<a id="user_session_create"></a>
## user_session_create - Creates a new session for the User

This function creates a new entry in the sessions collection.

If a session for the given user already exists, it will be deleted.

**NOTE** There cannot be more than one session for a given user / email at a time.

 | Name | Type                    | req   | Description                      
 | ---- | ----------------------- | ----- | ---------------------------------
 | req  | ilrequest               | **Y** | The ILRequest                    
 | user | [User](#structure-user) | **Y** | The user to create the session to


#### Return: str
