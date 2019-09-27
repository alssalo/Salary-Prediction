import pandas as pd

def read_data(path,dataset):
  
  """"
  Read the data based type(properties,target(salary))
  
  Arguments:

  Path:Path of the data
  
  files: list containing the names of the dataset
  
  Returns a pandas df 
  
  """
  
  data=pd.read_csv(path+"/{}".format(dataset))
  print("*"*10,"Reading in ",dataset,"*"*10)
  print("\n {} has {} rows and {} columns".format(dataset,data.shape[0],data.shape[1]))
  print("\n","*"*10,dataset,"has the following columns","*"*10)
  print("\n\n",data.info())
  print("\n","*"*30)
  print("\n The first five rows of data looks like this... \n")
  print(data.head())
  
  return(data)




def get_data(dataset_type):

    """
   Prepare data for fitting and predicting for model
   
   Arguments:

   dataset_type: Select test/train data

   Returns:
   For dataset_type=="Train" ,return features and target
   For dataset_type=="Test" ,return test features, and ids_df

    """

    if dataset_type=="Train":
        features=pd.read_csv("C:/Users/Jo's/Documents/DSDJ/Portfollio.mod4.5/S1/data/unzipped_data/data/train_features.csv")
        target=pd.read_csv("C:/Users/Jo's/Documents/DSDJ/Portfollio.mod4.5/S1/data/unzipped_data/data/train_salaries.csv")
        target.drop(["jobId"],axis=1,inplace=True)
        features.drop(["jobId","companyId"],axis=1,inplace=True)
        return(features,target)

    else:
        test_data=pd.read_csv("C:/Users/Jo's/Documents/DSDJ/Portfollio.mod4.5/S1/data/unzipped_data/data/test_features.csv")
        ids_df=test_data[["jobId","companyId"]]
        test_data.drop(["jobId","companyId"],axis=1,inplace=True)
        return(test_data,ids_df)
        
