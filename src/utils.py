from pathlib import Path

from src.constants import SUPPORTED_AGENTS

def build_skill_template(
    name: str = "skill-name",
    description: str = "Describe what this skill does and when to use it"
):
    """
    Building the skill template.
    """
    return f"""---\nname: {name}\ndescription: {description}.\n---\n# {name.replace("-", " ").title()}\n## Instructions\nAdd your skill instructions here.\n"""

def check_available_coding_agents():
    """
    Method to check the available agents.
    """
    root_dir = Path.home()
    available_agents = {}
    for supported_agent in SUPPORTED_AGENTS:
        config_dir = Path(f'{root_dir}/{supported_agent.get("config_dir")}')
        if config_dir.exists():
            available_agents[supported_agent.get('name')] = {
                'exist': True,
                'config_dir': config_dir
            }

    return available_agents

def find_skill(skill_name: str, parent_dir: str = Path.cwd()) -> list:
    """
    Method finds where the skill is located.
    """
    result ={}
    for supported_agent in SUPPORTED_AGENTS:
        if agent_path := Path(f'{parent_dir}/{supported_agent.get("skills_dir")}').resolve():
            skill_file = f'{agent_path}/{skill_name}/SKILL.md'
            if Path(skill_file).is_file():
                result[supported_agent.get('name')] = skill_file
    return result

class SkillNotFoundError(Exception):
    """
    Exception raised for a skill not found.
    """
    def __init__(self, message: str ="Skill not found."):
        super().__init__(f"{message}")
