def main():
    for x in "0123456789abcde":
        f = (int(f"6{x}839", 15) + int(f"5793{x}{x}5", 15) + int(f"53129{x}", 15) + int(f"14{x}677935", 15))
        if f % 14 == 0:
            return f // 14


if __name__ == "__main__":
    print("ANS:", main())
