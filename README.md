# Visualize_MAP

```This repository provides a code for visualizing confirmed cases of COVID-19.```

1. How to use 
    1. Download the map file from https://github.com/CSSEGISandData/COVID-20/tree/master/data_tables/JHU_USCountymap and place it in the map_path directory.
    2. Get any CSV file you want to visualize and put it in the csv_path directory.
    3. Please specify the column to be visualized as selected_col.
    4. Execute sh file. 
    
2. Intro
    - This code is designed to save images by date
    - CSV file must have "dt," "Countyname," and "ST_Name" columns. dt column indicates the date time for each figure, and ST_name denotes the state's name. 
