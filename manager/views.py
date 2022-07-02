from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group,Permission

from .models import requesting
