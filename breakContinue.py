def run():

  
    for i in range(100):
        print(i)
        if i==50:
            break

    for i in range(100):
        if i<50:
            continue
        print(i)


if __name__=='__main__':
    run()