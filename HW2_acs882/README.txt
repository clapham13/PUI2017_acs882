IMPORTANT: Because of issues with the data facitity, I connected to NYC Open Data through the web. I spoke with Frederica, who said that this was fine. 

Part 1: Uses the MTA info to pull information on bus locations and number of buses for a particular route.

Part 2: Takes the MTA information in part 1, and adds upcoming stops and bus status, and writes this into CSV format

Part 3: I used data on real estate in Time Square, and initially compared floor space to the number of stories in the building (admitidly not the most interesting of comparisons, but you do see a strong correlation between # of stories and floor space, as would be expected). For the extra credit, I used 'Last Sale Date' and 'Last Sale Price' to map over the years included in the dataset; There were a small number of overwhelming outliers (very expensive real estate) that made the graphs unintelligable. To cope with this, I used a 'log' function to normalize the sales price, creating a more readable graph.

Collaboration: I did most of the work alone. I am currently sitting in a room with Jonathan, Prince, and Jack, who informed me that the 'open' function will create a new CSV if one doesn't already exist. Beyond that, occasional use of Stack Overflow was my only assistance. 
