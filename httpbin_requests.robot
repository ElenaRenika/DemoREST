*** Settings ***
 Library  HttpbinRequestLibrary.py

*** Test Cases *** 
Successful Authenticated With Valid Credentials
  [Template]  Basic Auth With Credentials 
  user  passwd  200

Invalid Login With Wrong Credentials
  [Template]  Basic Auth With Credentials
  aabbbcc  passwd  401
  user  111222333  401
  aabbbcc  111333  401
  ${EMPTY}  passwd  401
  user  ${EMPTY}  401

Right Count Of Lines In Stream Request
  [Template]  Stream Request 
  0  0  200
  2  2  200
  10  10  200
  100  100  200
  1111  100  200

Check Right Value Header
  [Template]  Check Get Request Header
  Connection  keep-alive  200
  Content-Type  application/json  200


*** Keywords ***
Basic Auth With Credentials
  [Arguments]  ${username}  ${password}  ${response_code}
   ${response} =  basic auth  http://httpbin.org  /basic-auth/user/passwd  ${username}  ${password}
  Should Be Equal As Strings   ${response.status_code}  ${response_code}    

Check Get Request Header  
  [Arguments]  ${header}  ${header_value}  ${response_code}
  ${response} =   get  http://httpbin.org  /get
  Should Be Equal As Strings   ${response.status_code}  ${response_code}
  Should Be Equal As Strings   ${response.headers[\'${header}\']}  ${header_value}

Stream Request 
  [Arguments]  ${param}  ${stream_count}  ${response_code}
  ${response} =  stream  http://httpbin.org  /stream/  ${param}
  Should Be Equal As Strings   ${response.status_code}  ${response_code} 
  ${count} =  stream count  http://httpbin.org  /stream/  ${param}
  Should Be Equal As Strings  ${count}  ${stream_count}
