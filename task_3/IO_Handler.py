

def read_skill_levels(Filepath)-> list[int]:
    with open(Filepath,"r")as data :
        skill_levels=[]
        for skill_level in data:
                skill_levels.append(int(skill_level))

    return skill_levels