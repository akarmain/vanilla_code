from collections import defaultdict

def main():
    file_names = []
    for _ in range(int(input())):
        file_names.append(input())
    download_count = defaultdict(int)
    downloaded_files = []
    for file_name in file_names:
        name_parts = file_name.split('.')
        if len(name_parts) == 2:
            base_name, extension = name_parts[0], '.' + name_parts[1]
        else:
            base_name, extension = name_parts[0], ''
        if download_count[base_name, extension] > 0:
            indexed_file_name = f"{base_name}({download_count[base_name, extension]}){extension}"
            downloaded_files.append(indexed_file_name)
        else:
            downloaded_files.append(file_name)
        download_count[base_name, extension] += 1
    downloaded_files = sorted(downloaded_files)

    for item in downloaded_files:
        print(item)

if __name__ == '__main__':
    main()
