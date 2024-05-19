import os, random, datetime, schedule, time
from github import Github

folder_path = "path_to_folder" # PATH FOR 
github_token = "your_github_token" # AUTH TOKEN
files_list = [file for file in os.listdir(folder_path) if file.endswith((".py", ".bat"))]

def upload_files():
    if len(files_list) > 0:
        g = Github(github_token)
        repo = g.get_user().get_repo('Utils') # REPO UTILS IN THIS CASE
        random_file = random.choice(files_list)
        nome = os.path.splitext(random_file)[0]
        pattyh=os.path.join(folder_path, nome + '.utils')
        if os.path.isdir(pattyh):
            print("La cartella '{}' è presente.".format(nome + '.utils'))
            for filename in os.listdir(pattyh):
                with open(os.path.join(folder_path, filename), "rb") as file:
                    contents = file.read()
                    repo.create_file(f"files/{nome}.utils/{filename}", f"Committing {random_file} in {nome}.utils on {datetime.datetime.now()}", contents)
            os.remove(os.path.join(folder_path, random_file))
        else:
            print("La cartella '{}' non è presente.".format(nome + '.utils'))
        
        with open(os.path.join(folder_path, random_file), "rb") as file:
            contents = file.read()
            repo.create_file(f"files/{random_file}", f"Committing {random_file} on {datetime.datetime.now()}", contents)
        
            print(f"{random_file} caricato con successo su GitHub.")
        os.remove(os.path.join(folder_path, random_file)
    else:
        print("La cartella è vuota.")

def upload_job():
    upload_files()
    last_upload_time=datetime.datetime.now()
    with open("last_upload_time.txt", "w") as time_file:
        time_file.write(str(last_upload_time))

# Eachday at 00.00
schedule.every().day.at("00:00").do(upload_job)

while True:
    schedule.run_pending()
    time.sleep(1)
