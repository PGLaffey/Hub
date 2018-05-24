class Move_Table():
    def __init__(self):
        self.table = {}
        self.set_elements()
        self.read_in()

    def read_in(self):
        dirrect = 'moves.txt'
        file = open(dirrect,'r')
        line = file.readline()
        while line != '>>':
            if line[0] != '#':
                line = line.strip('\n')
                line = line.split(',')
                count = 0
                while count < len(line):
                    if line[count][0] == ' ':
                        line[count] = line[count].lstrip(' ')
                    count += 1
                self.element_hash(line[3],line[0],line)
            line = file.readline()
        file.close()

    def set_elements(self):
        elements = ['dark','fire','normal','rock','ground','grass','poison','bug','flying','dragon','water','electric','fighting','ice','psychic','ghost'] 
        for element in elements:
            self.table[element] = [[]]*26

    def element_hash(self, element, name, move):
        index = hash(name[0]) % 26
        if self.table[element][index] == []:
            self.table[element][index] = [move]
        else:
            self.table[element][index].append(move)

            
    
