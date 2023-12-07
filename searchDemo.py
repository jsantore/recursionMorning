import Project5Start

def main():
    game_data = Project5Start.get_project5_data()
    game_data.sort(key=get_key)
    game_to_find = input(("what game:"))
    result = binary_search(game_data, game_to_find)
    print(result)

def get_key(gameDatum):
    return gameDatum['name']

def binary_search(data, to_find):
    if len(data) == 0:
        return None
    middle = len(data)//2
    middle_item = data[middle]
    if middle_item['name'] == to_find:
        return middle_item
    if middle_item['name'] < to_find:
        return binary_search( data[middle+1:], to_find)
    else:
        return binary_search(data[:middle], to_find)


main()