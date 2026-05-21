"""
HOMO Skill Vault — CrewAI Plugin
把 Skill Vault 加密引擎接入 CrewAI 的 Skills 系统

安装: pip install homo-crewai-skill-vault
使用: from homo_crewai_skill_vault import SecureSkill
"""
import os
import json
import hashlib
import subprocess
from pathlib import Path

VAULT_BIN = os.environ.get("HOMO_VAULT_BIN", "vault")
VAULT_DIR = Path.home() / ".homo-vault"
SKILLS_DIR = Path.home() / ".crewai" / "skills"
LICENSE_FILE = VAULT_DIR / "license.bin"

class SecureSkill:
    """加密 Skill 的 Python 封装"""
    
    def __init__(self, skill_name, license_key=None):
        self.skill_name = skill_name
        self.license_key = license_key or os.environ.get("HOMO_VAULT_LICENSE")
        self._validate_license()
    
    def _validate_license(self):
        if not self.license_key:
            raise PermissionError("No license key. Set HOMO_VAULT_LICENSE or pass license_key=.")
        result = subprocess.run(
            [VAULT_BIN, "verify", self.license_key, self.skill_name],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode != 0:
            raise PermissionError(f"License invalid: {result.stderr}")
    
    def load_skill(self):
        """加载加密的 Skill 文件"""
        skill_path = SKILLS_DIR / f"{self.skill_name}.hvskill"
        if not skill_path.exists():
            # 尝试下载
            self._download_skill()
        
        result = subprocess.run(
            [VAULT_BIN, "unpack", str(skill_path), 
             str(VAULT_DIR / "runtime" / self.skill_name)],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode != 0:
            raise RuntimeError(f"Failed to unpack skill: {result.stderr}")
        
        # 读取 skill 内容
        skill_file = VAULT_DIR / "runtime" / self.skill_name / "skill.yaml"
        if skill_file.exists():
            return skill_file.read_text()
        return None
    
    @staticmethod
    def pack_skill(skill_dir, output_path, master_key=None):
        """加密 Skill 目录"""
        master_key = master_key or os.environ.get("HOMO_VAULT_KEY")
        if not master_key:
            raise ValueError("Need HOMO_VAULT_KEY to pack skills")
        subprocess.run(
            [VAULT_BIN, "pack", skill_dir, output_path],
            env={**os.environ, "HOMO_VAULT_KEY": master_key},
            check=True, timeout=30
        )

# CrewAI 集成入口
def install_plugin():
    """安装插件到 CrewAI"""
    print("""
    ╔══════════════════════════════════════╗
    ║  HOMO Skill Vault for CrewAI        ║
    ║  🔒 Skills encrypted & protected    ║
    ╚══════════════════════════════════════╝
    """)
    print("Plugin installed. Use: from homo_crewai_skill_vault import SecureSkill")
    print("Set: export HOMO_VAULT_LICENSE=your-license-key")

if __name__ == "__main__":
    install_plugin()
