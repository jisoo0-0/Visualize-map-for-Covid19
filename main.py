import argparse 
from make_dataset import *
def main():
    parser = argparse.ArgumentParser(description='Setting')
    parser.add_argument('--num_bins', type=int, default=50)
    parser.add_argument('--cmap', type=str, default='PiYG_r')
    parser.add_argument('--selected_col', type = str, default =r"Confirmed Cases")
    parser.add_argument('--csv_path', type = str, default =r"E:\VisualStudio_Code\Covid\covid_image\result_time_newconfirmed.csv")
    parser.add_argument('--map_path', type = str, default=r'E:\VisualStudio_Code\Covid\covid_image\ImagePreProcessing\rawdata\USCounties_JHUmap\USCounties_JHUmap.shp')
    parser.add_argument('--img_save_path', type=str, default=r'E:\VisualStudio_Code\Covid\covid_image\ImagePreProcessing\clean_data\newconfirmed\rgbcolor')
    args = parser.parse_args()
    col_name = ['Alabama',  'American Samoa', 'Arizona', 'Arkansas',
       'California', 'Colorado', 'Connecticut', 'Delaware',
       'Diamond Princess', 'District of Columbia', 'Florida', 'Georgia',
       'Grand Princess',  'Idaho', 'Illinois', 'Indiana',
       'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
       'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
       'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
       'New Jersey', 'New Mexico', 'New York', 'North Carolina',
       'North Dakota', 'Northern Mariana Islands', 'Ohio', 'Oklahoma',
       'Oregon', 'Pennsylvania', 
       'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',
       'Vermont',  'Virginia', 'Washington',
       'West Virginia', 'Wisconsin', 'Wyoming']
    save_imgs(args.csv_path, args.map_path, args.img_save_path, col_name, args.num_bins, args.selected_col)
    
if __name__ == '__main__':    
    main()