if __name__ == "__main__":
    n = input(())
    arr = map(int, input().split())
    
    unique_set = sorted(set(arr), reverse=True)
    print(unique_set[1])