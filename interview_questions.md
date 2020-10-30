# Interview Questions for Data Engineering

[Source](https://realpython.com/data-engineer-interview-questions-python/)

## Questions on Relational Databases

Databases are one of the most crucial components in system. Without them, there
can be no state and no history. It effects the loading time of webapps. 

New tools have been introduced:
- NoSQL
- Cache Databases
- Graph Databases
- NoSQL support in SQL databases

Invented to increase the speed at which databases process requests

### Relational vs Non-relational databases
A relational database is one where data is stored in the form of a table. Each
table has a schema, which is the columns and types a record is required to
have.

Each schema must have at least one primary key that uniquely identifies that
record. There cannot be any duplicate rows in your database. Each table can be
related to other tables using foreign keys. 

A change in a schema must be applied to all records. This can sometimes cause
breakages and big headaches during migrations. 

Non-relational databases tackle things in a different way. They are inherently
schema-less, which means that records can be saved with different schemas and
with a different, nested structure. Records can still have primary keys, but
a change in the schema is done on an entry-by-entry basis. 

You would need a perform a speed comparison test based on the type of function
being performed, you can choose `INSERT, UPDATE, DELETE` or another function. 

Databases also differ in scalability. A non-relational database may be less of
a headache to distribute. That's because a collection of related records can be
easily stored on a particular node. On the other hand, relational databases
require more thought and usually make use of a master-slave system

## SQLite Example
Convenient database that you can use on your local machine. The database is
a single file, which makes it ideal for prototyping purposes.

## SQL Aggregation Functions
Aggregation functions are those that perform a mathematical operation on
a result set. Some examples include AVG, COUNT, MIN, MAX and SUM. Often, you'll
need GROUP BY and HAVING clauses to complement these aggregations. One useful
aggregation function is AVG, which you can use to compute the mean of a given
result set

## Speeding up SQL Queries
Speeds depends on various factors, but is mostly affected by how many of each
of the following are present:
- Joins
- Aggregations
- Traversals
- Records

Multiple joins are quite expensive to perform on several tables because the
database also needs to cache the intermediate result. At this point, you might
start to think about how to increase your memory size

Speed is also affected by whether or not there are indices present in the
database. Indices are extremely important and allow you to quickly search
through a table and find a match for some column specified in the query.

## Debugging SQL Queries 
Most databases include an EXPLAIN QUERY PLAN that describes the steps the
database takes to execute the query. For SQLite, you can enable this
functionality by adding EXPLAIN QUERY PLAN in front of a SELECT statement

