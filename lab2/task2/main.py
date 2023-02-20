import commands
from storage import Storage


command_promt_template="""
supported commands:
add <key>    - add one or more elements to the container (if the element is already in there then don’t add);
remove <key> - delete key from container;
find <key>   - check if the element is presented in the container, print each found or “No such elements” if nothing is;
list         - print all elements of container;
grep <regex> - check the value in the container by regular expression, print each found or “No such elements” if nothing is;
save         - save container to file;
load         - load container from file;
switch <user>- switches to another user.
quit         - stop the program
"""


def program_loop(st:Storage):
    
    usr_name=input("Enter username: ")
    st.switch(usr_name)
    

    while(True):
        usr_input=input(command_promt_template)
        command_input=usr_input.split()[0]
        args=usr_input.split()[1:]
        match command_input:
            case commands.ADD:
                st.add(args)
            case commands.REMOVE:
                st.remove(args[0])
            case commands.FIND:
                st.find(args[0])
            case commands.LIST:
                st.lst()
            case commands.GREP:
                st.grep(args[0])
            case commands.SAVE:
                st.save()
            case commands.LOAD:
                st.load()
            case commands.SWITCH:
                sub_input=input("save current container (y/n)?: ")
                if sub_input=="y":
                    st.save()
                sub_input=input("enter username: ")
                st.switch(sub_input)
            case commands.QUIT:
                sub_input=input("save current container (y/n)?: ")
                if sub_input=="y":
                    st.save()
                break



def main():
    program_loop(Storage())


if __name__ =="__main__":
    main()