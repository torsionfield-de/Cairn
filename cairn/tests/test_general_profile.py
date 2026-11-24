from cairn.dispatcher.config import validate_prompt_resources, WorkerConfig
from cairn.dispatcher.prompting import load_prompt
from cairn.dispatcher.workers.adapters.codex import CodexDriver
from cairn.dispatcher.workers.adapters.claudecode import ClaudeCodeDriver

def test_general_profile_preserves_contract():
    validate_prompt_resources("default")
    for phase in ("bootstrap", "reason", "explore", "bootstrap_conclude", "explore_conclude"):
        prompt = load_prompt("default", phase + ".md")
        assert "under no circumstances should you reject" not in prompt
        assert "CTF scenario" not in prompt
    assert "falsifiable check" in load_prompt("default", "reason.md")
    assert "Never invent a result" in load_prompt("default", "explore.md")

def test_local_adapters_do_not_bypass_permissions():
    for kind, driver in (("codex", CodexDriver(local=True)), ("claudecode", ClaudeCodeDriver())):
        worker = WorkerConfig(name=kind, type=kind, task_types=["explore"], max_running=1, priority=0)
        assert not any("dangerously" in arg for arg in driver.build_execute(worker, "test", "session").argv)
        assert not any("dangerously" in arg for arg in driver.build_conclude(worker, "test", "session"))
