


def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    fruit_list.reverse()
    reversed_fruit_list = fruit_list
    print(f"reversed: {reversed_fruit_list}")

    fruit_list.append("orange")
    new_fruit = fruit_list
    print(f"append orange: {new_fruit}")
    
    fruit_index = fruit_list.index("apple")
    fruit_list.insert(fruit_index, "cherry")
    print(f"inserted cherry: {fruit_list}")
    
    fruit_list.remove("banana")
    print(f"remove banana: {fruit_list}")
    
    fruit_list.pop(fruit_list.index("orange"))
    print(f"popped orange: {fruit_list}")
    
    fruit_list.sort()
    print(f"sorted list: {fruit_list}")

    fruit_list.clear()
    print(f"cleared list: {fruit_list}")
       
       
       
if __name__=="__main__":
    main()