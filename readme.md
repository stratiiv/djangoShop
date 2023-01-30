Using Django, Django REST frameworks create an application that allows to:

- (using Django admin) create a product with fields: name, category (FK), user (FK), price category field should be searchable.
- (using Django admin) create a category with fields: name
- (HTML page) retrieve products with the ability to filter by a category
- (using Django admin) retrieve all orders with the following data: user name, email, product name, category, price
- (HTML page, DRF) order a product leaving the following data: name, email. (Create an HTML page using Django forms that allow users to create an order. Also, create another HTML page that will look the same but will send data to the system using a jQuery POST request. You will need to create an endpoint for it).

* don't waste time on appearance
* each feature should have a separate URL
* you can use SQLite as DB
* a project should have only one migration