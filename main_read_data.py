import utils
import os

from dotenv import load_dotenv
# Can load environment variables from the .env file
load_dotenv()

# Access the environment variable
prj_path = os.getenv('PROJECT_PATH')

df_short = utils.get_aws_data('collapse_MSCI_GTI_merged_complete.csv')
fileshort_path=os.path.expandvars(prj_path+'/green-innovations-finance/data/collapse_MSCI_GTI_merged_complete.csv')
df_short.to_csv(fileshort_path)

datast = utils.get_aws_data('st_interest.csv')
filest_path=os.path.expandvars(prj_path+'/green-innovations-finance/data/st_interest.csv')
datast.to_csv(filest_path)

dtff = utils.get_aws_data('US_FF_5_Factors_2x3.txt')
file_path=os.path.expandvars(prj_path+'/green-innovations-finance/data/US_FF_5_Factors_2x3.txt')
dtff.to_csv(file_path)

datamerged = utils.get_aws_data('merged_data.csv')
filemerge_path=os.path.expandvars(prj_path+'/green-innovations-finance/data/merged_data.csv')
datamerged.to_csv(filemerge_path)
