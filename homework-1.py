def extract_data(filename):
    ''' (string) -> dict
    
    Bir .txt dosyasinda isimlere karşilik gelen not değerlerini virgule göre boler ve sonucu doner. 
    
    >>>extract_data('deneme.txt')
    dict_items([('Didem Kome', [73]), ('Necla Surekli', [100])])

    >>>extract_data('deneme2.txt')
    dict_items([('didem', [10]), ('ozge', [51])])

    '''
    with open(filename, 'r') as info_file:
        student_data = {}
        for line in info_file:
            line = line.split(',')
            name = line[0]
            score = int(line[1])
            if name not in student_data:
                student_data[name] = []
            student_data[name].append(score)
        return (student_data.items())

data  = extract_data('C:/Users/46921166678/Python-Homework1/info.txt')
highest_averages = sorted(data, key=lambda x: sum(x[1])/float(len(x[1])), reverse=True)
highest_scores = sorted(data, key=lambda x: max(x[1]), reverse=True)

def print_function(x, y):
    ''' (string, number) -> string

    Verilerin belirli formatta ekrana çikti vermesini saglar.

    >>>print_function('didem',45)
    didem,45

    >>>print_function('merhaba',5)
    merhaba,5

    '''
    print("{}, {}".format(x, y))
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

for name, score in highest_scores:
    print_function(name, max(score))

for name, score in highest_averages:
    print_function(name, sum(score)/float(len(score)))
