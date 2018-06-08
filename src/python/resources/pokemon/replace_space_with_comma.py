def main():
    print("Enter the filename: ")
    fileStr = input()
    file = open(fileStr, "r")
    string = file.read()
    string = string.replace("\n", ",")
    string = string.replace("'", "`")
    file.close()
    file = open("d" + fileStr, "w")
    file.write(string)
    

main()
