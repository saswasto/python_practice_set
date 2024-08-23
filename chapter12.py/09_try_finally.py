def main():
    try:
      a = int(input("Hey give me a number: "))
      print(a)
      return 
    
    except Exception as e:
      print(e)
      return
    
    finally:
       print("Hey I am inside in the finally block")


main()