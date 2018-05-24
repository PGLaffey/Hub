def main():
    print("Enter the filename: ")
    fileStr = input()
    file = open(fileStr, "r")
    string = file.read()
    string = string.replace("\n", ",")
    file.close()
    file = open("d" + fileStr, "w")
    file.write(string)
    

main()
