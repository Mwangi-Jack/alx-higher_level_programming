## 0x0D- SQL Introduction

### Database

An organized collection of structured information or data typically stored electronically in a computer system
It is usually controlled by a DBMS
They are widely divided into two;
  #### Relational Databases
   Data is organized in tables/entities and these tables are all in relation to each other
   - Examples; MySQL, Oracle, PostgreSQL and SQL server
#### Non-Relational Databases
They do not use the tabular schema of rows and columns
They use storage model that is optimizedfor the specific requirements of the type of data being stored
- Examples; MongoDB, Redis Couchbase    

A  solid database is expected to be ACID, which means it guarantees;
- <b>Atomicity</b>: if a transaction fails the result will be likeit neve happend
- <b>Consistency</b>: You can define rules for your data and expect  the data to abide by the rules, or else the transaction will fail
- <b>Isolation</b> : run two operations at the same time and expect the resultis as though they were run one after the other
- <b>Durability</b>: Unplug your server at any time, boot it back up, and it did not loose any data

The four operations that can be performed to data in database include;
- <b>C</b>: Create some data
- <b>R</b>: Read some data
- <b>U</b>: Update some data
- <b>D</b>: Delete some data

SQL Statments are divided into two major categories;
- Data Definition Language (DDL)
<br>
DDL statements are used to build and modify the structure of the tables and other objects in the database. Example 'CREATE' statement used to create a table
<br>
When a DDL statement is executed, it takes effect immediately

- Data Manipulation Language (DML)
<br>
DML statements are used to work with the data in tables, examples include, 'SELECT', 'INSERT', 'DELETE', 'UPDATE', 'COMMIT', 'ROLLBACK' etc


