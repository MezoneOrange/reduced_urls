# Website for reduced urls  
###### Diploma django project from "Python developer" course in programming school "IT technologies itProger"  

## In the site realised reduced users urls:  

- ### Creation and display reduced url links.

Each user has individual page with form for creation reduced urls. All links, that user had created, displaying on the page with creation form. Each user can see only those links that he has created. Also, he can to delete link which he not needed any more.

- ### Profile, registration, authorisation and password recovery.  

Site has a realisation of these functions. On the profile page user could change his data. If you want that works the password recovery function, you got to change the variables in `settings.py` (that displaying below) on yours.  

``
EMAIL_USE_TLS = True  
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_HOST_USER = 'mezorservice123@gmail.com'  
EMAIL_HOST_PASSWORD = 'dsfasdgdfafdss'  
EMAIL_PORT = 587  
``

- ### Also, was used java script for:
1. Display success messages for the 7 seconds. 
2. Change form background to red-color if form was invalid.

## On the website were used:
- Fonts: "Ubuntu", "PT Sans Narrow", "Lobster" from https://fonts.google.com/ .
- Styles: own-styles.

###### Creator: Dmitry Shelukhin

### P.S.

Many thanks to Georgy Dudar and programming school "IT technologies itProger" for learning and experience.
