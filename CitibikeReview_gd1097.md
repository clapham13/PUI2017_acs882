## 1-Null and Alternative Hypothesis
The null hypothesis stated in Alex’s notebook is “The ratio of men to women biking between the hours of 7pm-7am (dark) will be the same as or less than the ratio of men to women biking between 7am-7pm (light)”
I think the null hypothesis is formulated correctly, overall. Alternative hypothesis is not stated in words in the notebook. It should have been stated as:
The ratio of men to women biking between the hours of 7pm-7am (dark) will be the greater than the ratio of men to women biking between 7am-7pm (light)

The problems that I noticed in the null hypotheses are the followings
-   I noticed that Alex is using “starttime” attribute of citibike dataset to decide if the travel of a person is before 7 pm (light) or after 7 pm (dark). However, what if the travel starts at 6.59 pm and ends at 7.05 pm. Then, according to Alex, that person is traveling at light (before 7 pm), but the travel actually ends after 7 pm (dark). I think this is an important issue on the stated Null Hypothesis. 

-   The formula stated for the null hypothesis in the notebook (Wlight/Wdark – Mlight/Mdark <=0 ) does not reflect the stated null hypothesis. The null hypothesis involves the ratio of men to women when before and after 7 pm. I think the correct form (what I understand from stated null hypothesis) should be:

(Mdark/Wdark) – (Mlight/Wlight)  <= 0. 

The same issue is valid for alternative hypothesis formula

##2-  The data
The data supports the project. Basically, Alex is extracting the data of gender, time_of_the day as an hour, and dark (before 7 pm or after).
-   The only problem here is using “starttime” attribute to decide if the travel is before 7 pm or not, as I mentioned above.


##3-  Appropriate test suggestion based on Statistics in a Nutshell:
Given the null hypothesis: 
-     If distribution of the data is Gaussian, then parametric tests apply. 
-     Unpaired data with 2 categories. Therefore, I suggest 2 groups unpaired t test.
-     If distribution of the data is not Gaussian, then non-parametric tests are safe to use
-     Unpaired data with 2 categories. Therefore, I suggest 2 groups Mann-Whitney U test.

