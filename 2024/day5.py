
class Page:
    def __init__(self, this_page):
        self.later_pages = set()
        self.this_page = this_page

    def add_later_page(self, later_page):
        self.later_pages.add(later_page)

    def check(self, later_page):
        return later_page in self.later_pages

    def __repr__(self):
        return "{} -> {}".format(self.this_page, self.later_pages)


pages = {}

def add_page_item(row):
    first, second = map(int, row.split('|'))
    if first not in pages:
        pages[first] = Page(first)
    pages[first].add_later_page(second)

def check_item(row):
    items = list(map(int, row.split(',')))
    # for left_index, left in enumerate(items):
    #     print(">>", left_index)
    #     for right_index, right in enumerate(items, left_index+1):
    #         print(left_index, right_index)
    print(items)
    ok = True
    for left_index in range(len(items)):
        for right_index in range(len(items)):
            if left_index == right_index:
                continue
            should_be_bigger = right_index > left_index
            if items[left_index] not in pages:
                continue
            c = pages[items[left_index]].check(items[right_index])
            #print(left_index, right_index, items[left_index], items[right_index], should_be_bigger, c)
            if not should_be_bigger and c:
                print("BAD")
                ok = False
    if ok:
        return items[int(len(items)/2)]
    return 0

sum_middles = 0
with open('day5.txt', 'r') as f:
    for item in f:
        if '|' in item:
            add_page_item(item)

        if ',' in item:
            middle_item = check_item(item)
            print(">>>", middle_item)
            sum_middles += middle_item

    for k in pages:
        print(pages[k])

#check_item('75,97,47,61,53')
print("Sum: ", sum_middles)
