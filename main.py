import CubRubik 

if __name__ == "__main__":
    # Crearea unei instanțe a cubului Rubik
    cub = CubRubik.CubRubik()
    
    # Afișarea stării inițiale a cubului
    #cub.display()
    
    # Exemplu de rotație a feței "Sus"
    # cub.rotate("U")
    cub.rotate("R-")
    cub.rotate("U")
    cub.rotate("B")
    cub.rotate("L")
    cub.rotate("D-")
    cub.rotate("F")
    cub.rotate("L-")
    
    
    
    # Afișarea stării cubului după rotație
    #cub.display()
    
    # Exemplu de rotație a feței "Fata" în sens invers acelor de ceasornic
    #cub.rotate("F-")
    
    # Afișarea stării cubului după rotația inversă
    cub.display()
    
    print("Fata 'Sus' a cubului Rubik:" + str(cub.cube['U']))
    print("Fata 'Jos' a cubului Rubik:" + str(cub.cube['D']))
    print("Fata 'Fata' a cubului Rubik:" + str(cub.cube['F']))
    
    