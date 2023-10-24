# Jitto OA
This repository contains code for the Jitto OA where it implements basic AWS lambdas to interact with 
a DynamoDB. The lambdas are built using Python 3.9. 

## Project Structure:
├── infrastructure &emsp;# Terraform to create the DynamoDB <br>
├── lambdas &emsp;&emsp;&emsp; # Lambdas <br>
├── .gitignore <br>
├── requirements.txt <br>
└── README.md

## Available APIs
Here are the endpoints available to use: <br>
https://rrt5z23mf6.execute-api.us-east-1.amazonaws.com/prod/dynamodb <br>
GET: returns a row with matching uuid <br>
eg: {uuid = "123masd-12asd"}

POST: adds an item with name and description to the table <br>
eg: {name = "example", description = "example item"}

https://rrt5z23mf6.execute-api.us-east-1.amazonaws.com/prod/get-all-rows <br>
GET: returns all rows currently in the table

To access these endpoints you need an API key. Users are limited to 100 requests a second and bursts of 50.
Users also are limited to 1000 requests a month

To add an API key, add to the header: `x-api-key` and then the key

## DynamoDB 
The primary key of the database is an uuid generated upon insert. The other fields are the name and description field 
