from helium import *
import pandas as pd

start_firefox('https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787')
wait_until(Text('Key No. 22408 3000 E & FOOTHILL RD CURVE, TWIN FAL...').exists)

#click on the first link for first project details
click('Key No. 22408 3000 E & FOOTHILL RD CURVE, TWIN FAL...')
click('Key No. 22408 3000 E & FOOTHILL RD CURVE, TWIN FAL...')

#clicks on this point so scrolling down can occur
wait_until(Text('QuestCDN Partner Posting').exists)
click(Point(200,300))

#wait until page is loaded then scroll down
scroll_down(num_pixels=480)

#wait until page is loaded then extract the text we want
wait_until(Text('Project Details').exists)

df= Text( to_right_of="Closing Date").value, Text( to_right_of="Est. Value Notes").value, Text( to_right_of="Description:").value
print(df)

# Go back to previous page
click ('Search Postings')

wait_until(Text('City').exists)
click('entries')
scroll_down(num_pixels=450)

#now we click on second option
click('Key No. 24192 SH-75, Ohio Gulch Road Intersection')
click('Key No. 24192 SH-75, Ohio Gulch Road Intersection')

#clicks on this point so scrolling down can occur
wait_until(Text('QuestCDN Partner Posting').exists)
click('QuestCDN Partner Posting')

#wait until page is loaded then scroll down
scroll_down(num_pixels=480)

#wait until page is loaded then extract the text we want
wait_until(Text('Project Details').exists)

bf= Text( to_right_of="Closing Date").value, Text( to_right_of="Est. Value Notes").value, Text( to_right_of="Description:").value
print(bf)

# Go back to previous page
click ('Search Postings')

wait_until(Text('City').exists)
click('entries')
scroll_down(num_pixels=450)

#now we click on Third option
click('Key No. 23815 FY24 D6 STRIPING')
click('Key No. 23815 FY24 D6 STRIPING')

#clicks on this point so scrolling down can occur
wait_until(Text('QuestCDN Partner Posting').exists)
click('QuestCDN Partner Posting')

#wait until page is loaded then scroll down
scroll_down(num_pixels=480)

#wait until page is loaded then extract the text we want
wait_until(Text('Project Details').exists)

ef= Text( to_right_of="Closing Date").value, Text( to_right_of="Est. Value Notes").value, Text( to_right_of="Description:").value
print(ef)

# Go back to previous page
click ('Search Postings')

wait_until(Text('City').exists)
click('entries')
scroll_down(num_pixels=550)

#now we click on Fourth option
click('Key No. 21842, I-84, FY23 D4 Interstate Striping')
click('Key No. 21842, I-84, FY23 D4 Interstate Striping')

#clicks on this point so scrolling down can occur
wait_until(Text('QuestCDN Partner Posting').exists)
click('QuestCDN Partner Posting')

#wait until page is loaded then scroll down
scroll_down(num_pixels=480)

#wait until page is loaded then extract the text we want
wait_until(Text('Project Details').exists)

ff= Text( to_right_of="Closing Date").value, Text( to_right_of="Est. Value Notes").value, Text( to_right_of="Description:").value
print(ff)

# Go back to previous page
click ('Search Postings')

wait_until(Text('City').exists)
click('entries')
scroll_down(num_pixels=550)

#now we click on Fifth option
click('Key No. 20592 / 20482 SH-3, CDA RV BR to I-90, SH-...')
click('Key No. 20592 / 20482 SH-3, CDA RV BR to I-90, SH-...')

#clicks on this point so scrolling down can occur
wait_until(Text('QuestCDN Partner Posting').exists)
click('QuestCDN Partner Posting')

#wait until page is loaded then scroll down
scroll_down(num_pixels=480)

#wait until page is loaded then extract the text we want
wait_until(Text('Project Details').exists)

gf= Text( to_right_of="Closing Date").value, Text( to_right_of="Est. Value Notes").value, Text( to_right_of="Description:").value
print(gf)
















