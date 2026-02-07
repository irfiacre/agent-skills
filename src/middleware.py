from pathlib import Path

from src.utils import find_skill

def check_if_skill_exist(skill_name: str, project_level: bool = True) -> list:
    """
    Method checks if a skill already exist.
    
    Args:
        skill_name: The name of the skill  
        project_level: Specifies where the skill should be saved, (default: True)

    Returns:
        list of skill location.
    """
    base_path = Path.cwd() if project_level else Path.home()
    result = find_skill(skill_name=skill_name, parent_dir=base_path)
    return result

