***Settings***
Library    RequestsLibrary
Library    DataDriver     ./fixtures/csv/users.csv    dialect=excel
Test Template    Post User DDT       

*** Variables ***
${url}    https://petstore.swagger.io/v2/user
${content_type}    application/json   



*** Test Cases ***
TC001    ${user_id}    ${user_username}    ${user_firstName}   ${user_lastName}    ${user_email}   ${user_password}    ${user_phone}   ${user_userStatus}
TC002    ${user_id}    ${user_username}    ${user_firstName}   ${user_lastName}    ${user_email}   ${user_password}    ${user_phone}   ${user_userStatus}
TC003    ${user_id}    ${user_username}    ${user_firstName}   ${user_lastName}    ${user_email}   ${user_password}    ${user_phone}   ${user_userStatus}

*** Keywords ***
Post User DDT 
    [Arguments]    ${user_id}    ${user_username}    ${user_firstName}   ${user_lastName}    ${user_email}   ${user_password}    ${user_phone}   ${user_userStatus}
   
    ${headers}    Create Dictionary    Content-Type=${content_type}
    ${user_userStatus}    Convert To Integer    ${user_userStatus}
    ${body}    Create Dictionary    id=${user_id}    username=${user_username}    firstName=${user_firstName}   lastName=${user_lastName}
    ...    email=${user_email}   password=${user_password}    phone=${user_phone}   userStatus=${user_userStatus}
   
    ${response}    POST    ${url}    headers=${headers}    json=${body}
    ${response_body}    Set Variable    ${response.json()}
    Log To Console    ${response_body}
    
    Status Should Be    200
    Should Be Equal    ${response_body}[type]       unknown
    Should Be Equal    ${response_body}[message]    ${user_id}