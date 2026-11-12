from fastapi import FastAPI, Request 
#from fastapi.responses import HTMLResponse #This class helps us create servers that return HTML(visual) content to the end user
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory='templates') #Templates help us with creating a server that sends both json response as well as the HTML docs

posts: list[dict] = [
    {
        "id": 1, 
        "author": "Corey Schafer", 
        "title": "FastAPI is awesome", 
        "content": "This framework is really easy to use and is very fast",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2, 
        "author": "Jane Doe", 
        "title": "Python is great for web development", 
        "content": "Python is a versatile language that has many use cases across different sectors of software",
        "date_posted": "April 21, 2025",   
    },
] 

#response_class=HTMLResponse -> Helps us create API routes that return HTML content
#include_in_schema=False -> For removing non-JSON, visual routes from the "/docs" route because it won't be necessary, as we can already see that in webpages
@app.get("/", include_in_schema=False, name="home") #The app decorator in FastAPI is used to create routes in our web page
@app.get("/posts",include_in_schema=False, name="posts") #Stacking route decorators like this helps us return the same response on multiple routes 
# name= "home" and "posts" are explicit names given to the API routes to distinguish between similar routes
def home(request:Request):
    return templates.TemplateResponse(request,
                                      "home.html", 
                                      {"posts": posts,
                                       "title":"Home"})

@app.get("/api/posts")
def get_posts():
    return posts