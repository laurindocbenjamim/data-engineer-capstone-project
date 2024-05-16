import wget

def download(url, folderToStore=None, filename=None):
    if url == None:
        print("File not found!")
    else:
        return wget.download(url, folderToStore + '/'+filename)

download("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/analytics/ecommerce.csv", "files", "e_commerce.csv")