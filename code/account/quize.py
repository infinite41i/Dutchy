import os


def get_file_list(dir):
    graph_list = []
    for r, d, f in os.walk(dir):
        for file in f:
            graph_list.append(file)
        for directory in d:
            graph_list.extend(get_file_list(directory))
    return graph_list


def combet(SAliB_format, Sajjad_format, path):
    sajad_count = 0
    salib_count = 0
    files = {}
    all_files = get_file_list(path)
    for file in all_files:
        name, mem = file.split(".")
        if mem == Sajjad_format:
            sajad_count += 1
        elif mem == SAliB_format:
            salib_count += 1

        if mem != Sajjad_format:
            if name in files.keys():
                files[name] += 1
            else:
                files[name] = 1

    if sajad_count > salib_count:
        return "Win! Normally!"

    for file in files.keys():
        if sajad_count + files[file] > salib_count:
            return "Win! you can win if you cheat on '%s'!" % file

    return "Lose! you can't win this game!"

