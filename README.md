# epstein-scraper

This project is intended to provide a simple means of accessing the justice department's release of the so-called "Epstein Files", which is mostly just a large data dump of PDF files.

[https://www.justice.gov/epstein/](https://www.justice.gov/epstein/)

The web portal forces the user to jump through several hoops in order to perform basic search.

Download functionality is not very easy from this perspective and neither is searching.

A quick reverse-engineer of the "protections" (lol) in place resulted in me writing a Python3 script that allows me to not only perform search using their API, but also retrieve the URIs of any files my searches result in, and also download them.

One of the "catches" to this process is you will need to bypass the "age restriction" at least once in order to obtain a valid cookie for this script, but it is very easy to do and I was basically done within 5 minutes...

-----

Some interesting notes about the infrastructure of justice.gov before I continue:

```
justice.gov.                 300     IN      A       172.65.90.26
justice.gov.                 300     IN      A       172.65.90.27
justice.gov.                 300     IN      A       172.65.90.24
justice.gov.                 300     IN      A       172.65.90.25
www.justice.gov.             600     IN      CNAME   www.justice.gov.edgekey.net.
www.justice.gov.edgekey.net. 300     IN      CNAME   e7598.dscb.akamaiedge.net.
e7598.dscb.akamaiedge.net.   20      IN      A       23.7.131.92
```

```
HTTP/2 200 OK
X-Amz-Id-2: adKovfn9hMpH7I2H7ecILoPnHhf4HdeX6P1m558X7jspioA59ybDtM3jU49ebNyI5sStjCJeyzK9D5Pigh7R6Nw7uH53K/98
X-Amz-Request-Id: YPY18XCFKD9GKDZN
Last-Modified: Fri, 30 Jan 2026 05:41:36 GMT
Etag: "6452b9162bf5590eb9ce8e1af9ba741c"
X-Amz-Server-Side-Encryption: AES256
X-Amz-Version-Id: null
Accept-Ranges: bytes
Content-Type: application/pdf
Content-Length: 47801
Server: AmazonS3
Expires: Wed, 04 Feb 2026 18:19:45 GMT
Cache-Control: max-age=0, no-cache, no-store
Pragma: no-cache
Date: Wed, 04 Feb 2026 18:19:45 GMT
Alt-Svc: h3=":443"; ma=93600
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-Queueit-Connector: akamai
Set-Cookie: QueueITAccepted-SDFrts345E-V3_usdojfiles=
```

Notice anything interesting?

- CloudFlare
- akamai
- AWS
- QueueIT

----------

# requirements

- python3
- requests

# usage

```
# Only command-line nerds will understand what to do:
python3 scraper.py <search_term> <page_number>

# example
python3 scraper.py 'linux' 0

https://www.justice.gov/epstein/files/DataSet%209/EFTA01079104.pdf
But the ThinkServer RD540 seems to come with
option for Red Hat Enterprise <em>Linux</em> Server or SUSE <em>Linux</em> Enterprise Server as well.
As Ben
mentioned any <em>Linux</em> will work.
All of our Al
code is <em>Linux</em> based not Windows based.

https://www.justice.gov/epstein/files/DataSet%2010/EFTA01375608.pdf
You can upgrade to the latest version of Adobe Reader for Windows Mac, or <em>Linux</em>®by
visiting http://www.adobe.com/go/reader_download.
<em>Linux</em> is the registered trademark of Linus Torvalds in the U.S. and other
countries.
CONFIDENTIAL - PURSUANT TO FED. R. CRIM.

https://www.justice.gov/epstein/files/DataSet%2011/EFTA02412623.pdf
download it to your <em>Linux</em>, Mac and AppleTV today.
we are excited to welcome you to take part in alpha testing of boxee.
follow this link to validate your
boxee :)
http://app.boxee.tv/validate/veiwqedn
for a quick overview of a few of the features check out this video
http://vimeo.com/2010794 boxee for <em>Linux</em>

https://www.justice.gov/epstein/files/DataSet%209/EFTA00693253.pdf
John Sprunger, A Computer Science student, amateur developer,
giver of opinons
345.4k views
I'm pretty sure there are no set Milestones for <em>Linux</em> knowledge
I like to
divide the knowledge of <em>Linux</em> (and other things) into topics.
1. What is <em>Linux</em>?
- <em>Linux</em> is a kernel t
Read More
»
What was the coolest military unit of all time?

https://www.justice.gov/epstein/files/DataSet%209/EFTA00774200.pdf
month=7&day=22&year=2009&hour=0&min=0+&sec=0&p0=179
myhosting.com - Premium Microsoft® Windows and <em>Linux</em> web and application
hosting - http://link.myhosting.com

https://www.justice.gov/epstein/files/DataSet%209/EFTA00703607.pdf
Why does the computer
science world force GNU/<em>Linux</em> on you?
M
Matthew Perry
atthe
366.4k views
Windows is not a bad Desktop OS.
It's on par with (arguably better than) OS X
and the best <em>Linux</em> desktop environments.
Read More
Why do developers like <em>Linux</em> so much?

https://www.justice.gov/epstein/files/DataSet%2011/EFTA02441876.pdf
month=7&day=22&year=2009&hour=0&min=0+ssec=0&p0=179
myhosting.com - Premium Microsoft® Windows® and <em>Linux</em> web and application
hosting - http://link.myhosting.com

https://www.justice.gov/epstein/files/DataSet%209/EFTA00137043.pdf
Cyber Criminals Targeting <em>Linux</em> Users For Ransomware Attacks.
) reports, "the cybercriminal crosshairs are aiming at
<em>Linux</em> users" for ransomware attacks.
Kapersky has "detailed a new file-encrypting Trojan called RansomEXX
that attacks <em>Linux</em> machines."

https://www.justice.gov/epstein/files/DataSet%2011/EFTA02226865.pdf
Join from PC, Mac, <em>Linux</em>, iOS or Android: https://kernel-hi.zoom.us/j/456759189
Or iPhone one-tap :
US: +14086380968,456759189# or +16468769923,456759189

https://www.justice.gov/epstein/files/DataSet%2011/EFTA02353566.pdf
gmail.com
Subject:
more
More from steve:
mostly I believe it is impossible to be a new 6th operating system--yo= have to compete with windows, mac osx, <em>Linux</em>

https://www.justice.gov/epstein/files/DataSet%209/EFTA00137043.pdf
https://www.justice.gov/epstein/files/DataSet%209/EFTA00693253.pdf
https://www.justice.gov/epstein/files/DataSet%2010/EFTA01375608.pdf
https://www.justice.gov/epstein/files/DataSet%2011/EFTA02353566.pdf
https://www.justice.gov/epstein/files/DataSet%2011/EFTA02441876.pdf
https://www.justice.gov/epstein/files/DataSet%2011/EFTA02226865.pdf
https://www.justice.gov/epstein/files/DataSet%209/EFTA01079104.pdf
https://www.justice.gov/epstein/files/DataSet%209/EFTA00774200.pdf
https://www.justice.gov/epstein/files/DataSet%2011/EFTA02412623.pdf
https://www.justice.gov/epstein/files/DataSet%209/EFTA00703607.pdf
```


