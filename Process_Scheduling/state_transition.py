def scheduling(data_dict, running, finish):
    if len(running) == 0:
        for i in range(len(data_dict), 0, -1):
            if len(data_dict[i]) > 0:
                running = data_dict[i].pop()
                running[1] = 'running'
                return data_dict, running, finish
    else:
        if running[2] > 1:
            running[2] -= 1
        if running[3] - 1 == 0:
            running[1] = 'finish'
            running[2] = 0
            running[3] -= 1
            running[4] += 1
            finish.append(running)
            running = []
            for i in range(len(data_dict), 0, -1):
                if len(data_dict[i]) > 0:
                    running = data_dict[i].pop()
                    running[1] = 'running'
                    return data_dict, running, finish
            return data_dict, running, finish
        elif running[3] - 1 > 0:
                running[1] = 'ready'
                running[3] -= 1
                running[4] += 1
                data_dict[running[2]].append(running)
                running = []
                for i in range(len(data_dict), 0, -1):
                    if len(data_dict[i]) > 0:
                        running = data_dict[i].pop()
                        running[1] = 'running'
                        return data_dict, running, finish
                return data_dict, running, finish


def block(running, block):
    if len(running) > 1:
        running[1] = 'Block'
        block.append(running)
        return running, block, 1
    else:
        return running, block, -1


def wakeup(data_dict, block):
    if len(block) > 0:
        temp = block.pop()
        temp[1] = 'ready'
        data_dict[temp[2]].append(temp)
        return data_dict, block, 1
    else:
        return data_dict, block, -1


def revocation(running, finish):
    if len(running) > 1:
        running[1] = 'finish'
        running[2] = 0
        finish.append(running)
        running = []
        return running, finish, 1
    else:
        return running, finish, -1
