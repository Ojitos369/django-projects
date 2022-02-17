class Test1:
    
    def check_data(self, user_data, correct_answers):
        res = 0
        i=0
        user_data = dict(user_data)
        del user_data['csrfmiddlewaretoken']
        for r in user_data:
            if user_data[r][0] in correct_answers:
                res += 1
            else:
                print(f'{i+1}.- {user_data[r][0]} incorrecto - {correct_answers[i]} correcto')
            i += 1
        return res
    
    def section_1(self, user_data):
        correct_answers = [
            '2', '5', '10', '13', '18', '24', '27', '29', '35', '39', '43', '46', '50', '55', '57', '63'
        ]
        res = self.check_data(user_data, correct_answers)
        
        rango = ''
        if res >= 0 and res <= 7: rango = "Deficiente";
        if res >= 8 and res <= 9: rango = "Inferior";
        if res >= 10 and res <= 11: rango = "Term. M.B.";
        if res >= 12 and res <= 13: rango = "Term. Medio";
        if res == 14: rango = "Term. M.A."
        if res == 15: rango = "Superior"
        if res == 16: rango = "Excelente"
        
        return res, rango

    def section_2(self, user_data):
        correct_answers = [
            '67', '68', '72', '76', '79', '81', '85', '88', '90', '92', '96'
        ]
        res = self.check_data(user_data, correct_answers)
        
        rango = ''
        res_2 = res * 2
        if res_2 >= 0 and res_2 <= 6: rango = "Deficiente"
        if res_2 == 8: rango = "Inferior"
        if res_2 == 10: rango = "Term. M.B."
        if res_2 >= 12 and res_2 <= 16: rango = "Term. Medio"
        if res_2 == 18: rango = "Term. M.A."
        if res_2 == 20: rango = "Superior"
        if res_2 == 22: rango = "Excelente"
        
        return res, rango

    def section_3(self, user_data):
        correct_answers = [
            'Opuestos', 'Iguales', 'Opuestos', 'Opuestos', 'Opuestos', 'Opuestos', 'Iguales', 'Iguales', 'Opuestos', 'Iguales', 'Opuestos', 'Opuestos', 'Opuestos', 'Iguales', 'Opuestos', 'Opuestos', 'Iguales', 'Opuestos', 'Iguales', 'Opuestos', 'Opuestos', 'Opuestos', 'Iguales', 'Iguales', 'Iguales', 'Opuestos', 'Iguales', 'Opuestos', 'Opuestos', 'Iguales'
        ]
        
        res = 30
        
        i=0
        user_data = dict(user_data)
        del user_data['csrfmiddlewaretoken']
        for r in user_data:
            if user_data[r][0] != correct_answers[i]:
                res -= 2
                print(f'{i+1}.- {user_data[r][0]} incorrecto - {correct_answers[i]} correcto')
            i += 1
            
        extras = len(correct_answers) - i
        res -= extras * 2
        
        if res < 0: res = 0
        rango = ''
        if res >= 0 and res <= 7: rango = "Deficiente"
        if res >= 8 and res <= 11: rango = "Inferior"
        if res >= 12 and res <= 13: rango = "Term. M.B."
        if res >= 14 and res <= 22: rango = "Term. Medio"
        if res >= 23 and res <= 26: rango = "Term. M.A."
        if res >= 27 and res <= 28: rango = "Superior"
        if res >= 29 and res <= 30: rango = "Excelente"
        
        return res, rango


class Test2():
    pass

class Test3():
    pass

SECTIONS = {
    1: Test1().section_1,
    2: Test1().section_2,
    3: Test1().section_3,
    4: Test1(),
    5: Test1(),
    6: Test1(),
    7: Test1(),
    8: Test1(),
    9: Test1(),
    10: Test1(),
    11: Test2(),
    12: Test3()
}



class CheckTest:
    def check_section(self, user_data, section_id):
        return SECTIONS[section_id](user_data)


check_test = CheckTest()




def checar():
    opciones = 2
    preguntas = 30
    extra = 64 + 33
    res = ['O', 'I', 'O', 'O', 'O', 'O', 'I', 'I', 'O', 'I', 'O', 'O', 'O', 'I', 'O', 'O', 'I', 'O', 'I', 'O', 'O', 'O', 'I', 'I', 'I', 'O', 'I', 'O', 'O', 'I']
    letters = ['I', 'O']
    aux = 0
    checking = 0
    checked = False
    for i in range(preguntas * opciones):
        resp = ''
        if res[checking] == letters[aux] and not checked:
            resp = res[checking]
            checking += 1
            checked = True
            print(f'{i+1 + extra}.- {resp}')
        aux += 1
        if aux == opciones:
            #print('-'*20)
            aux = 0
            checked = False
            
            
            
def completar():
    res = ['O', 'I', 'O', 'O', 'O', 'O', 'I', 'I', 'O', 'I', 'O', 'O', 'O', 'I', 'O', 'O', 'I', 'O', 'I', 'O', 'O', 'O', 'I', 'I', 'I', 'O', 'I', 'O', 'O', 'I']
    for r in res:
        if r == 'O':
            print('Opuestos')
        else:
            print('Iguales')
            
            
            
