import pycurl
from io import BytesIO
import time

b_obj = BytesIO()
crl = pycurl.Curl()

# Set URL value
crl.setopt(crl.URL, 'https://wiki.python.org/moin/BeginnersGuide')

# Write bytes that are utf-8 encoded
crl.setopt(crl.WRITEDATA, b_obj)

t0 = time.time()

# Perform a file transfer
crl.perform()
ttime = time.time()-t0

# End curl session
crl.close()

# Get the content stored in the BytesIO object (in byte characters)
get_body = b_obj.getvalue()

# Decode the bytes stored in get_body to HTML and print the result
print('Output of GET request:\n%s' % get_body.decode('utf8'))
print ("\nTransaction Time: ", ttime, "seconds")