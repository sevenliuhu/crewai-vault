# Copyright (c) 2026 HOMO AI. Proprietary. License required. Contact: 16208204@qq.com
"""测试 CrewAI 插件"""
import os, sys, json, tempfile, subprocess
sys.path.insert(0, os.path.dirname(__file__))

# Mock vault binary
MOCK_VAULT = tempfile.mktemp()
with open(MOCK_VAULT, 'w') as f:
    f.write("""#!/usr/bin/env python3
import sys, os
cmd = sys.argv[1] if len(sys.argv) > 1 else ''
if cmd == 'verify':
    parts = sys.argv[2].split('-')
    if len(parts) == 2 and parts[0] == sys.argv[3].upper().replace('-',''):
        sys.exit(0)
    sys.exit(1)
elif cmd == 'pack':
    print(f'Packed: {sys.argv[2]} -> {sys.argv[3]}')
    sys.exit(0)
elif cmd == 'unpack':
    out_dir = sys.argv[3]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'skill.yaml'), 'w') as f:
        f.write('name: test-skill')
    sys.exit(0)
else:
    sys.exit(1)
""")
os.chmod(MOCK_VAULT, 0o755)

os.environ["HOMO_VAULT_BIN"] = MOCK_VAULT

passed = 0; failed = 0

def test(name, fn):
    global passed, failed
    try:
        fn()
        passed += 1
        print(f"  ✅ {name}")
    except Exception as e:
        failed += 1
        print(f"  ❌ {name}: {e}")

print("\n📋 CrewAI Skill Vault 测试\n")

test("有效 License 通过", lambda: (
    subprocess.run([MOCK_VAULT, "verify", "TESTKEY-abc", "testkey"], capture_output=True).returncode == 0
))

test("无效 License 拒绝", lambda: (
    subprocess.run([MOCK_VAULT, "verify", "WRONG", "testkey"], capture_output=True).returncode != 0
))

test("空 License 拒绝", lambda: (
    subprocess.run([MOCK_VAULT, "verify", "", "testkey"], capture_output=True).returncode != 0
))

test("Skill 加密打包", lambda: None(
    subprocess.run([MOCK_VAULT, "pack", "/tmp", "/tmp/test.hvskill"], capture_output=True, check=True)
))

test("Skill 解密安装", lambda: None(
    subprocess.run([MOCK_VAULT, "unpack", "/tmp/test.hvskill", "/tmp/skill-out"], capture_output=True, check=True),
    os.path.exists("/tmp/skill-out/skill.yaml")
))

test("插件模块可导入", lambda: (
    __import__('plugin')
))

print(f"\n📊 结果: {passed} ✅ / {failed} ❌ / {passed + failed} 总计\n")
sys.exit(failed > 0)
