import os


def initTitle(title_str=None):
    if title_str is None:
        title_str = 'Default title:'
    else:
        title_str = str(title_str)
        hr_line = len(title_str) * '-'
    print('%s\n%s\n%s' % (hr_line, title_str, hr_line))


def addTip(tip_str=None):
    if tip_str is None:
        tip_str = '(Default tip)'
    else:
        tip_str = '('+str(tip_str)+')'
        hr_line = len(tip_str) * '-'
    print('%s\n%s' % (tip_str, hr_line))


def listEmpty(some_list):
    if len(some_list) > 0:
        return False
    else:
        addTip('List is empty')
        return True


def showList(main_list):
    initTitle('Show list:')
    list_empty = listEmpty(main_list)
    if not list_empty:
        for i in range(0, len(main_list)):
            item = main_list[i]
            print('%s.%s' % ((i+1), item['name']))


def addItem(main_list):
    initTitle('Add item:')
    addTip('Type new item name or press \'Enter\' to exit')
    exit_loop = False
    while not exit_loop:
        user_input = input('Type name:')
        if user_input != '':
            item_id = (len(main_list)+1)
            item_name = user_input.strip()
            new_item = dict(id=item_id, name=item_name)
            main_list.append(new_item)
            initTitle('(>>>Item added<<<)')
            exit_loop = True
        else:
            addTip('Input name is empty!')
            exit_loop = True


def editItem(main_list):
    initTitle('Edit item:')
    list_empty = listEmpty(main_list)
    if not list_empty:
        addTip('Type item number or press \'Enter\' to exit')
        exit_loop = False
        while not exit_loop:
            user_input = input('Type number:')
            if user_input != '':
                try:
                    search_num = int(user_input)
                    list_len = len(main_list)
                    if search_num > list_len or search_num == 0:
                        addTip(
                            'Item not in list. List has ' +
                            str(list_len) +
                            ' items.')
                    else:
                        i = 0
                        while i < list_len:
                            item = main_list[i]
                            if search_num == item['id']:
                                initTitle(
                                    'Old item:\'' +
                                    str(item['id']) +
                                    '.' +
                                    item['name'] +
                                    '\'')
                                new_item_name = input('New name:')
                                if new_item_name == '':
                                    addTip('Input name is empty!')
                                    exit_loop = True
                                else:
                                    item['name'] = new_item_name.strip()
                                    initTitle('(>>>Item edited<<<)')
                                    exit_loop = True
                                break
                            else:
                                i += 1
                except ValueError:
                    addTip('ERROR:Must be number!')
            else:
                addTip('Input number is empty!')
                exit_loop = True


def removeItem(main_list):
    initTitle('Remove item:')
    list_empty = listEmpty(main_list)
    if not list_empty:
        addTip('Type item number or press \'Enter\' to exit')
        exit_loop = False
        while not exit_loop:
            user_input = input('Type number:')
            if user_input != '':
                try:
                    search_num = int(user_input)
                    list_len = len(main_list)
                    if search_num > list_len or search_num == 0:
                        addTip(
                            'Item not in list. List has ' +
                            str(list_len) +
                            ' items.')
                    else:
                        i = 0
                        while i < list_len:
                            item = main_list[i]
                            if item['id'] != (i+1):
                                item['id'] = (i+1)
                            else:
                                pass
                            if search_num == item['id']:
                                main_list.remove(item)
                                list_len = len(main_list)
                                i = i
                                search_num = 0
                                initTitle('(>>>Item removed<<<)')
                                exit_loop = True
                            else:
                                i += 1
                except ValueError:
                    addTip('ERROR:Must be number!')
            else:
                addTip('Input number is empty!')
                exit_loop = True


def exitApp(main_list):
    i = 0
    list_len = len(main_list)
    main_str = ''
    while i < list_len:
        item = main_list[i]
        if i == (list_len-1):
            str_item = str(item['id'])+'.'+item['name']
        else:
            str_item = str(item['id'])+'.'+item['name']+'\n'
        main_str += str_item
        i += 1
    openList('w', main_str)
    initTitle('Exit app')
    exit()


def showOptions(options):
    initTitle('Options:')
    opt_i = 0
    for key in options:
        opt = options[key]
        opt_i += 1
        if opt['name'] == 'Exit':
            print('%s.To %s type:\'%s\'' % (opt_i, opt['name'], key))
        elif opt['name'] == 'List':
            print('%s.To show %s type:\'%s\'' % (opt_i, opt['name'], key))
        else:
            print('%s.To %s item type:\'%s\'' % (opt_i, opt['name'], key))


def mainLoop(options, main_list):
    user_input = ''
    while user_input != 'x':
        showOptions(options)
        user_input = input('Type option:')
        try:
            letter = user_input.strip().lower()
            opt = options[letter]['func']
            opt(main_list)
        except KeyError:
            addTip('ERROR:No option!')
            user_input = ''


def openList(file_mode, append_str=None):
    file_name = 'your_list.txt'
    file_path = cwd+'\\'+file_name
    main_list = []
    with open(file_path, file_mode) as file:
        if file_mode == 'r':
            initTitle('File loaded')
            line_num = 1
            for file_line in file:
                line = file_line.strip('\n')
                line_list = line.split('.')
                list_len = len(line_list)
                i = 2
                while i < list_len:
                    line_list[1] += '.'+line_list[i]
                    line_list.remove(line_list[i])
                    list_len = len(line_list)
                    i = i
                try:
                    txt_line = str(line_list[1])
                    int_line = int(line_list[0])
                    list_item = dict(id=int_line, name=txt_line)
                    main_list.append(list_item)
                except ValueError:
                    list_item = dict(id=line_num, name=txt_line)
                    main_list.append(list_item)
                line_num += 1
        elif file_mode == 'w':
            file.write(append_str)
            initTitle('File saved')
        else:
            initTitle('File created')
    return main_list


def listApp():
    initTitle('---To DO List App---')
    options = {
        'l': {'name': 'List', 'func': showList},
        'a': {'name': 'Add', 'func': addItem},
        'e': {'name': 'Edit', 'func': editItem},
        'r': {'name': 'Remove', 'func': removeItem},
        'x': {'name': 'Exit', 'func': exitApp}
    }
    global cwd
    cwd = os.getcwd()
    try:
        main_list = openList('r')
    except FileNotFoundError:
        main_list = openList('a')
    mainLoop(options, main_list)
listApp()
