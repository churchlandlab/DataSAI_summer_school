





def download_neural_data(data_type, destination = None):
    '''Function to automatically download either miniscope or widefield data from
    the google drive

    Parameters
    ----------
    data_type: string, either "widefield" or "miniscope"
    destination: string, desired folder to store the data, default = download_neural_data

    Returns
    -------
    data_file: string, the path to the data file for loading

    ----------------------------------------------------------------------------
    '''
    import gdown #Make sure to install this first via: pip install gdown
    import os

    if data_type == "miniscope":
        url = "https://drive.google.com/file/d/1cLbUqh2LKLXuwqXdjyvMi4DuKMFC0DiM/view?usp=drive_link"
        fname = "miniscope_data.npy"
    elif data_type == "widefield":
        url = "https://drive.google.com/file/d/1XNCPKY5bRS9QtvY1aj982CjaCkMgeOJt/view?usp=drive_link"
        fname = "widefield_data.mat" #Some renaming here to simplify

    if destination is None:
        parent = os.path.split(os.getcwd())[0] #The parent directory
        destination = os.path.join(parent, "DataSAI_data_folder")
        if not os.path.isdir(destination):
            os.makedirs(destination)
    data_file = os.path.join(destination, fname)

    gdown.download(url, data_file, quiet=False, fuzzy =True)
    return data_file
