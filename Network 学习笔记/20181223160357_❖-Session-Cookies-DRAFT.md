# ❖ Session & Cookies [DRAFT]

## DRAFT

- Cookies -> Mini K-V Database on client side, then server becomes visitor
- Session -> A specific row of data in the “Cookies DB”

Session is just a value of sessionID, as a temporary REFERENCE to userID. 

Reasons of using session:
- Identify the client’s userID without exposing it
- Check login status of a user:
    - client has sessionID: logged in
    - Doesn’t have: not logged in

Session storage:
- On server, AND 
- On client, as a cookie 



