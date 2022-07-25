#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sathwik
"""

#ORDERING THE ROUTES

from fastapi import FastAPI

app=FastAPI()

#static for admin order
@app.get("/user/admin")
def profile():
    return {"This is admin page"}



#dynamic for user order
@app.get("/user/{username}")
def profile(username):
    return {f"This is a profile page for {username}"}

#In this i went in a sequential order firstly i used to type for admin profile page
#and next i typed dynamic order for user profile

