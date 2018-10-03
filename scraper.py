# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
import urllib
import urllib2

headers = {
#   'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.13) Gecko/2009073022 Firefox/3.0.13',
    'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml; q=0.9,*/*; q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded'
}

formFields = (
   # the viewstate is actualy 800+ characters in length! I truncated it
   # for this sample code.  It can be lifted from the first page
   # obtained from the site.  It may be ok to hardcode this value, or
   # it may have to be refreshed each time / each day, by essentially
   # running an extra page request and parse, for this specific value.
   (r'__VSTATE', r'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'),

   # following are more of these ASP form fields
   (r'__VIEWSTATE', r''),
   (r'__EVENTVALIDATION', r'/wEWDwL+raDpAgKnpt8nAs3q+pQOAs3q/pQOAs3qgpUOAs3qhpUOAoPE36ANAve684YCAoOs79EIAoOs89EIAoOs99EIAoOs39EIAoOs49EIAoOs09EIAoSs99EI6IQ74SEV9n4XbtWm1rEbB6Ic3/M='),
   (r'ctl00_RadScriptManager1_HiddenField', ''), 
   (r'ctl00_tabTop_ClientState', ''), 
   (r'ctl00_ContentPlaceHolder1_menuMain_ClientState', ''),
   (r'ctl00_ContentPlaceHolder1_gridMain_ClientState', ''),
  
# Read in a page
html = scraperwiki.scrape("https://www.ahpra.gov.au/Registration/Registers-of-Practitioners.aspx")

# Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
