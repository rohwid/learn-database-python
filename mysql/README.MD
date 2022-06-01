For this case there's an example's table with a table named `customers`. This comment uses to show the content of the table:

    SELECT * FROM `customers`;

# **Create the Table**

Create a new table named `products`.

    CREATE TABLE products (
        id INT,
        name STRING,
        prince MONEY
    );

Implement the `primary key` parameter to that table. The purpose of the `primary key` is to uniquely indentify the rows record inside the table. So, this section were need to add for `primary key` implementation.

    CREATE TABLE table_name (
        id INT,
        name STRING,
        price MONEY,
        PRIMARY KEY (id)
    );

Implement the `not null` parameter to that table. The purpose of the `not null` is to make one or more column of the table become required or must be fill. So, this section were need to add.

    CREATE TABLE products (
        id INT NOT NULL,
        name STRING,
        price MONEY,
        PRIMARY KEY (id)
    );

## **Insert the Data Into the Database**

There are some way to insert the value into the database table. This first way is **specifies both the column names and the value** like this:

    INSERT INTO table_name (column1, column2, column3, ...)
    VALUES (value1, value2, value3, ...);

But, If **you're adding values for all the columns of the table**, you don't need to specify the colummn names in the SQL query. However, make sure the order of the values is in the same order as the columns in the table. The INSERT INTO syntax would be as follows:

    INSERT INTO table_name
    VALUES (value1, value2, value3, ...);

For the example with the `products` database that created before, we try to insert some values into it. This first case is about to **insert the entire column or table content in one row**:

    INSERT INTO products
    VALUES (1, 'Pen', 1.23)

And this second case is about to **insert the values to some column or table content in one row**:

    INSERT INTO products (id, name)
    VALUES (2, 'Pencil')

And this thrid case is about to **insert the values to some column or table content in one row without id**. So, it will be lead into an **error**:

    INSERT INTO products (name, price)
    VALUES ('Ruler', 1.05)

# **Read the Data from the Table**

Read all the data from the database, here's the command to select all the data:

    SELECT column1, column2, ... FROM table_name

for the example:

    SELECT * FROM products

The next is select the specific column from the table:

    SELECT column1, column2, ... FROM table_name

for the example:

    SELECT name, price FROM products

If you want to select or read the data with specific value, here's the command:

    SELECT column1, column2, ... FROM table_name where condition

for the example:

    SELECT column1, column2, ... FROM products WHERE id=1

# **Updating Single Values and Adding Columns in SQL**

To update the values of the table, we can use this command to set the values of the table:

    UPDATE table_name
    SET column1 = value1, column2 = value2, ...
    WHERE condition

For the example:

    UPDATE products
    SET price = 0.8
    WHERE id=2

To insert new column into the table, we can use this command to insert new column into the table:

    ALTER TABLE table_name
    ADD column_name datatype;

For the example:

    ALTER TABLE products
    ADD stock INT

Then update the stock value:

    UPDATE products
    SET stock = 32
    WHERE id = 1

And
    
    UPDATE products
    SET stock = 12
    WHERE id = 2

# **Delete the Data from the Database**

To delete the data with specific condition from the database, we can use this command:

    DELETE FROM table_name
    WHERE condition

for the example:

    DELETE FROM products
    WHERE id=2

# **Understanding the SQL Relationships**

The main relationship in SQL usually use two commponent, here is:

## **Foreign Key**

Create new table to establish the relationship, here's the example:

    CREATE TABLE orders (
        id INT NOT NULL,
        order_number INT,
        customer_id INT,
        product_id INT,
        PRIMARY KEY (id),
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (product_id) REFERENCES products(id)
    )

So, the **foreign key** will be `customer_id` and `product_id`. Then, we can insert the values like this:

    INSERT INTO orders
    VALUES (1, 4362, 2, 1)

## **Joins**

In this example will be show only **the inner joins**. This example shows that the inner joins mean **select the values from different table and join it as a new table (only view, not create)**, which there are **some parameter that needed as rules to join**.

Here's the example in the **customers** side:

    SELECT orders.order_number, customers.first_name, customers.last_name, customers.address
    FROM orders
    INNER JOIN customers on orders.customer_id = customers.id

And in **product** side:

    SELECT orders.order_number, customers.first_name, customers.last_name, customers.address
    FROM orders
    INNER JOIN products on orders.product_id = products.id