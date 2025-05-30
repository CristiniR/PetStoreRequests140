***Settings***
Library    RequestsLibrary
Library    DataDriver     ./fixtures/csv/users.csv    dialect=excel
Test Template    Delete User DDT       

*** Variables ***
${content_type}    application/json   

*** Test Cases ***
TCD001    ${user_id}    ${user_username}    ${user_firstName}   ${user_lastName}    ${user_email}   ${user_password}    ${user_phone}   ${user_userStatus}

*** Keywords ***
Delete User DDT 
    [Arguments]    ${user_id}    ${user_username}    ${user_firstName}   ${user_lastName}    ${user_email}   ${user_password}    ${user_phone}   ${user_userStatus}
    ${headers}    Create Dictionary    Content-Type=${content_type} 
    ${url}    Set Variable    https://petstore.swagger.io/v2/user/${user_username}
    ${response}    DELETE    ${url}   headers=${headers}

    ${response_body}    Set Variable    ${response.json()}
    Log To Console    ${response_body}
    
    Status Should Be    200
    Should Be Equal    ${response_body}[type]       unknown
    Should Be Equal    ${response_body}[message]    ${user_username} 