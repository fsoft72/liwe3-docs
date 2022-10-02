# Module: Upload

The `upload` module is responsible of all the file upload functionalities in the whole website.

## Index

### Types

 | Name                                         | Description
 | -------------------------------------------- | -------------------------------------
 | [Upload](#structure-upload)                  | Upload
 | [UploadExtended](#structure-upload-extended) | Upload Extended
 | [UploadReqData](#structure-upload-req-data)  | Upload Required Data
 | [UploadReqInfo](#structure-upload-req-info)  | Upload Required Info
 | [UploadSmall](#structure-upload-small)       | Upload reduced structure for listings

### Endpoints

 |            | Path                                         | Description
 | ---------- | -------------------------------------------- | ---------------------------------------------
 | **DELETE** | [/upload/del](#delete-upload-del)            | Deletes an Upload
 | **GET**    | [/upload/details](#get-upload-details)       | Get all info about a single Upload
 | **GET**    | [/upload/extensions](#get-upload-extensions) | Lists all available extensions
 | **POST**   | [/upload/file](#post-upload-file)            | Uploads a single file to the system
 | **GET**    | [/upload/get](#get-upload-get)               | Returns a file
 | **GET**    | [/upload/list](#get-upload-list)             | Lists available files
 | **POST**   | [/upload/multiple](#post-upload-multiple)    | Uploads multiple files
 | **POST**   | [/upload/tus/move](#post-upload-tus-move)    | Moves files from temp tus dir to uploader dir

### Functions

 | Name                                          | Description
 | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------
 | [upload_add_file](#upload_add_file)           | This function initializes the module database tables.
 | [upload_add_file_name](#upload_add_file_name) | This function initializes the module database tables.
 | [upload_db_init](#upload_db_init)             | This function initializes the module database tables.
 | [upload_del_file](#upload_del_file)           | This function removes a file from the Upload system.
 | [upload_list_small](#upload_list_small)       | This function lists all resources for the given `module` and `id_obj` and returns a list of `UploadSmall` items
 | [upload_move_file](#upload_move_file)         | This function moves the specified file.
 | [upload_req_info](#upload_req_info)           | This function gets some info from a file being uploaded.
 | [upload_req_info_file](#upload_req_info_file) | This function gets some info from a file being uploaded.



# Types

---------------------------------------
<a id="structure-upload"></a>
### Upload
DB Table: `uploads`

Upload

 | idx | Name              | Type | req   | priv  | Description
 | - | ----------------- | --- | ----- | ----- | ----------------------------------------------------------
 | u | id                | str | **Y** |       | the main id field
 | y | domain            | str |       | **Y** | The domain for the file
 | y | id_owner          | str |       |       | User that created this file (and it is defined as 'owner')
 | y | id_object         | str |       |       | ID of the object this upload is binded to
 | y | module            | str |       |       | The module name the `id_object` belongs to
 | y | name              | str |       |       | Upload file name
 | y | original_filename | str |       |       | The original uploaded file name
 |   | mimetype          | str |       |       | The file mimetype
 |   | thumbnail         | str |       |       | The path of the generated thumbnail
 |   | path              | str |       |       | The uploaded path
 |   | filename          | str |       |       | The uploaded filename
 |   | abs_path          | str |       |       | The absolute path and filename
 | y | size              | num |       |       | File size in bytes
 | y | ext               | str |       |       | File Extension


---------------------------------------
<a id="structure-upload-extended"></a>
### UploadExtended
Upload Extended

 | idx | Name              | Type                    | req   | priv | Description
 | - | ----------------- | ----------------------- | ----- | - | ------------------------------------------
 | u | id                | str                     | **Y** |  | the main id field
 |   | owner             | [User](#structure-user) |       |  | The upload owner
 |   | id_object         | str                     |       |  | ID of the object this upload is binded to
 |   | module            | str                     |       |  | The module name the `id_object` belongs to
 |   | name              | str                     |       |  | Upload file name
 |   | original_filename | str                     |       |  | The original uploaded file name
 |   | mimetype          | str                     |       |  | The file mimetype
 |   | thumbnail         | str                     |       |  | The path of the generated thumbnail
 |   | path              | str                     |       |  | The uploaded path
 |   | filename          | str                     |       |  | The uploaded filename
 |   | abs_path          | str                     |       |  | The absolute path and filename
 |   | size              | num                     |       |  | File size in bytes
 |   | ext               | str                     |       |  | File Extension
 |   | uploaded          | date                    |       |  | Date of when the file has been uploaded


---------------------------------------
<a id="structure-upload-req-info"></a>
### UploadReqInfo
Upload Required Info

 | idx | Name           | Type | req | priv | Description
 | - | -------------- | ---- | - | - | ----------------------
 |  | file           | file |  |  | The real file
 |  | path           | str  |  |  | The file fullpath
 |  | size           | num  |  |  | The file size in bytes
 |  | type           | str  |  |  | The file mimetype
 |  | name           | str  |  |  | The original file name
 |  | ext            | str  |  |  | The file extension


---------------------------------------
<a id="structure-upload-req-data"></a>
### UploadReqData
Upload Required Data

 | idx | Name           | Type | req | priv | Description
 | - | -------------- | --- | - | - | ---------------------------
 |  | path           | str |  |  | The file fullpath
 |  | name           | str |  |  | The original file name
 |  | full_filename  | str |  |  | The full original file name


---------------------------------------
<a id="structure-upload-small"></a>
### UploadSmall
Upload reduced structure for listings

 | idx | Name              | Type | req   | priv | Description
 | - | ----------------- | --- | ----- | - | -----------------------------------
 | u | id                | str | **Y** |  | the main id field
 | y | original_filename | str |       |  | The original uploaded file name
 |   | thumbnail         | str |       |  | The path of the generated thumbnail
 | y | size              | num |       |  | File size in bytes
 | y | ext               | str |       |  | File Extension

# Endpoints

-----------------------------------
<a id="post-upload-file"></a>
## **POST** /upload/file - Uploads a single file to the system

This function returns the full `Upload` structure.

 | Name   | Type           | req   | Description
 | ------ | -------------- | ----- | ------------------------------------------------
 | name   | str            | **Y** | The filename
 | file   | file           |       | The file must be inside the `file` field
 | id_obj | str            |       | the ID of the object this file will be binded to
 | module | str            |       | The module name the `id_obejct` refers


#### Permissions:
 | name           | description
 | -------------- | -----------------------------
 | ``upload.add`` | The user can add a new upload


#### Return: [Upload](#structure-upload) as `upload`


-----------------------------------
<a id="post-upload-multiple"></a>
## **POST** /upload/multiple - Uploads multiple files

Uploads multiple files at once in the system.

 | Name      | Type           | req | Description
 | --------- | -------------- | - | ----------------------------------------
 | files     | file           |  | The file must be inside the `file` field
 | module    | str            |  | The module name
 | md5_check | str            |  | The md5 hash of the file


#### Permissions:
 | name           | description
 | -------------- | -----------------------------
 | ``upload.add`` | The user can add a new upload


#### Return: [Upload](#structure-upload) as `uploads`


-----------------------------------
<a id="delete-upload-del"></a>
## **DELETE** /upload/del - Deletes an Upload

This call deletes an upload.

 | Name      | Type           | req   | Description
 | --------- | -------------- | ----- | ------------------------------
 | id_upload | str            | **Y** | The id of the upload to delete


#### Permissions:
 | name           | description
 | -------------- | -----------------------------
 | ``upload.del`` | The user can delete an upload


#### Return: str as `id`


-----------------------------------
<a id="get-upload-list"></a>
## **GET** /upload/list - Lists available files

This call shows available files.

Result can be filtered by `module`, `id_obj`, `id_user`, `mimetype`

 | Name     | Type           | req | Description
 | -------- | -------------- | - | ---------------
 | module   | str            |  | The module name
 | id_obj   | str            |  | The id_object
 | id_user  | str            |  | The user id
 | mimetype | str            |  | The mime type


#### Permissions:
 | name            | description
 | --------------- | -------------------------
 | ``upload.list`` | The user can list uploads


#### Return: [Upload](#structure-upload) as `uploads`


-----------------------------------
<a id="get-upload-extensions"></a>
## **GET** /upload/extensions - Lists all available extensions

This call returns all available extensions.

 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions:
 | name       | description
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: str as `extensions`


-----------------------------------
<a id="get-upload-details"></a>
## **GET** /upload/details - Get all info about a single Upload

Get all info about a single upload, specified by `id`.

 | Name | Type           | req   | Description
 | -- | -------------- | ----- | -------------
 | id | str            | **Y** | The upload ID


#### Permissions:
 | name       | description
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: [UploadExtended](#structure-upload-extended) as `upload`


-----------------------------------
<a id="get-upload-get"></a>
## **GET** /upload/get - Returns a file

This call returns a file by `id`.

 | Name | Type           | req   | Description
 | -- | -------------- | ----- | -------------
 | id | str            | **Y** | The upload ID


#### Permissions:
 | name       | description
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: str as `url`


-----------------------------------
<a id="post-upload-tus-move"></a>
## **POST** /upload/tus/move - Moves files from temp tus dir to uploader dir

This endpoint accepts a JSON with mappings of files uploaded by TUS and move them to the uploader dir. The data field contains a JSON with this format:

```json
{
        "module": "(module name)",
        "id_object": "(id_object)",
        "files": [
                {
                        "name": "(file_name)",
                        "tmp_name": "(tmp_file_name)",
                        "size": 1234
                }
        ]
}```

 | Name | Type           | req   | Description
 | ---- | -------------- | ----- | ---------------------------------------------
 | data | json           | **Y** | A json containing a list of files to be moved


#### Permissions:
 | name       | description
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: str as `ids`

# Functions

-----------------------------------
<a id="upload_del_file"></a>
## upload_del_file - Deletes an entry in the Upload

This function removes a file from the Upload system.

 | Name | Type           | req   | Description
 | -- | -------------- | ----- | -------------
 | id | str            | **Y** | The Upload ID


#### Return: boolean


-----------------------------------
<a id="upload_move_file"></a>
## upload_move_file - Moves the specified file

This function moves the specified file.

 | Name      | Type                                        | req   | Description
 | --------- | ------------------------------------------- | ----- | ---------------------------------------
 | req       | ilrequest                                   | **Y** | The request containing the `files` attr
 | u         | [Upload](#structure-upload)                 | **Y** | The upload object
 | u_info    | [UploadReqInfo](#structure-upload-req-info) | **Y** | The upload info object
 | dest_path | str                                         |       | The destination path
 | thumb     | boolean                                     |       | If T, a thumbnail is generated


#### Return: [Upload](#structure-upload)


-----------------------------------
<a id="upload_req_info_file"></a>
## upload_req_info_file - Returns info about an upload

This function gets some info from a file being uploaded.

 | Name | Type           | req   | Description
 | ---- | -------------- | ----- | ---------------------------------------
 | req  | ilrequest      | **Y** | The request containing the `files` attr
 | file | file           | **Y** | The file field


#### Return: [UploadReqInfo](#structure-upload-req-info)


-----------------------------------
<a id="upload_req_info"></a>
## upload_req_info - Returns info about an upload

This function gets some info from a file being uploaded.

 | Name       | Type           | req   | Description
 | ---------- | -------------- | ----- | ---------------------------------------
 | req        | ilrequest      | **Y** | The request containing the `files` attr
 | field_name | str            | **Y** | The field name


#### Return: [UploadReqInfo](#structure-upload-req-info)


-----------------------------------
<a id="upload_add_file"></a>
## upload_add_file - Adds a new file in the system

This function initializes the module database tables.

 | Name      | Type                        | req   | Description
 | --------- | --------------------------- | ----- | -------------------------------------------------------------
 | req       | ilrequest                   | **Y** | The request containing the `files` attr
 | file      | [Upload](#structure-upload) | **Y** | The file
 | module    | str                         | **Y** | The module related to this file
 | id_obj    | str                         | **Y** | The object related to this file
 | dest_path | str                         | **Y** | The destination path (partial)
 | file_name | str                         |       | The destination file name (if omitted, the name is generated)
 | thumb     | boolean                     |       | If T, a thumbnail is generated
 | name      | str                         |       | The new "public" filename (when file is downloaded)
 | owner     | str                         |       | If provided, it is the owner of the upload
 | md5_check | str                         |       | The md5 hash of the file


#### Return: [Upload](#structure-upload)


-----------------------------------
<a id="upload_add_file_name"></a>
## upload_add_file_name - Adds a new file in the system

This function initializes the module database tables.

 | Name       | Type           | req   | Description
 | ---------- | -------------- | ----- | -------------------------------------------------------------
 | req        | ilrequest      | **Y** | The request containing the `files` attr
 | field_name | str            | **Y** | The field name
 | module     | str            | **Y** | The module related to this file
 | id_obj     | str            | **Y** | The object related to this file
 | dest_path  | str            | **Y** | The destination path (partial)
 | file_name  | str            |       | The destination file name (if omitted, the name is generated)
 | thumb      | boolean        |       | If T, a thumbnail is generated
 | name       | str            |       | The new "public" filename (when file is downloaded)
 | owner      | str            |       | If provided, it is the owner of the upload


#### Return: [Upload](#structure-upload)


-----------------------------------
<a id="upload_db_init"></a>
## upload_db_init - Initializes upload module database

This function initializes the module database tables.

 | Name | Type           | req   | Description
 | ---- | -------------- | ----- | ----------------
 | liwe | iliwe          | **Y** | LiWE full config


#### Return: boolean


-----------------------------------
<a id="upload_list_small"></a>
## upload_list_small - List all resources for the given module/id_obj

This function lists all resources for the given `module` and `id_obj` and returns a list of `UploadSmall` items

 | Name   | Type           | req   | Description
 | ------ | -------------- | ----- | -----------------
 | req    | ilrequest      | **Y** | the Request field
 | module | str            | **Y** | The module name
 | id_obj | str            | **Y** | The id object


#### Return: [UploadSmall](#structure-upload-small)
