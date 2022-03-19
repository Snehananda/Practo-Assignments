import requests
import sys

#Define variable with file name.
filename = "LogFile_py.txt"

#Check for command line arguments
#If not given then ask user for article title.
#Replace space with %20
if len(sys.argv) == 1:
    title = input("Enter the Title of the Article: ").replace(" ", "%20")
else:
    title = '%20'.join(sys.argv[1:])


print(f"Title: {title.replace('%20', ' ')}")

#URL to access the content of the article.
url = "https://en.wikipedia.org/w/api.php?action=query&format=json&titles="+title+"&prop=extracts"
 
#Request for the content.
res = requests.get(url)

#Get the status code
stat_code = res.status_code
print("Response Status Code: " , stat_code)

#If status code is 200, then write the URL in the file.
#Else display error message to the user.
if stat_code == 200:
    try:
        with open(filename, "a") as file:
            file.writelines(url + "\n\n")
    except Exception:
        print("Error....")
