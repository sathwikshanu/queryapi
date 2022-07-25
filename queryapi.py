#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sathwik
"""

from fastapi import FastAPI

app=FastAPI()

#query

@app.get("/products")
def products(id):
    return{f"product with an id:{id}"}



#multiple queries

@app.get("/productss")
def products(id, price):
    return {f"this is a product with an id:{id} and price {price}"}



#passing default values to query

@app.get("/productse")
def products(id=2,price=3):
    return {f"this is a product with an id:{id} and price{price}"}

#adding a validation logic

@app.get("/productsi")
def products(id:int=1,price:int=4):
    return {f"this is a product with an id:{id} and price {price}"}

#using path and query parameters simultaneously

@app.get("/profile/{id}/comments")
def profile(id:int,commentid:int):
    return {f"this is a profile page with an Id:{id} and comments{commentid}"}
