# url_shortener
as the name says it shortens url from example from http://google.com to http://your_ip:some_port/s/fghhjkd

available methods:

POST /create

{

"url": "some_url.com"

}

it creates and returns short url

-----

GET /s/<the short generated sequence>
  
it redirects to whatever link was shortened by it
  
and adds to hit counter for the link
  
-----
  
GET /hit/<the short generated sequence>
  
it adds to number of hits on the link and returns to you how much the link was hit
  
-----
  
-----
  
-----
  
also there are test for creating link, checking for redirect and checking for non existing link
