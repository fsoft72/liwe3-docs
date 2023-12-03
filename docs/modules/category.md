# Module: Category

The `category` module is responsible of all the functions of the category and subcategory management.


## Index

### Types

 | Name                                                | Description         
 | --------------------------------------------------- | --------------------
 | [Category](#structure-category)                     | A category in memory
 | [CategorySmallItem](#structure-category-small-item) |                     
 | [CategoryTreeItem](#structure-category-tree-item)   |                     

### Endpoints

 |            | Path                                                            | Description                     
 | ---------- | --------------------------------------------------------------- | --------------------------------
 | **POST**   | [/category/admin/add](#post-category-admin-add)                 | Adds a Category to the system   
 | **DELETE** | [/category/admin/del](#delete-category-admin-del)               | Deletes a Category              
 | **PATCH**  | [/category/admin/fields](#patch-category-admin-fields)          | Modifies a single field         
 | **GET**    | [/category/admin/list](#get-category-admin-list)                | List all categories             
 | **POST**   | [/category/admin/module/add](#post-category-admin-module-add)   | Adds a new module to a category 
 | **DELETE** | [/category/admin/module/del](#delete-category-admin-module-del) | Deletes a module from a category
 | **PATCH**  | [/category/admin/update](#patch-category-admin-update)          | Updates a catagory              
 | **GET**    | [/category/list](#get-category-list)                            | Returns the categories as a tree
 | **POST**   | [/category/slug/valid](#post-category-slug-valid)               | Checks if a slug is valid       
 | **GET**    | [/category/top/list](#get-category-top-list)                    | Returns the Top categories      

### Functions

 | Name                                  | Description                        
 | ------------------------------------- | -----------------------------------
 | [category_db_init](#category_db_init) | Initialize category database tables

	

# Types

---------------------------------------
<a id="structure-category"></a>
### Category
DB Table: `categories` 

A category in memory


 | idx | Name           | Type    | req   | priv  | Description                                                                                 
 | - | -------------- | ------- | ----- | ----- | --------------------------------------------------------------------------------------------
 | u | id             | str     | **Y** |       | the main id field                                                                           
 | y | domain         | str     |       | **Y** | The Domain name                                                                             
 | y | id_parent      | str     |       |       | If the category is a "sub category", the id_parent contains the id of the Category container
 | y | id_owner       | str     |       |       | User that created this category (and it is defined as 'owner')                              
 | y | is_folder      | boolean |       |       | A true / false flag defining if the current category is actually a folder                   
 |   | title          | str     |       |       | Category name                                                                               
 |   | description    | str     |       |       | Category description                                                                        
 |   | image          | str     |       |       | Category image id                                                                           
 |   | image_url      | str     |       |       | Category image URL                                                                          
 | u | slug           | str     |       |       | Category slug                                                                               
 | y | visible        | boolean |       |       | If the category is visible                                                                  
 | y | top            | boolean |       |       | This is a top category                                                                      
 | * | modules        | str[]   |       |       | tags for the type                                                                           


---------------------------------------
<a id="structure-category-tree-item"></a>
### CategoryTreeItem



 | idx | Name           | Type                              | req | priv | Description                                                                                 
 | - | -------------- | --------------------------------- | - | - | --------------------------------------------------------------------------------------------
 | u | id             | str                               |  |  | the main id field                                                                           
 |   | id_parent      | str                               |  |  | If the category is a "sub category", the id_parent contains the id of the Category container
 |   | id_owner       | str                               |  |  | User that created this category (and it is defined as 'owner')                              
 |   | is_folder      | boolean                           |  |  | A true / false flag defining if the current category is actually a folder                   
 |   | title          | str                               |  |  | Category name                                                                               
 |   | description    | str                               |  |  | Category description                                                                        
 |   | image          | str                               |  |  | Category image                                                                              
 |   | image_url      | str                               |  |  | Category image URL                                                                          
 |   | children       | [Category](#structure-category)[] |  |  | the children of this Tree Item                                                              
 |   | slug           | str                               |  |  | Slug                                                                                        


---------------------------------------
<a id="structure-category-small-item"></a>
### CategorySmallItem



 | idx | Name           | Type | req   | priv | Description         
 | - | -------------- | --- | ----- | - | --------------------
 | u | id             | str | **Y** |  | the main id field   
 |   | title          | str | **Y** |  | Category name       
 |   | description    | str | **Y** |  | Category description
 |   | image          | str | **Y** |  | Category image      
 |   | image_url      | str | **Y** |  | Category image URL  

# Endpoints

-----------------------------------
<a id="post-category-admin-add"></a>
## **POST**&nbsp;`/category/admin/add`&nbsp;- Adds a Category to the system

The call creates a category inside the system.

This function returns the full `Category` structure



 | Name        | Type           | req   | Description                              
 | ----------- | -------------- | ----- | -----------------------------------------
 | title       | str            | **Y** | Category title                           
 | slug        | str            | **Y** | Category slug                            
 | id_parent   | str            |       | the parent Category (if any)             
 | description | str            |       | Category description                     
 | modules     | str[]          |       | The Module(s) the category is included in
 | top         | boolean        |       | Flag T/F if Category is a TOP category   
 | visible     | boolean        |       | Flag T/F for category visibility         
 | image       | str            |       | The category image                       


#### Permissions: 
 | name                | description                 
 | ------------------- | ----------------------------
 | ``category.editor`` | The user can edit categories


#### Return: `category` as [Category](#structure-category)


-----------------------------------
<a id="patch-category-admin-update"></a>
## **PATCH**&nbsp;`/category/admin/update`&nbsp;- Updates a catagory

The call updates a category inside the system.

This function returns the full `Category` structure



 | Name        | Type           | req   | Description                           
 | ----------- | -------------- | ----- | --------------------------------------
 | id          | str            | **Y** | the Category ID to update             
 | id_parent   | str            |       | the parent Category (if any)          
 | title       | str            |       | Category title                        
 | slug        | str            |       | Category slug                         
 | description | str            |       | Category description                  
 | modules     | str[]          |       | The Module(s) the category is included
 | top         | boolean        |       | Flag T/F if Category is a TOP category
 | visible     | boolean        |       | If the category is visible or not     
 | image       | str            |       | The category image                    


#### Permissions: 
 | name                | description                 
 | ------------------- | ----------------------------
 | ``category.editor`` | The user can edit categories


#### Return: `category` as [Category](#structure-category)


-----------------------------------
<a id="patch-category-admin-fields"></a>
## **PATCH**&nbsp;`/category/admin/fields`&nbsp;- Modifies a single field

The call modifies a single field.

This function returns the full `Category` structure



 | Name | Type           | req   | Description               
 | ---- | -------------- | ----- | --------------------------
 | id   | str            | **Y** | The category ID           
 | data | json           | **Y** | The field / value to patch


#### Permissions: 
 | name                | description                 
 | ------------------- | ----------------------------
 | ``category.editor`` | The user can edit categories


#### Return: `category` as [Category](#structure-category)


-----------------------------------
<a id="get-category-admin-list"></a>
## **GET**&nbsp;`/category/admin/list`&nbsp;- List all categories

The call lists all categories in the system.

This function returns the full `Category[]` structure


 | Name        | Type           | req | Description                                  
 | ----------- | -------------- | - | ---------------------------------------------
 | parent_only | boolean        |  | If T, returns only the first level categories


#### Permissions: 
 | name                | description                 
 | ------------------- | ----------------------------
 | ``category.editor`` | The user can edit categories


#### Return: `categories` as [Category](#structure-category)


-----------------------------------
<a id="delete-category-admin-del"></a>
## **DELETE**&nbsp;`/category/admin/del`&nbsp;- Deletes a Category

This call deletes a category. If the category contains sub categories, all sub categories will be deleted as well, recursively.


 | Name | Type           | req   | Description                  
 | -- | -------------- | ----- | -----------------------------
 | id | str            | **Y** | Ths ID category to be deleted


#### Permissions: 
 | name                | description                 
 | ------------------- | ----------------------------
 | ``category.editor`` | The user can edit categories


#### Return: `id` as str


-----------------------------------
<a id="post-category-admin-module-add"></a>
## **POST**&nbsp;`/category/admin/module/add`&nbsp;- Adds a new module to a category

The call updates a category adding a new module.

This function returns the full `Category` structure



 | Name   | Type           | req   | Description              
 | ------ | -------------- | ----- | -------------------------
 | id     | str            | **Y** | the Category ID to update
 | module | str            | **Y** | The module to add        


#### Permissions: 
 | name                | description                 
 | ------------------- | ----------------------------
 | ``category.editor`` | The user can edit categories


#### Return: `category` as [Category](#structure-category)


-----------------------------------
<a id="delete-category-admin-module-del"></a>
## **DELETE**&nbsp;`/category/admin/module/del`&nbsp;- Deletes a module from a category

The call updates a category deleting a new module.

This function returns the full `Category` structure



 | Name   | Type           | req   | Description              
 | ------ | -------------- | ----- | -------------------------
 | id     | str            | **Y** | the Category ID to update
 | module | str            | **Y** | The module to be removed 


#### Permissions: 
 | name                | description                 
 | ------------------- | ----------------------------
 | ``category.editor`` | The user can edit categories


#### Return: `category` as [Category](#structure-category)


-----------------------------------
<a id="get-category-list"></a>
## **GET**&nbsp;`/category/list`&nbsp;- Returns the categories as a tree

This endpoint returns all the categories as a tree



 | Name        | Type           | req | Description             
 | ----------- | -------------- | - | ------------------------
 | id_category | str            |  | The starting id_category
 | module      | str            |  | The starting module     


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: `tree` as [CategoryTreeItem](#structure-category-tree-item)


-----------------------------------
<a id="get-category-top-list"></a>
## **GET**&nbsp;`/category/top/list`&nbsp;- Returns the Top categories

This endpoint returns all the top categories (parent)



 | Name   | Type           | req | Description                           
 | ------ | -------------- | - | --------------------------------------
 | module | str            |  | The starting module                   
 | limit  | num            |  | Maximum number of categories to return


#### Permissions: 
 | name       | description           
 | ---------- | ----------------------
 | ``public`` | Everyone can call this


#### Return: `categs` as [CategorySmallItem](#structure-category-small-item)


-----------------------------------
<a id="post-category-slug-valid"></a>
## **POST**&nbsp;`/category/slug/valid`&nbsp;- Checks if a slug is valid




 | Name | Type           | req   | Description                
 | ---- | -------------- | ----- | ---------------------------
 | slug | str            | **Y** | The slug to check          
 | id   | str            |       | The ID category (if exists)


#### Permissions: 
 | name                | description                 
 | ------------------- | ----------------------------
 | ``category.editor`` | The user can edit categories


#### Return: `ok` as boolean

# Functions

-----------------------------------
<a id="category_db_init"></a>
## category_db_init - Category init function

Initialize category database tables

 | Name | Type           | req   | Description     
 | ---- | -------------- | ----- | ----------------
 | liwe | iliwe          | **Y** | init category db


#### Return: boolean
