# Entities and Relationships

## Product

A product represents an item sold by the business.

Attributes:

* Product ID
* Product Name
* Category
* Price

## Customer

A customer is an individual or organization purchasing products.

Attributes:

* Customer ID
* Name
* Customer Type
* City

## Supplier

A supplier provides products to the business.

Attributes:

* Supplier ID
* Supplier Name
* Product Category
* Supplier Rating

## Inventory

Inventory represents the quantity of products currently available.

Attributes:

* Product ID
* Quantity
* Reorder Level
* Reorder Quantity

## Order

An order represents a customer's request to purchase one or more products.

An order contains:

* Order ID
* Customer ID
* Product ID
* Quantity
* Order Status

## Payment

Payment represents the financial transaction associated with an order.

Attributes:

* Payment ID
* Order ID
* Amount
* Payment Status

## Relationships

The major relationships are:

Customer → places → Order

Order → contains → Product

Product → stored in → Inventory

Product → supplied by → Supplier

Order → has → Payment

These relationships allow the system to reason about the complete business process.
