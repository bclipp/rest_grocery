## Grocery Store

The goal of this project is to have a a group of rest endpoints that allow's a user to 
* authenticate to google
* add items with price and row
* add shopper with address , CC and purchase history (food, date)
* MongoDB will be the data store
* Redis will be used to store the latest prices, loaded from MongoDB

## Setup

## URIs

* managers: id,store_id, first_name, last_name,ssn
    * GET
    * POST
    * PUT
    * DELETE

* items: id, price, store_id, name
    * GET
    * POST
    * PUT
    * DELETE
    
* customers: id, first_name, last_name, address, phone number
    * GET
    * POST
    * PUT
    * DELETE
    
*  purchases: id, customers_id, items_id
    * GET
    * POST
    * PUT
    * DELETE
    
* stores: id, address, managager_id
    * GET
    * POST
    * PUT
    * DELETE
    
## Requirements



