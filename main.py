from src.commands import create_skill, edit_skill, delete_skill, list_skills


if __name__ == "__main__":
    create_skill('cool-package-skill', 'Some skill')
    create_skill('yah-package-skill', 'Some skill')
    print(list_skills())
