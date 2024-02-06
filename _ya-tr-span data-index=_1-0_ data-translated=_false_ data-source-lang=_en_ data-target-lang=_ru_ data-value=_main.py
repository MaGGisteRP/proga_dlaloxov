def is_convertible(str1, str2):
    conversions = {
        '0': '2',
        '1': '0',
        '2': '01',
        '02': '1'
    }
    
    if len(str1) != len(str2):
        return False
    
    for i in range(len(str1)):
        
        if str1[i] != str2[i]:
            if str1[i] == '0' and str2[i] == '2':
                return False
            
            if str1[i] == '1' and str2[i] == '0':
                return False
            
            if str1[i] == '2' and str2[i] == '01':
                return False
            
            if str1[i:i+2] == '02' and str2[i] == '1':
                return False
            
    return True

def count_conversions(str1, str2):
    count = 0
    
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    
    return count

str1 = '11202'
str2 = '01211'

if is_convertible(str1, str2):
    print("Одну строку можно преобразовать в другую несколькими заменами.")
    print(f"Количество таких замен: {count_conversions(str1, str2)}")
else:
    print("Одну строку нельзя преобразовать в другую несколькими заменами.")