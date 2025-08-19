import CubRubik 

if __name__ == "__main__":
    # Crearea unei instanțe a cubului Rubik
    cub = CubRubik.CubRubik()
    
    # Afișarea stării inițiale a cubului
    #cub.display()
    
    # Exemplu de rotație a feței "Sus"
    cub.rotate("U")

    #cub.rotate("D-") 
    
    # Afișarea stării cubului după rotație
    #cub.display()
    
    # Exemplu de rotație a feței "Fata" în sens invers acelor de ceasornic
    #cub.rotate("F-")
    
    # Afișarea stării cubului după rotația inversă
    cub.display()
    
    print("Fata Dreapta:" + str(cub.cube['R']))
    print("Fata Front:" + str(cub.cube['F']))
    print("Fata Sus:" + str(cub.cube['U']))
    