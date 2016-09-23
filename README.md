#seleniumScrape

Web scraping is an important process to gather required data.

Simply using python’s requests library alone to authenticate to Linkedin is near impossible due to Linkedin’s security and is considered a violation of their terms of service. Linkedin provides a pretty straightforward API with which to authenticate to and parse profile and company data, but they require vetted API access in order to carry out a keyword-based search. So in order to effectively scrape and parse Linkedin data efficiently, without the need to go through another client, the use of both Selenium and Beautiful Soup in tandem is required in this case. What makes Selenium so useful in this case is that it simulates web surfing via a browser and thus eliminates the need for non-browser-based authentication such as OAuth 2.0 or OAuth 1.0a.

I have created a brief sample Python module, called seleniumScrape, that shows the logic behind the discussed method. The script intentionally parses just a few details to demonstrate its functionality.

#datasctructures

I have implemented a convnetional binary search tree along with a method to find loop size of a linked list, if a loop exists.

#toCamelCase

A simple python utility that takes a string and outputs its camel case version, or - since no one has coined this term - it becomes "camelfied".  
