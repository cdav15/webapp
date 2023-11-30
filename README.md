# Informatics Final Project Submission 

## Chandler Davis

Link to web app: https://chandlerdavismvp.streamlit.app/

## Streamlit Web App and Repository README File

### Abstract

The main purpose of my project was to build a web app where it was easy for the user to compare the Zillow Price Index data across multiple cities. This is a growing need because of the increasing number of people who work from home after the COVID-19 pandemic. For those who are remote workers, they have greater flexibility in where they live and work, and that comes with the benefit of being able to compare housing prices in different cities so they can find the best place for their dollar. 
The result came with a web app that allowed users to visualize and understand the differences in housing prices over time across many different cities. They can compare many different cities at once on the main chart, or they can use the percentage change calculator to calculate the price change over the period they specify. 

### Data Description

The data utilized in this project was taken from the Zillow Rent Index (2010-2017) from Kaggle.com. The index given in the dataset is the median estimated monthly rental price for a given area across all housing types. Zillow calculates this estimate based on proprietary statistical and machine learning models. These models observe rental listings and learn how different factors affect rental pricing to generate predictions. Zillow didn’t start creating Rent Zestimates until November 2010, so that is when the data started. The dataset only goes up until 2017, which is something about that dataset that I would’ve liked to change, but I could not update it to include 2017-2023. 

### Algorithm Description

The web app uses data visualization and a statistical calculator algorithm to show the data in a user-friendly format. The data visualization is a line chart that color codes each line by the city that is selected to show the differences in the price index between the cities chosen by the user. The calculator calculates changes in the price index over the specified period the user chooses. These work together to generate information valuable to the user. 

### Tools Used

-	Python: (including Pandas for data manipulation and cleaning, Vega-Altair for data visualizations within the web app, and Streamlit packages to aid in functionality and aesthetics).
-	GitHub: Hosts the repository in which the data and code are pulled for the web app to work.
-	Streamlit: Hosts the web app.

