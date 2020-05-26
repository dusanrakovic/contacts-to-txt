# contacts-to-txt

This is small piece of code from the beginning of my programming adventure. It converts backup .vcf file
from Contacts app for Android 4.4.1 into friendlier .txt file. Not much, but it helped me at that time to
use contact information on my desktop computer. I've planned to add some more capabilities to it, like more
export formats (csv, json...), and proper GUI, but didn't have spare time to do it. Well, soon maybe...

Code is written in Python 3 and don't use external libraries. It works with UTF-8 encoded .vcfs, more precisely
with Serbian Latin alphabet.

I include two sample files in this repository:
- PIM00001.vcf (small sample file backed up from Contacts app), which looks like this:

BEGIN:VCARD
VERSION:2.1
N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:=50=65=74=72=6f=76=69=c4=87;=4a=6f=76=61=6e;;;
FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:=4a=6f=76=61=6e=20=50=65=74=72=6f=76=69=c4=87=
TEL;CELL:0995552188
TEL;HOME;VOICE:022143698555
EMAIL;INTERNET:neki.joca.petrovic@gmail.com
EMAIL;HOME:jovanp@provajder.net
END:VCARD
BEGIN:VCARD
VERSION:2.1
N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:=4d=69=6c=69=c4=87=65=76=69=c4=87;=4a=65=6c=65=6e=61;;;
FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:=4a=65=6c=65=6e=61=20=4d=69=6c=69=c4=87=65=76=69=c4=87=
TEL;CELL:099555945
EMAIL;INTERNET:jelena@provajder.net
END:VCARD
BEGIN:VCARD
VERSION:2.1
N:Basta;Danko;;;
FN:Danko Basta
TEL;CELL:0600284423
TEL;HOME;VOICE:022266140555
EMAIL;INTERNET:izmisljeni-lik@provajder.net
URL:http://www.example.com/
END:VCARD

and
- Contacts.txt (output of previous file processed through my code), which looks like this:

Name: Jovan Petrović
Phone: 0995552188
Phone: 022143698555
E-mail: neki.joca.petrovic@gmail.com
E-mail: jovanp@provajder.net

Name: Jelena Milićević
Phone: 099555945
E-mail: jelena@provajder.net

Name: Danko Basta
Phone: 0600284423
Phone: 022266140555
E-mail: izmisljeni-lik@provajder.net
Website: http://www.example.com/

Code is set to extract only textual information, it doesn't have capability to extract pictures.
