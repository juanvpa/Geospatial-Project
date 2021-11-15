# 

>## **GEOSPATIAL DATA PROJECT**


##### ![aquí había una imagen de la ciudad tecnológica perfecta]("tecnologica.jpeg","width="256",height="455")
# 

>### **GOAL**

#### The objective of this project is to determine the perfect location for a new company in the technology industry. 
#### The preferences of "my colleages" at the office were:

- **Designers** --> Want to be near to companies that do design.
- **Developers** --> Want to be near tech startups that have raised at least 1 Million dollars.
- **Executives** --> Like Starbucks.
- **Account managers** --> Travel a lot.
- **Average age between 25 and 40** --> Want some place to go party.
- **30% of the company** --> Have at least 1 child.
- **CEO** --> Is vegan.
- **Maintenance guy** --> Love to play basketball.
- **Dog—"Dobby"** --> Hairdresser every month. 
#

>### **OBJECTIVE**

#### Based on all the information given by the employees, propose and find the best city.
 1. San Francisco
 2. New York
 3. Beijing
 4. Madrid 
#

>### **WORKING PLAN**

####  On my last project I worked on Unicorn Companies around the world, in order to find which is the industry with more growth & find where they were born & raised.  
#### Find out that **San Francisco, New York & Beijing** were the cities with more Unicorns in the world. 
#### Let´s add Madrid and see wihich city match the better with the above information.
#

>### **STRUCTURE** 

#### Used the API Foursquare to find Nightlife Spot's, Basketball Court's, School's, Stations & Transport's.
#### Once all the information was downloaded in json format, I made a calculation of the distances between the coordinates of origin and the information obtained from Foursquare. 
#### For the final decision, I have decided to weigh according to the most relevant needs of my colleagues.
#### The following resources have been used to achieve the objective of this project: 

#### [Foursquare API](https://foursquare.com/): get access to global data and content from thousands trusted sources. To access all the necessary information about the resources surrounding the possible locations of the enterprise. 
#### [MongoDB](https://www.mongodb.com/): is a document database with the scalability and flexibility that we want using querying and indexing.
#

>### **STRUCTURE OF THE PROJECT FILES**

 1. A folder of notebooks: 
​
- #### **Foursquare API.ipynb** -> Called the Api of "Foursquare Developers", to find some of the preferences of my colleagues.
- #### **Geospatial queries.ipynb** -> Made the spatial queries to calculate the distance between each point obtained in the Foursquare API and the locations selected at the beginning.
 
 2. SRC folder:
 
 - #### Where all the .py files are stored with all the explained functions used during the project. 
 - #### The .py files included are: 
    - APIsFunctions used in the APIs.ipynb
    - GeospatialFunctions used in the Gespatial queries.ipynb
    - CleaningFunctions used in the Madrid vs Barcelona vs Bilbao vs Gijon.ipynb
​
 3. Output: all the dataframes imported and saved in csv format. 
​#

>### **Libraries**

- #### [sys](https://docs.python.org/3/library/sys.html)
- #### [requests](https://pypi.org/project/requests/2.7.0/)
- #### [pandas](https://pandas.pydata.org/)
- #### [dotenv](https://pypi.org/project/python-dotenv/)
- #### [pymongo](https://www.mongodb.com/2)
- #### [json](https://docs.python.org/3/library/json.html)
- #### [os](https://docs.python.org/3/library/os.html)
- #### [geopandas](https://geopandas.org/)
- #### [shapely](https://pypi.org/project/Shapely/)
- #### [reduce](https://docs.python.org/3/library/functools.html)
- #### [operator](https://docs.python.org/3/library/operator.html)
- #### [import dumps](https://pymongo.readthedocs.io/en/stable/api/bson/json_util.html)
- #### [re](https://docs.python.org/3/library/re.html)