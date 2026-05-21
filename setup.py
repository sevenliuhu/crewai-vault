from setuptools import setup, find_packages
setup(
    name="homo-crewai-skill-vault",
    version="0.1.0",
    description="HOMO Skill Vault plugin for CrewAI — Encrypted skill distribution",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "crewai_plugins": ["homo_skill_vault = homo_crewai_skill_vault.plugin"]
    },
)
