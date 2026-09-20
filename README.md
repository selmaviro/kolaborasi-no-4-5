# kolaborasi-no-4-5
repo_name = REPO_URL.split('/')[-1].replace('.git', '')
!git clone {REPO_URL}
%cd {repo_name}
with open("main.py", "w") as f:
    f.write("# Program Utama Kelompok\n")
