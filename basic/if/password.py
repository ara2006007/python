uname=input("Please input your user name ")
password =int(input("enter your password "))



print("**********************************************")

print("user_ name : \t",uname )
print("Password : \t",password)

print("**********************************************")


if (uname=="Ara" and password==2006):
    role = int(input("press 0 for admin or press 1 for user "))
    if role==0 :
        print (r"""welcome to admin board 
        ⢀⣴⣿⣿⣿⣿⣦⡀⠀⠀⠀
    ⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀
    ⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀
    ⠀⠀⠀⠙⢿⣿⣿⣿⣿⡿⠋⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀
    ⣰⣿⣿⣿⣿⣆⠀⠀⣰⣿⣿⣿⣿⣆
    ⣿⣿⣿⣿⣿⣿⠁⠈⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡏⠀⠀⢹⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⠇⠀⠀⠸⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣷⡀⢀⣾⣿⣿⣿⣿⣿
    ⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏
    ⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁
    ⠀⠀⠈⠛⢿⣿⣿⣿⣿⡿⠛⠁⠀⠀""")
    else:
        print ("give a proper role")
elif (uname=="Athi" and password==2009) :
    role = int(input("press 0 for admin or press 1 for user "))
    if role==1:
        print(r'''welcome to work        
                     _,,,_
                   .'     `'.
                  /     ____ \
                 |    .'_  _\/
                 /    ) a  a|         .----.
                /    (    > |        /|     '--.
               (      ) ._  /        ||    ]|   `-.
               )    _/-.__.'`\       ||    ]|    ::|
              (  .-'`-.   \__ )      ||    ]|    ::|
               `/      `-./  `.      ||    ]|    ::|
              _ |    \      \  \     \|    ]|   .-'
             / \|     \   \  \  \     L.__  .--'(
            |   |\     `. /  /   \  ,---|_      \---------,
            |   `\'.     '. /`\   \/ .--._|=-    |_      /|
            |     \ '.     '._ './`\/ .-'          '.   / |
            |     |   `'.     `;-:-;`)|             |-./  |
            |    /_      `'--./_  ` )/'-------------')/)  |
            \   | `""""----"`\//`""`/,===..'`````````/ (  |
             |  |            / `---` `==='          /   ) |
             /  \           /                      /   (  |
            |    '------.  |'--------------------'|     ) |
             \           `-|                      |    /  |
              `--...,______|                      |   (   |
                     | |   |                      |    ) ,|
                     | |   |                      |   ( /||
                     | |   |                      |   )/ `"
                    /   \  |                      |  (/
              jgs .' /I\ '.|                      |  /)
               .-'_.'/ \'. |                      | /
               ```  `"""` `| .-------------------.||
                           `"`                   `"`  ''' )
    else :
        print ("give a proper role")
else :
    print("Either username or password is wrong")