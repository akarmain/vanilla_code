def main():
    s = input()
    if s.find("V") != -1 and  s.find("K") != -1:
        return "VK"
    elif s.find("v") != -1 and  s.find("k") != -1:
        return "vk"
    return ":("
if __name__ == '__main__':
    print(main())
