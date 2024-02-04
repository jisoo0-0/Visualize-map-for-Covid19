# Visualize map for Covid-19

```This repository provides a code for visualizing confirmed cases of COVID-19.```

1. How to use 
    1. Download the map file from https://github.com/CSSEGISandData/COVID-20/tree/master/data_tables/JHU_USCountymap and place it in the map_path directory.
    2. Get any CSV file you want to visualize and put it in the csv_path directory.
    3. Please specify the column to be visualized as selected_col.
    4. Execute sh file. 
    
2. Intro
    - This code is designed to save images by date
    - CSV file must have "dt," "Countyname," and "ST_Name" columns. dt column indicates the date time for each figure, and ST_name denotes the state's name. 

3. Sample images
   
    ![Alabama_2021-01-09](https://github.com/jisoo0-0/Visualize_MAP/assets/130432190/e076069c-7ec6-4a35-8cc9-c18b55599185)
    ![Massachusetts_2020-08-08](https://github.com/jisoo0-0/Visualize_MAP/assets/130432190/40003cac-4f50-4c04-bd70-2d7176528eba)
    ![Vermont_2020-07-17](https://github.com/jisoo0-0/Visualize_MAP/assets/130432190/c6847aec-17c7-4704-b1e5-8cc8a07472d3)
    ![Wisconsin_2021-08-03](https://github.com/jisoo0-0/Visualize_MAP/assets/130432190/ab2a4e8c-9db5-4d35-a073-425744150480)
