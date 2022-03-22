def eliminate1(work_set, page_table, page_number, current_position):
    while True:
        current_position = current_position % 8
        if work_set[current_position][1] == 0:
            eliminate_pagenumber = work_set[current_position][0]
            page_table[page_number] = page_table[work_set[current_position][0]]
            page_table[work_set[current_position][0]] = ' '
            work_set[current_position][0] = page_number
            work_set[current_position][1] = 1
            current_position = (current_position + 1) % 8
            return work_set, page_table, current_position, eliminate_pagenumber
        else:
            work_set[current_position][1] = 0
        current_position += 1


def eliminate2(work_set, page_table, page_number, page_river_position, current_position):
    while True:
        current_position = current_position % 8
        if work_set[current_position][1] == 0:
            eliminate_pagenumber = work_set[current_position][0]
            page_table[page_number] = page_table[work_set[current_position][0]]
            page_table[work_set[current_position][0]] = ' '
            work_set[current_position][0] = page_number
            work_set[current_position][1] = 1
            current_position = (current_position + 1) % 8
            page_river_position += 1
            return work_set, page_table, current_position, page_river_position, eliminate_pagenumber
        else:
            work_set[current_position][1] = 0
        current_position += 1
