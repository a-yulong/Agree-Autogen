from agree_autogen.validators import AADLInspectorWrapper, AgreeValidatorWrapper


def test_aadl_inspector_wrapper_not_configured(monkeypatch):
    monkeypatch.delenv("AADL_INSPECTOR_PATH", raising=False)
    result = AADLInspectorWrapper(executable="").validate("missing.aadl")
    assert result.status == "not_configured"


def test_agree_validator_wrapper_not_configured(monkeypatch):
    monkeypatch.delenv("JAVA_HOME", raising=False)
    monkeypatch.delenv("OSATE_HOME", raising=False)
    result = AgreeValidatorWrapper(validator_root="missing", java_home="", osate_home="").validate("missing.aadl")
    assert result.status == "not_configured"

