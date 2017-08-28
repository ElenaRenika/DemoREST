#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, sys
import requests
from requests.auth import HTTPBasicAuth
#import robot

class HttpbinRequestLibrary(object):
    """ This is the simple library for testing three http-request methods 
        by using http://httpbin.org/ """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL' 

    def __init__(self):
        status = 'UNKNOWN'
        
    def basic_auth(self, server, uri, user, passwd):
        """ Send HTTP GET requests with HTTP Basic Authentification. 
        ``server`` Base HTTP server url.
        ``uri``   Endpoint.
        ``user``  Username for authentification
        ``passwd``  Password for authentification
        """
        try:
            response = requests.get(server+uri, auth=HTTPBasicAuth(user, passwd))
            return response
        except requests.exceptions.ConnectionError:
            print('Connection error occured.')
    
    def get(self, server, uri):
        """   Send HTTP Get requests.
        ``server`` Base HTTP server url.
        ``uri``   Endpoint.
        """
        try:
            response = requests.get(server+uri)
            return response
        except requests.exceptions.ConnectionError:
            print('Connection error occured.')
    
    def stream(self, server, uri, params): 
        """  Send HTTP Get requests with stream parameter.
        ``server`` Base HTTP server url.
        ``uri``   Endpoint.
        ``params``  Count lines.
        """ 
        try:
            response = requests.get(server+uri+str(params), stream=True)
            return response
        except requests.exceptions.ConnectionError:
            print('Connection error occured.')

    def stream_count(self, server, uri, params): 
        """ Get required count of lines from stream-request.
        ``server`` Base HTTP server url.
        ``uri``   Endpoint.
        ``params``  Count lines.
        """
        response = self.stream(server, uri, params)
        count = 0
        for line in response.iter_lines(): 
            if line:
                count += 1
        return count
            
