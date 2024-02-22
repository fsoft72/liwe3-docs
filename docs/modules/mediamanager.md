# Module: MediaManager



## Index

### Types

 | Name                                        | Description                              
 | ------------------------------------------- | -----------------------------------------
 | [Media](#structure-media)                   | The Media type                           
 | [MediaBind](#structure-media-bind)          | Describes which modules are using a media
 | [MediaFolder](#structure-media-folder)      | Collection of folders                    
 | [MediaTreeItem](#structure-media-tree-item) | A structure describing a MediaTree Item  

### Endpoints

 |            | Path                                                        | Description                       
 | ---------- | ----------------------------------------------------------- | ----------------------------------
 | **DELETE** | [/media/delete/items](#delete-media-delete-items)           | Deletes one or more items         
 | **POST**   | [/media/folder/create](#post-media-folder-create)           | Creates a new folder              
 | **DELETE** | [/media/folder/delete](#delete-media-folder-delete)         | Deletes a folder                  
 | **PATCH**  | [/media/folder/rename](#patch-media-folder-rename)          | Rename a folder                   
 | **GET**    | [/media/folder/root](#get-media-folder-root)                | Returns the root folder           
 | **GET**    | [/media/folders/tree](#get-media-folders-tree)              | Returns a tree of folders         
 | **GET**    | [/media/get](#get-media-get)                                | Gets a media by id                
 | **GET**    | [/media/get/latest](#get-media-get-latest)                  | Returns the latest loaded items   
 | **GET**    | [/media/list](#get-media-list)                              | List media                        
 | **PATCH**  | [/media/meta/update](#patch-media-meta-update)              | Update media metadata             
 | **GET**    | [/media/search](#get-media-search)                          |                                   
 | **POST**   | [/media/upload](#post-media-upload)                         | Uploads a single file             
 | **POST**   | [/media/upload/chunk/add](#post-media-upload-chunk-add)     | Adds a new chunk during the upload
 | **POST**   | [/media/upload/chunk/start](#post-media-upload-chunk-start) | Starts a new media chunked upload 

	

# Types

---------------------------------------
<a id="structure-media"></a>
### Media
DB Table: `mm_medias` 

The Media type


 | idx | Name              | Type    | req   | priv | Description                              
 | - | ----------------- | ------- | ----- | - | -----------------------------------------
 | u | id                | str     | **Y** |  | the main id field                        
 | y | domain            | str     |       |  |                                          
 | y | id_owner          | str     |       |  | The user id that uploaded this media     
 | y | id_folder         | str     |       |  | The folder containing this media         
 | y | title             | str     |       |  | Media title                              
 |   | name              | str     |       |  | Upload file name                         
 |   | original_filename | str     |       |  | The original uploaded file name          
 |   | mimetype          | str     |       |  | The file mimetype                        
 |   | thumbnail         | str     |       |  | The path of the generated thumbnail      
 |   | path              | str     |       |  | The uploaded path                        
 |   | filename          | str     |       |  | The uploaded filename                    
 |   | abs_path          | str     |       |  | The absolute path and filename           
 |   | size              | int     |       |  | File size in bytes                       
 |   | ext               | str     |       |  | File Extension                           
 | y | is_ready          | boolean |       |  | Flag T/F that tells if the media is ready
 |   | md5               | str     |       |  | MD5 file checksum                        
 | * | tags              | str[]   |       |  | tags for this media                      
 |   | lat               | str     |       |  | Latitude                                 
 |   | lng               | str     |       |  | Longitude                                
 |   | width             | int     |       |  | Width in pixels                          
 |   | height            | int     |       |  | Height in pixels                         
 | y | year              | int     |       |  | Year of creation of the media            
 | y | month             | int     |       |  | Month of creation of the media           
 | y | creation          | date    |       |  | Date of creation of the media            
 | y | orientation       | int     |       |  | If a photo is vertical or horizontal     
 |   | exif              | json    |       |  | Image EXIF metadata                      


---------------------------------------
<a id="structure-media-bind"></a>
### MediaBind
DB Table: `mm_bindings` 

Describes which modules are using a media


 | idx | Name           | Type | req   | priv | Description      
 | - | -------------- | --- | ----- | - | -----------------
 | u | id             | str | **Y** |  | the main id field
 |   | id_media       | str | **Y** |  |                  
 |   | id_object      | str | **Y** |  |                  
 |   | module         | str | **Y** |  |                  


---------------------------------------
<a id="structure-media-folder"></a>
### MediaFolder
DB Table: `mm_folders` 

Collection of folders


 | idx | Name           | Type  | req   | priv | Description                 
 | - | -------------- | ----- | ----- | - | ----------------------------
 | u | id             | str   | **Y** |  | the main id field           
 | y | domain         | str   |       |  | The domain                  
 |   | id_parent      | str   |       |  | The parent folder           
 |   | name           | str   | **Y** |  |                             
 |   | subfolders     | str[] |       |  | IDs of Media Folders        
 |   | medias         | str[] |       |  | IDs of Medias in this folder


---------------------------------------
<a id="structure-media-tree-item"></a>
### MediaTreeItem
A structure describing a MediaTree Item


 | idx | Name           | Type                                          | req   | priv | Description      
 | - | -------------- | --------------------------------------------- | ----- | - | -----------------
 | u | id             | str                                           | **Y** |  | the main id field
 |   | id_parent      | str                                           |       |  |                  
 |   | name           | str                                           | **Y** |  |                  
 |   | subfolders     | [MediaTreeItem](#structure-media-tree-item)[] | **Y** |  |                  

# Endpoints

-----------------------------------
<a id="post-media-upload-chunk-start"></a>
## **POST**&nbsp;`/media/upload/chunk/start`&nbsp;- Starts a new media chunked upload

Use this to start a new chunked upload.
The chunked upload is used to upload very big files.

This call will instruct the server to receive a new chunked file.
During this call you have to provide the original `filename` and the whole upload `size` in bytes.

The endpoint will return the `id_upload` that must be used for the next chunked transfer calls.


 | Name      | Type           | req   | Description                            
 | --------- | -------------- | ----- | ---------------------------------------
 | id_folder | str            | **Y** | The ID Folder where to upload the media
 | filename  | str            | **Y** | Original filename                      
 | size      | int            | **Y** | Complete file size in bytes            
 | title     | str            |       | The media title                        
 | tags      | str[]          |       | The media tags                         


#### Permissions: 
 | name             | description           
 | ---------------- | ----------------------
 | ``media.create`` | Can create a new media


#### Return: `id_upload` as str


-----------------------------------
<a id="post-media-upload-chunk-add"></a>
## **POST**&nbsp;`/media/upload/chunk/add`&nbsp;- Adds a new chunk during the upload

This call will add a new chunk to the file being uploaded.

In the query field you have to provide:

- `id_upload`:   the upload id you got with the `/media/upload/chunk/start` call
- `start`:  the start position of this chunk (in bytes)

In the `post` section, you have to provide an `application/octet-stream` of your binary chunk data.


 | Name      | Type           | req   | Description       
 | --------- | -------------- | ----- | ------------------
 | id_upload | str            | **Y** | The id_upload     
 | start     | int            | **Y** | The starting point


#### Permissions: 
 | name             | description           
 | ---------------- | ----------------------
 | ``media.create`` | Can create a new media


#### Return: `bytes` as int


-----------------------------------
<a id="post-media-folder-create"></a>
## **POST**&nbsp;`/media/folder/create`&nbsp;- Creates a new folder

Creates a new folder


 | Name      | Type           | req   | Description      
 | --------- | -------------- | ----- | -----------------
 | id_parent | str            | **Y** | The parent folder
 | name      | str            | **Y** | The folder name  


#### Permissions: 
 | name             | description             
 | ---------------- | ------------------------
 | ``media.folder`` | Can create media folders


#### Return: `folder` as [MediaFolder](#structure-media-folder)


-----------------------------------
<a id="patch-media-folder-rename"></a>
## **PATCH**&nbsp;`/media/folder/rename`&nbsp;- Rename a folder

Renames a folder


 | Name      | Type           | req   | Description        
 | --------- | -------------- | ----- | -------------------
 | id_folder | str            | **Y** |                    
 | name      | str            | **Y** | The new folder name


#### Permissions: 
 | name             | description             
 | ---------------- | ------------------------
 | ``media.folder`` | Can create media folders


#### Return: `folder` as [MediaFolder](#structure-media-folder)


-----------------------------------
<a id="delete-media-folder-delete"></a>
## **DELETE**&nbsp;`/media/folder/delete`&nbsp;- Deletes a folder

This endpoint deletes the provided folder along with all the subfolders and all the media contained.


 | Name      | Type           | req   | Description            
 | --------- | -------------- | ----- | -----------------------
 | id_folder | str            | **Y** | The ID folder to delete


#### Permissions: 
 | name                    | description              
 | ----------------------- | -------------------------
 | ``media.folder_delete`` | Can delete a media folder


#### Return: `ok` as boolean


-----------------------------------
<a id="get-media-folder-root"></a>
## **GET**&nbsp;`/media/folder/root`&nbsp;- Returns the root folder

Returns the root folder (related to the user `domain`)


 | Name | Type           | req | Description
 | - | -------------- | - | -


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: `folder` as [MediaFolder](#structure-media-folder)


-----------------------------------
<a id="get-media-list"></a>
## **GET**&nbsp;`/media/list`&nbsp;- List media

This endpoints can returns all elements of the specified `id_folder`.

If `id_folder` is not specified, all media are returned.


 | Name       | Type           | req | Description                      
 | ---------- | -------------- | - | ---------------------------------
 | id_folders | str[]          |  | The ID Folders we want media from


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: `medias` as [Media](#structure-media)


-----------------------------------
<a id="get-media-get"></a>
## **GET**&nbsp;`/media/get`&nbsp;- Gets a media by id




 | Name | Type           | req   | Description 
 | -- | -------------- | ----- | ------------
 | id | str            | **Y** | The media ID


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: `media` as [Media](#structure-media)


-----------------------------------
<a id="get-media-folders-tree"></a>
## **GET**&nbsp;`/media/folders/tree`&nbsp;- Returns a tree of folders

Returns a tree of folders starting from the `id_folder` provided.

If not `id_folder` is provided, the `root` folder will be used.

The tree returned will contain all folders and subfolders, but not the files.


 | Name      | Type           | req | Description           
 | --------- | -------------- | - | ----------------------
 | id_folder | str            |  | The starting ID folder


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: `tree` as [MediaFolder](#structure-media-folder)


-----------------------------------
<a id="delete-media-delete-items"></a>
## **DELETE**&nbsp;`/media/delete/items`&nbsp;- Deletes one or more items

This endpoint deletes from the filesystem all the items specified inside the `medias`.\
Each item specified is the `id` of a media item


 | Name   | Type           | req   | Description                       
 | ------ | -------------- | ----- | ----------------------------------
 | medias | str[]          | **Y** | An array of ID media to be deleted


#### Permissions: 
 | name             | description       
 | ---------------- | ------------------
 | ``media.delete`` | Can delete a media


#### Return: `deleted` as int


-----------------------------------
<a id="post-media-upload"></a>
## **POST**&nbsp;`/media/upload`&nbsp;- Uploads a single file

This method allows the upload of one or more files, using the *classical* way of uploading of `POST` files.


 | Name      | Type           | req | Description                   
 | --------- | -------------- | - | ------------------------------
 | title     | str            |  | The media title               
 | module    | str            |  | The module the file belongs to
 | id_folder | str            |  | Destination Folder id         
 | tags      | str[]          |  | File tags                     


#### Permissions: 
 | name             | description           
 | ---------------- | ----------------------
 | ``media.create`` | Can create a new media


#### Return: `media` as [Media](#structure-media)


-----------------------------------
<a id="get-media-search"></a>
## **GET**&nbsp;`/media/search`&nbsp;- 

Performs a query for one or more of the given fields


 | Name  | Type           | req | Description            
 | ----- | -------------- | - | -----------------------
 | title | str            |  | Media title            
 | name  | str            |  | Media name             
 | type  | str            |  | Media type             
 | tags  | str[]          |  | Media tags             
 | year  | int            |  | Media creation year    
 | skip  | int            |  | Pagination start       
 | rows  | int            |  | How many rows to return


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: `medias` as [Media](#structure-media)


-----------------------------------
<a id="get-media-get-latest"></a>
## **GET**&nbsp;`/media/get/latest`&nbsp;- Returns the latest loaded items




 | Name | Type           | req | Description               
 | ---- | -------------- | - | --------------------------
 | skip | int            |  | The starting point        
 | rows | int            |  | How many items to retrieve


#### Permissions: 
 | name       | description                          
 | ---------- | -------------------------------------
 | ``logged`` | Only autheticated users can call this


#### Return: `medias` as [Media](#structure-media)


-----------------------------------
<a id="patch-media-meta-update"></a>
## **PATCH**&nbsp;`/media/meta/update`&nbsp;- Update media metadata

Updates the media metadata


 | Name  | Type           | req   | Description
 | ----- | -------------- | ----- | -----------
 | id    | str            | **Y** | Media id   
 | title | str            |       | Media title
 | tags  | str[]          |       | Media tags 


#### Permissions: 
 | name             | description           
 | ---------------- | ----------------------
 | ``media.create`` | Can create a new media


#### Return: `media` as [Media](#structure-media)

# Functions