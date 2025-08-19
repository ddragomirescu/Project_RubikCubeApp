import CubRubik 

if __name__ == "__main__":
    # Crearea unei instanțe a cubului Rubik
    cub = CubRubik.CubRubik()
    
    # Afișarea stării inițiale a cubului
    cub.display()
    
    # Exemplu de rotație a feței "Sus"
    cub.rotate("Sus")
    
    # Afișarea stării cubului după rotație
    cub.display()
    
    # Exemplu de rotație a feței "Fata" în sens invers acelor de ceasornic
    cub.rotate("Fata'")
    
    # Afișarea stării cubului după rotația inversă
    cub.display()
    
    