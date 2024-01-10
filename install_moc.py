import os

try:
    import git
except:
    os.system("pip install GitPython")
    import git
    
try:
    import shutil
except:
    os.system("pip install shutil")
    import shutil
    
moc_dir = "C:/Program Files (x86)/Steam/steamapps/common/Victoria 2/mod/MOC"
mod_dir = "C:/Program Files (x86)/Steam/steamapps/common/Victoria 2/mod/"
try:
    shutil.rmtree(moc_dir)
except:
    pass
tempdir = "./temp"
try:
    os.system('rmdir /S /Q "{}"'.format(tempdir))
except:
    pass
gitlink = "https://github.com/JakobRinke/Mod-of-Chaos"
#os.mkdir(tempdir)
git.Repo.clone_from(gitlink, tempdir)
moc_temp_dir = tempdir + "/" + "MOC"
shutil.move(moc_temp_dir, mod_dir)
os.system('rmdir /S /Q "{}"'.format(tempdir))