# Module: User

The `user` module is responsible of all the functions of the user handling.


## Index

### Types

 | Name                                                  | Description                                  
 | ----------------------------------------------------- | ---------------------------------------------
 | [User](#structure-user)                               | The main user table                          
 | [User2FA](#structure-user2-f-a)                       | Table to handle 2FA                          
 | [UserActivationCode](#structure-user-activation-code) | Activation code returned during registratrion
 | [UserDetails](#structure-user-details)                | User Details info                            
 | [UserFaceRec](#structure-user-face-rec)               | The Face Recognition info                    
 | [UserPerms](#structure-user-perms)                    | User permissions for a given module          
 | [UserRegistration](#structure-user-registration)      | Returned during registration process         
 | [UserSessionData](#structure-user-session-data)       | The user session info                        
 | [UserSmall](#structure-user-small)                    | The user minimum data                        

### Endpoints

 |            | Path                                                               | Description                                      
 | ---------- | ------------------------------------------------------------------ | -------------------------------------------------
 | **GET**    | [/user/2fa/start](#get-user-2fa-start)                             | Start a 2FA authentication                       
 | **POST**   | [/user/2fa/verify](#post-user-2fa-verify)                          | Verifies that 2FA is OK                          
 | **POST**   | [/user/admin/add](#post-user-admin-add)                            | Creates a new user in the system                 
 | **POST**   | [/user/admin/change/password](#post-user-admin-change-password)    | Change a user password                           
 | **DELETE** | [/user/admin/del](#delete-user-admin-del)                          | Deletes a user from the system                   
 | **PATCH**  | [/user/admin/fields](#patch-user-admin-fields)                     | Modifies single fields                           
 | **GET**    | [/user/admin/get](#get-user-admin-get)                             | Returns a user after a search                    
 | **GET**    | [/user/admin/list](#get-user-admin-list)                           | List users to the system                         
 | **POST**   | [/user/admin/relogin](#post-user-admin-relogin)                    | Login as a different user                        
 | **PATCH**  | [/user/admin/update](#patch-user-admin-update)                     | Updates a specified user                         
 | **POST**   | [/user/anonymous](#post-user-anonymous)                            | Creates an anonymous user session                
 | **POST**   | [/user/avatar](#post-user-avatar)                                  | Uploads user avatar                              
 | **PATCH**  | [/user/change/password](#patch-user-change-password)               | Changes the user password                        
 | **POST**   | [/user/del/app](#post-user-del-app)                                | Deletes an user from the app                     
 | **POST**   | [/user/facerec/add](#post-user-facerec-add)                        | Uploads user face                                
 | **GET**    | [/user/faces/get](#get-user-faces-get)                             | Gets all images for face recognition             
 | **GET**    | [/user/faces/modules](#get-user-faces-modules)                     | Load user faces modules                          
 | **GET**    | [/user/find](#get-user-find)                                       | Finds a user in the system                       
 | **POST**   | [/user/info_add](#post-user-info_add)                              | Adds more data to the user in the extra field    
 | **DELETE** | [/user/info_del](#delete-user-info_del)                            | Deletes a key from extra field                   
 | **POST**   | [/user/login](#post-user-login)                                    | Standard user login                              
 | **POST**   | [/user/login/2fa](#post-user-login-2fa)                            | Login using 2FA                                  
 | **POST**   | [/user/login/metamask](#post-user-login-metamask)                  | User login by a remote service                   
 | **POST**   | [/user/login/remote](#post-user-login-remote)                      | User login by a remote service                   
 | **GET**    | [/user/logout](#get-user-logout)                                   | Logs out the current user                        
 | **GET**    | [/user/me](#get-user-me)                                           | Returns all the data of the currently logged user
 | **POST**   | [/user/password-forgot](#post-user-password-forgot)                | Start the 'Forgot password?' process             
 | **POST**   | [/user/password-forgot/app](#post-user-password-forgot-app)        | Start the 'Forgot password?' process in App Mode 
 | **POST**   | [/user/password-reset](#post-user-password-reset)                  | Reset the password                               
 | **POST**   | [/user/perms_set](#post-user-perms_set)                            | Sets the user permissions                        
 | **GET**    | [/user/perms/get](#get-user-perms-get)                             | Gets permissions for the specified user          
 | **PATCH**  | [/user/profile](#patch-user-profile)                               | Changes data to the user profile                 
 | **POST**   | [/user/register](#post-user-register)                              | Start the registration process                   
 | **GET**    | [/user/register/activate/:code](#get-user-register-activate-:code) | Activate the user                                
 | **POST**   | [/user/register/app](#post-user-register-app)                      | Register a user using 3rd party app              
 | **GET**    | [/user/remove/me](#get-user-remove-me)                             | Removes the current user from system             
 | **PATCH**  | [/user/set/billing](#patch-user-set-billing)                       | Creates / update user billing info               
 | **PATCH**  | [/user/set/bio](#patch-user-set-bio)                               | Creates / update users bio                       
 | **POST**   | [/user/tag](#post-user-tag)                                        | Tag an user                                      
 | **GET**    | [/user/test/create](#get-user-test-create)                         | Creates a demo user                              
 | **POST**   | [/user/token](#post-user-token)                                    | User authentication with OAuth2                  
 | **PATCH**  | [/user/update](#patch-user-update)                                 | Updates the user data                            
 | **POST**   | [/user/upload2face](#post-user-upload2face)                        | Assigns an upload as a face to the user          

### Functions

 | Name                                        | Description                                                                                                                                                                                                           
 | ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 | [user_db_init](#user_db_init)               | This function initializes the module database tables.
                                                                                                                                                                
 | [user_facerec_get](#user_facerec_get)       | Gets all Face Recs binded to a user                                                                                                                                                                                   
 | [user_get_by_group](#user_get_by_group)     | Returns all the users belonging to the specified group                                                                                                                                                                
 | [user_session_create](#user_session_create) | This function creates a new entry in the sessions collection.

If a session for the given user already exists, it will be deleted.

**NOTE** There cannot be more than one session for a given user / email at a time.
 | [user_session_del](#user_session_del)       | Removes a session from the system.                                                                                                                                                                                    
 | [user_session_get](#user_session_get)       | This function retrieves the session from the sessions collection, using the JWT token provided.

If the session is expired or does not exists, an empty object is returned.                                           
 | [users_list](#users_list)                   | Returns all users in the system matching a specified query                                                                                                                                                            

	

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
 |  | email          | str |  |  | The user email                   


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
 | u | username       | str                                       |       |       |                                                               
 |   | name           | str                                       |       |       | User name                                                     
 |   | lastname       | str                                       |       |       | User lastname                                                 
 |   | perms          | json                                      |       |       | User permissions                                              
 | y | enabled        | boolean                                   |       |       | If the user can log in or not                                 
 |   | level          | num                                       |       |       | User level                                                    
 |   | password       | str                                       |       | **Y** | User login password                                           
 |   | code           | str                                       |       | **Y** | User unique code (used for registration and password recovery)
 |   | extra          | json                                      |       |       | Extra items for user details (jsoninzed)                      
 |   | language       | str                                       |       |       | Preferred language                                            
 | y | phone          | str                                       |       |       | The user main phone                                           
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
 | y | group          | str                                       |       |       | The user group                                                


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
 |   | id_user        | str  |       |  |                                    
 |   | nonce          | str  |       |  | The Nonce used for 2FA             
 |   | group          | str  |       |  | The user group                     
 |   | username       | str  |       |  | The user username                  


---------------------------------------
<a id="structure-user-perms"></a>
### UserPerms
User permissions for a given module


 | idx | Name           | Type  | req | priv | Description                                 
 | - | -------------- | ----- | - | - | --------------------------------------------
 |  | module_name    | str   |  |  | The module name of the permissions          
 |  | permissions    | str[] |  |  | The list of permissions for the given module


---------------------------------------
<a id="structure-user-details"></a>
### UserDetails
User Details info


 | idx | Name           | Type | req   | priv | Description      
 | - | -------------- | --- | ----- | - | -----------------
 | u | id             | str | **Y** |  | the main id field
 |   | username       | str |       |  |                  
 |   | name           | str |       |  | User name        
 |   | lastname       | str |       |  | User lastname    
 |   | email          | str |       |  | User email       
 |   | avatar         | str |       |  | User avatar path 


---------------------------------------
<a id="structure-user2-f-a"></a>
### User2FA
DB Table: `user_2fas` 

Table to handle 2FA


 | idx | Name           | Type    | req   | priv | Description               
 | - | -------------- | ------- | ----- | - | --------------------------
 | u | id_user        | str     | **Y** |  | The ID User               
 |   | twofactor      | str     |       |  | The 2FA code              
 |   | enabled        | boolean |       |  | If T, twofactor is enabled
 | y | nonce          | str     |       |  | The nonce code            


---------------------------------------
<a id="structure-user-small"></a>
### UserSmall
The user minimum data


 | idx | Name           | Type | req   | priv | Description        
 | - | -------------- | --- | ----- | - | -------------------
 | u | id             | str | **Y** |  | the main id field  
 |   | domain         | str | **Y** |  | The user domain    
 |   | name           | str | **Y** |  | The user first name
 |   | lastname       | str | **Y** |  | The user lastname  
 |   | username       | str | **Y** |  | The user username  
 |   | email          | str | **Y** |  | The user email     

# Endpoints

-----------------------------------
<a id="post-user-admin-add"></a>
## **POST**&nbsp;`/user/admin/add`&nbsp;- Creates a new user in the system

This endpoint creates a valid user in the system, bypassing registration and verification phases.



 | Name     | Type           | req   | Description                            
 | -------- | -------------- | ----- | ---------------------------------------
 | email    | str            | **Y** | The user email                         
 | password | str            | **Y** | The user password                      
 | username | str            | **Y** | The username                           
 | name     | str            |       | The user first name                    
 | lastname | str            |       | The user lastname                      
 | perms    | str[]          |       | User permissions                       
 | enabled  | boolean        |       | Flag T/F to know if the user is enabled
 | language | str            |       | The user language                      
 | group    | str            |       | The user group                         


#### Permissions: 
 | name            | description                       
 | --------------- | ----------------------------------
 | ``user.create`` | Permission to create / modify user


#### Return: `user` as [User](#structure-user)


-----------------------------------
<a id="patch-user-admin-update"></a>
## **PATCH**&nbsp;`/user/admin/update`&nbsp;- Updates a specified user




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


#### Return: `user` as [User](#structure-user)


-----------------------------------
<a id="delete-user-admin-del"></a>
## **DELETE**&nbsp;`/user/admin/del`&nbsp;- Deletes a user from the system

Deletes a user from the system


 | Name    | Type           | req   | Description              
 | ------- | -------------- | ----- | -------------------------
 | id_user | str            | **Y** | The user ID to be deleted


#### Permissions: 
 | name            | description                       
 | --------------- | ----------------------------------
 | ``user.create`` | Permission to create / modify user


#### Return: `id_user` as str


-----------------------------------
<a id="patch-user-admin-fields"></a>
## **PATCH**&nbsp;`/user/admin/fields`&nbsp;- Modifies single fields

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


#### Return: `user` as [User](#structure-user)


-----------------------------------
<a id="post-user-register"></a>
## **POST**&nbsp;`/user/register`&nbsp;- Start the registration process

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
 | phone     | str            |       | the user phone          
 | username  | str            |       | The user username       
 | group     | str            |       | The user group          


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: `uac` as [UserActivationCode](#structure-user-activation-code)


-----------------------------------
<a id="patch-user-update"></a>
## **PATCH**&nbsp;`/user/update`&nbsp;- Updates the user data

Updates user data.
You can specify one or more of the required fields.
Some fields, such as `email` and `username` are checked for uniqueness.

Only the user can update him/her self.


 | Name     | Type           | req | Description          
 | -------- | -------------- | - | ---------------------
 | email    | str            |  | the new user email   
 | password | str            |  | the user password    
 | name     | str            |  | the user name        
 | lastname | str            |  | the user lastname    
 | username | str            |  | the username         
 | group    | str            |  | The user group       
 | phone    | str            |  | The user phone number


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: `user` as [User](#structure-user)


-----------------------------------
<a id="post-user-avatar"></a>
## **POST**&nbsp;`/user/avatar`&nbsp;- Uploads user avatar

Uploads a user avatar.
Only the user can update him/her self.


 | Name   | Type           | req   | Description         
 | ------ | -------------- | ----- | --------------------
 | avatar | file           | **Y** | The user avatar file


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: `user` as [User](#structure-user)


-----------------------------------
<a id="post-user-facerec-add"></a>
## **POST**&nbsp;`/user/facerec/add`&nbsp;- Uploads user face

Uploads a user face for face recognition.

Only the user can update him/her self.


 | Name | Type           | req   | Description        
 | ---- | -------------- | ----- | -------------------
 | face | file           | **Y** | the user face photo


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: `facerec` as [UserFaceRec](#structure-user-face-rec)


-----------------------------------
<a id="post-user-password-forgot"></a>
## **POST**&nbsp;`/user/password-forgot`&nbsp;- Start the 'Forgot password?' process

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


#### Return: `uac` as str


-----------------------------------
<a id="post-user-password-reset"></a>
## **POST**&nbsp;`/user/password-reset`&nbsp;- Reset the password

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


#### Return: `ok` as boolean


-----------------------------------
<a id="get-user-register-activate-:code"></a>
## **GET**&nbsp;`/user/register/activate/:code`&nbsp;- Activate the user

This is the activation request.


 | Name | Type           | req   | Description                                           
 | ---- | -------------- | ----- | ------------------------------------------------------
 | code | str            | **Y** | the activation code returned by the /api/register call


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: `user` as [User](#structure-user)


-----------------------------------
<a id="post-user-tag"></a>
## **POST**&nbsp;`/user/tag`&nbsp;- Tag an user

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


#### Return: `user` as [User](#structure-user)


-----------------------------------
<a id="post-user-token"></a>
## **POST**&nbsp;`/user/token`&nbsp;- User authentication with OAuth2

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


#### Return: `__plain__` as [UserSessionData](#structure-user-session-data)


-----------------------------------
<a id="post-user-login"></a>
## **POST**&nbsp;`/user/login`&nbsp;- Standard user login

This endpoint implements the user authentication with ``email`` or ``username`` and ``password`` field.

The call must provide also ``recaptcha`` or ``challenge`` in order to verify the validity of the call. \
You don't have to provide both, but one is mandatory.

If the user is known, a JWT token with the running session is returned to the system.


 | Name      | Type           | req   | Description                    
 | --------- | -------------- | ----- | -------------------------------
 | password  | str            | **Y** | the user password              
 | email     | str            |       | The user email                 
 | username  | str            |       | The username                   
 | recaptcha | str            |       | The recaptcha check code       
 | challenge | str            |       | The challenge verification code


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: `__plain__` as [UserSessionData](#structure-user-session-data)


-----------------------------------
<a id="post-user-login-remote"></a>
## **POST**&nbsp;`/user/login/remote`&nbsp;- User login by a remote service

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


#### Return: `__plain__` as [UserSessionData](#structure-user-session-data)


-----------------------------------
<a id="get-user-admin-list"></a>
## **GET**&nbsp;`/user/admin/list`&nbsp;- List users to the system

Returns all user registered to the system.

If `domain` is specified, the list is filtered by domain.

If the user does not have the `system.admin` permission, only the users by his `domain` will be shown.

If `tag` is specified, the list is filtered by tag.


 | Name | Type           | req | Description          
 | --- | -------------- | - | ---------------------
 | tag | str            |  |  The tag to filter by


#### Permissions: 
 | name                 | description                       
 | -------------------- | ----------------------------------
 | ``user.create``      | Permission to create / modify user
 | ``user.group_owner`` | The user is the master of a Group 


#### Return: `users` as [User](#structure-user)


-----------------------------------
<a id="get-user-logout"></a>
## **GET**&nbsp;`/user/logout`&nbsp;- Logs out the current user

This endpoint logs out the current user



 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: `ok` as boolean


-----------------------------------
<a id="get-user-me"></a>
## **GET**&nbsp;`/user/me`&nbsp;- Returns all the data of the currently logged user

This endpoints returns all data related to the currently logged in user.



 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: `user` as [User](#structure-user)


-----------------------------------
<a id="post-user-perms_set"></a>
## **POST**&nbsp;`/user/perms_set`&nbsp;- Sets the user permissions

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


#### Return: `ok` as boolean


-----------------------------------
<a id="post-user-info_add"></a>
## **POST**&nbsp;`/user/info_add`&nbsp;- Adds more data to the user in the extra field

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


#### Return: `ok` as boolean


-----------------------------------
<a id="delete-user-info_del"></a>
## **DELETE**&nbsp;`/user/info_del`&nbsp;- Deletes a key from extra field

This endpoint deletes the specified `key` from the `extra` field.



 | Name | Type           | req   | Description            
 | --- | -------------- | ----- | -----------------------
 | key | str            | **Y** | The `key` to be deleted


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: `ok` as boolean


-----------------------------------
<a id="patch-user-profile"></a>
## **PATCH**&nbsp;`/user/profile`&nbsp;- Changes data to the user profile

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


#### Return: `user` as [User](#structure-user)


-----------------------------------
<a id="get-user-test-create"></a>
## **GET**&nbsp;`/user/test/create`&nbsp;- Creates a demo user

This endpoint creates a demo user



 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions: 
 | name            | description                       
 | --------------- | ----------------------------------
 | ``user.create`` | Permission to create / modify user


#### Return: `user` as [User](#structure-user)


-----------------------------------
<a id="patch-user-change-password"></a>
## **PATCH**&nbsp;`/user/change/password`&nbsp;- Changes the user password

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


#### Return: `ok` as boolean


-----------------------------------
<a id="patch-user-set-bio"></a>
## **PATCH**&nbsp;`/user/set/bio`&nbsp;- Creates / update users bio

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


#### Return: `user` as [User](#structure-user)


-----------------------------------
<a id="patch-user-set-billing"></a>
## **PATCH**&nbsp;`/user/set/billing`&nbsp;- Creates / update user billing info

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


#### Return: `user` as [User](#structure-user)


-----------------------------------
<a id="post-user-login-metamask"></a>
## **POST**&nbsp;`/user/login/metamask`&nbsp;- User login by a remote service

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


#### Return: `__plain__` as [UserSessionData](#structure-user-session-data)


-----------------------------------
<a id="get-user-admin-get"></a>
## **GET**&nbsp;`/user/admin/get`&nbsp;- Returns a user after a search

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


#### Return: `user` as [User](#structure-user)


-----------------------------------
<a id="get-user-remove-me"></a>
## **GET**&nbsp;`/user/remove/me`&nbsp;- Removes the current user from system

This method removes the current user from the system


 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: `ok` as boolean


-----------------------------------
<a id="get-user-perms-get"></a>
## **GET**&nbsp;`/user/perms/get`&nbsp;- Gets permissions for the specified user

This endpoint set returns full user permissions.



 | Name    | Type           | req   | Description
 | ------- | -------------- | ----- | -----------
 | id_user | str            | **Y** | The user id


#### Permissions: 
 | name           | description                      
 | -------------- | ---------------------------------
 | ``user.perms`` | Permission to change user's perms


#### Return: `ok` as boolean


-----------------------------------
<a id="get-user-faces-get"></a>
## **GET**&nbsp;`/user/faces/get`&nbsp;- Gets all images for face recognition

Return all images available for face recognition

If the `id_user` is not specified, the current logged user faces are returned.

If the `id_user` is specified, but the user does not have the `user.create` permission, the `id_user` will be the one of the currently logged user.


 | Name    | Type           | req | Description                 
 | ------- | -------------- | - | ----------------------------
 | id_user | str            |  | The User ID to get faces for


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: `faces` as [UserFaceRec](#structure-user-face-rec)


-----------------------------------
<a id="post-user-upload2face"></a>
## **POST**&nbsp;`/user/upload2face`&nbsp;- Assigns an upload as a face to the user




 | Name      | Type           | req   | Description  
 | --------- | -------------- | ----- | -------------
 | id_upload | str            | **Y** | The ID Upload
 | id_user   | str            |       | The user id  


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: `face` as [UserFaceRec](#structure-user-face-rec)


-----------------------------------
<a id="get-user-faces-modules"></a>
## **GET**&nbsp;`/user/faces/modules`&nbsp;- Load user faces modules




 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: `ok` as boolean


-----------------------------------
<a id="post-user-anonymous"></a>
## **POST**&nbsp;`/user/anonymous`&nbsp;- Creates an anonymous user session

This method is used when you need a temporary session for a user.
It creates a *real* user in the database, with fake data.

Users have a 24 hours life span, if not converted into "real" users, they are deleted.


 | Name      | Type           | req   | Description                
 | --------- | -------------- | ----- | ---------------------------
 | ts        | str            | **Y** | The generated random number
 | challenge | str            | **Y** | The challenge              


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: `user` as [User](#structure-user)


-----------------------------------
<a id="post-user-register-app"></a>
## **POST**&nbsp;`/user/register/app`&nbsp;- Register a user using 3rd party app

Start the registration process of the user replacing the rechapta with a challenge code.
The call creates an entry inside the database (if no error is encountered)

If in **debug mode** this functyion returns  the `UserActivationCode`




 | Name      | Type           | req   | Description        
 | --------- | -------------- | ----- | -------------------
 | email     | str            | **Y** | the new user email 
 | password  | str            | **Y** | the user password  
 | challenge | str            | **Y** | The challenge code 
 | name      | str            |       | the user first name
 | lastname  | str            |       | the user lastname  
 | phone     | str            |       | the user phone     
 | username  | str            |       | The user username  
 | group     | str            |       | The user group     


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: `uac` as [UserActivationCode](#structure-user-activation-code)


-----------------------------------
<a id="get-user-find"></a>
## **GET**&nbsp;`/user/find`&nbsp;- Finds a user in the system

This endpoints allows the search of a user in the system.

You can search only for one these fields at a time:

- `email`
- `username`

and both these fields are considered complete strings and not partials.

The `search` parameter will search in both fields at the same time.


 | Name   | Type           | req | Description   
 | ------ | -------------- | - | --------------
 | search | str            |  | The user email


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: `user` as [UserDetails](#structure-user-details)


-----------------------------------
<a id="post-user-password-forgot-app"></a>
## **POST**&nbsp;`/user/password-forgot/app`&nbsp;- Start the 'Forgot password?' process in App Mode

Start the 'Password forgotten' process for the user in App Mode, where the reCaptcha cannot be used.
This password-forgot takes the `username` that will be checked against both `username` and `email` fields.

The call creates a temporary token for the user that is emailed to the user.

In **debug mode**  returns to the user the activation code as  ``str`` inside ``uac``.


 | Name      | Type           | req   | Description             
 | --------- | -------------- | ----- | ------------------------
 | username  | str            | **Y** | the username of the user
 | challenge | str            | **Y** | the challenge code      


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: `uac` as [UserActivationCode](#structure-user-activation-code)


-----------------------------------
<a id="post-user-del-app"></a>
## **POST**&nbsp;`/user/del/app`&nbsp;- Deletes an user from the app

Deletes a user from the app, providing a challenge.
The user can only remove him/her self.


 | Name      | Type           | req   | Description              
 | --------- | -------------- | ----- | -------------------------
 | id_user   | str            | **Y** | The user id to be deleted
 | username  | str            | **Y** | The username             
 | challenge | str            | **Y** | The request challenge    


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: `ok` as boolean


-----------------------------------
<a id="get-user-2fa-start"></a>
## **GET**&nbsp;`/user/2fa/start`&nbsp;- Start a 2FA authentication

This endpoint starts a new 2FA authentication process for the user.
It generates an internal key and stores it inside the `2fa` field of the user


 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: `url` as str


-----------------------------------
<a id="post-user-login-2fa"></a>
## **POST**&nbsp;`/user/login/2fa`&nbsp;- Login using 2FA

Completes the login process by providing the 2FA challenge value


 | Name  | Type           | req   | Description   
 | ----- | -------------- | ----- | --------------
 | id    | str            | **Y** | The user id   
 | code  | str            | **Y** | The 2FA code  
 | nonce | str            | **Y** | The nonce code


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: `__plain__` as [UserSessionData](#structure-user-session-data)


-----------------------------------
<a id="post-user-2fa-verify"></a>
## **POST**&nbsp;`/user/2fa/verify`&nbsp;- Verifies that 2FA is OK

Used to verify the 2FA activation for a new user.
The user must be logged in to use this call.



 | Name | Type           | req   | Description              
 | ---- | -------------- | ----- | -------------------------
 | code | str            | **Y** | The 2FA verification code


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: `ok` as boolean


-----------------------------------
<a id="post-user-admin-change-password"></a>
## **POST**&nbsp;`/user/admin/change/password`&nbsp;- Change a user password

This is an enpoint that can help admins to change user password when needed.


 | Name     | Type           | req   | Description                          
 | -------- | -------------- | ----- | -------------------------------------
 | id_user  | str            | **Y** | The user id to change the password to
 | password | str            | **Y** | The new password                     


#### Permissions: 
 | name              | description               
 | ----------------- | --------------------------
 | ``user.password`` | Can change a user password


#### Return: `ok` as boolean


-----------------------------------
<a id="post-user-admin-relogin"></a>
## **POST**&nbsp;`/user/admin/relogin`&nbsp;- Login as a different user

This endpoint allows a user to login to the system as a different user, without using login and password.



 | Name    | Type           | req   | Description              
 | ------- | -------------- | ----- | -------------------------
 | id_user | str            | **Y** | The user ID to login into


#### Permissions: 
 | name                     | description              
 | ------------------------ | -------------------------
 | ``user.change_identity`` | Can login as another user


#### Return: `__plain__` as [UserSessionData](#structure-user-session-data)

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


-----------------------------------
<a id="user_get_by_group"></a>
## user_get_by_group - Returns a list of users by group

Returns all the users belonging to the specified group

 | Name  | Type           | req   | Description      
 | ----- | -------------- | ----- | -----------------
 | req   | ilrequest      | **Y** | the Request field
 | group | str            | **Y** | The group        


#### Return: [User](#structure-user)


-----------------------------------
<a id="users_list"></a>
## users_list - List all users

Returns all users in the system matching a specified query

 | Name  | Type           | req   | Description         
 | ----- | -------------- | ----- | --------------------
 | req   | ilrequest      | **Y** | the Request field   
 | query | json           |       | The query conditions


#### Return: [User](#structure-user)
